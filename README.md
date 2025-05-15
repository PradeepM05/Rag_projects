-- First, identify companies with high volatility (|z-score| >= 2)
WITH high_volatility_companies AS (
    SELECT DISTINCT insm_issr_bb_co_id
    FROM CDN_ACTIVIATE.EQUITY_PRICING_SCR_HIST
    WHERE ABS(sgl_dy_pxchg_scr) >= 2.0
    -- Optionally, add date range if needed
    -- AND cob_dt BETWEEN '28-Apr-2025' AND '02-May-2025'
),

-- Then, for these companies, get all data points across all dates
high_vol_data AS (
    SELECT 
        h.cob_dt,
        h.insm_issr_bb_co_id,
        -- If there are multiple scores per company-date, get the max
        MAX(h.sgl_dy_pxchg_scr) as max_score
    FROM CDN_ACTIVIATE.EQUITY_PRICING_SCR_HIST h
    JOIN high_volatility_companies hv ON h.insm_issr_bb_co_id = hv.insm_issr_bb_co_id
    -- Include date range if needed
    -- WHERE h.cob_dt BETWEEN '28-Apr-2025' AND '02-May-2025'
    GROUP BY h.cob_dt, h.insm_issr_bb_co_id
)

-- Final output
SELECT * FROM high_vol_data
ORDER BY cob_dt, insm_issr_bb_co_id;



------------

import pandas as pd
import numpy as np
import cx_Oracle
from tqdm import tqdm

def get_high_volatility_data():
    # Replace with your actual connection details
    connection = cx_Oracle.connect("username/password@host:port/service_name")
    
    query = """
    -- SQL query from above
    """
    
    print("Fetching high volatility data from database...")
    df = pd.read_sql(query, connection)
    connection.close()
    
    print(f"Fetched data for {df['insm_issr_bb_co_id'].nunique()} high volatility companies")
    return df

def calculate_correlations(df, threshold=0.8, min_periods=5):
    # Pivot the data
    print("Pivoting data...")
    pivot_df = df.pivot(index='cob_dt', columns='insm_issr_bb_co_id', values='max_score')
    
    # Calculate correlation matrix
    print(f"Calculating correlation matrix for {len(pivot_df.columns)} companies...")
    try:
        corr_matrix = pivot_df.corr(min_periods=min_periods)
        
        # Extract high correlations
        print("Extracting highly correlated pairs...")
        results = []
        for i in tqdm(range(len(corr_matrix.columns))):
            for j in range(i+1, len(corr_matrix.columns)):
                comp1 = corr_matrix.columns[i]
                comp2 = corr_matrix.columns[j]
                corr = corr_matrix.iloc[i, j]
                
                if not pd.isna(corr) and abs(corr) >= threshold:
                    results.append({
                        'company1_id': comp1,
                        'company2_id': comp2,
                        'correlation': corr
                    })
        
        results_df = pd.DataFrame(results)
        if not results_df.empty:
            results_df = results_df.sort_values('correlation', ascending=False)
        
        print(f"Found {len(results_df)} highly correlated pairs")
        return results_df
    
    except MemoryError:
        print("Memory error occurred. Switching to batched processing...")
        return calculate_correlations_batched(pivot_df, threshold, min_periods)

def calculate_correlations_batched(pivot_df, threshold=0.8, min_periods=5, batch_size=500):
    # Batched correlation calculation (same as before)
    all_companies = pivot_df.columns.tolist()
    num_companies = len(all_companies)
    results = []
    
    for i in tqdm(range(0, num_companies, batch_size)):
        batch_companies_i = all_companies[i:min(i+batch_size, num_companies)]
        df_i = pivot_df[batch_companies_i]
        
        for j in range(i, num_companies, batch_size):
            if i == j:
                # Within-batch correlations
                batch_corr = df_i.corr(min_periods=min_periods)
                for idx1 in range(len(batch_companies_i)):
                    for idx2 in range(idx1+1, len(batch_companies_i)):
                        comp1 = batch_companies_i[idx1]
                        comp2 = batch_companies_i[idx2]
                        corr = batch_corr.iloc[idx1, idx2]
                        
                        if not pd.isna(corr) and abs(corr) >= threshold:
                            results.append({
                                'company1_id': comp1,
                                'company2_id': comp2,
                                'correlation': corr
                            })
            else:
                # Cross-batch correlations
                batch_companies_j = all_companies[j:min(j+batch_size, num_companies)]
                df_j = pivot_df[batch_companies_j]
                
                for comp1 in batch_companies_i:
                    for comp2 in batch_companies_j:
                        try:
                            s1 = df_i[comp1].dropna()
                            s2 = df_j[comp2].dropna()
                            
                            common_idx = s1.index.intersection(s2.index)
                            
                            if len(common_idx) >= min_periods:
                                corr = s1.loc[common_idx].corr(s2.loc[common_idx])
                                
                                if not pd.isna(corr) and abs(corr) >= threshold:
                                    results.append({
                                        'company1_id': comp1,
                                        'company2_id': comp2,
                                        'correlation': corr
                                    })
                        except Exception as e:
                            continue
    
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_df = results_df.sort_values('correlation', ascending=False)
    
    print(f"Found {len(results_df)} highly correlated pairs")
    return results_df

# Main execution
def main():
    # Get data from database with filtering already applied
    df = get_high_volatility_data()
    
    # Calculate correlations
    correlated_pairs = calculate_correlations(df, threshold=0.8, min_periods=5)
    
    # Save results
    correlated_pairs.to_csv("high_volatility_correlated_companies.csv", index=False)
    print("Results saved to high_volatility_correlated_companies.csv")
    
    # Display top correlations
    print("\nTop 20 most correlated pairs:")
    print(correlated_pairs.head(20))

if __name__ == "__main__":
    main()


111111111111111111111111
2
1
1
1
1

1
