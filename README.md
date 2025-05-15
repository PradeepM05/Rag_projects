1
1
1
1
1
1
import pandas as pd
import numpy as np
from tqdm import tqdm  # For progress tracking

# Assuming df is your dataframe with columns: cob_dt, insm_issr_bb_co_id, max_score
# And pivot_df is your pivoted dataframe with dates as index and company IDs as columns

def find_correlations_memory_efficient(pivot_df, threshold=0.8, min_periods=5, batch_size=1000):
    """Calculate correlations between companies in memory-efficient batches"""
    
    all_companies = pivot_df.columns.tolist()
    num_companies = len(all_companies)
    results = []
    
    # Process companies in batches to avoid memory issues
    for i in tqdm(range(0, num_companies, batch_size)):
        batch_companies_i = all_companies[i:min(i+batch_size, num_companies)]
        df_i = pivot_df[batch_companies_i]
        
        # Only calculate correlations with companies we haven't compared yet
        for j in range(i, num_companies, batch_size):
            if i == j:
                # When comparing within the same batch, only do upper triangle
                for idx1, comp1 in enumerate(batch_companies_i):
                    for idx2 in range(idx1+1, len(batch_companies_i)):
                        comp2 = batch_companies_i[idx2]
                        series1 = df_i[comp1].dropna()
                        series2 = df_i[comp2].dropna()
                        
                        # Find common indices (dates) where both have values
                        common_idx = series1.index.intersection(series2.index)
                        
                        if len(common_idx) >= min_periods:
                            # Calculate correlation just for these two companies
                            corr = np.corrcoef(
                                series1.loc[common_idx].values, 
                                series2.loc[common_idx].values
                            )[0, 1]
                            
                            if abs(corr) >= threshold:
                                results.append({
                                    'company1_id': comp1,
                                    'company2_id': comp2,
                                    'correlation': corr,
                                    'periods': len(common_idx)
                                })
            else:
                # When comparing between different batches
                batch_companies_j = all_companies[j:min(j+batch_size, num_companies)]
                df_j = pivot_df[batch_companies_j]
                
                for comp1 in batch_companies_i:
                    for comp2 in batch_companies_j:
                        series1 = df_i[comp1].dropna()
                        series2 = df_j[comp2].dropna()
                        
                        common_idx = series1.index.intersection(series2.index)
                        
                        if len(common_idx) >= min_periods:
                            corr = np.corrcoef(
                                series1.loc[common_idx].values, 
                                series2.loc[common_idx].values
                            )[0, 1]
                            
                            if abs(corr) >= threshold:
                                results.append({
                                    'company1_id': comp1,
                                    'company2_id': comp2,
                                    'correlation': corr,
                                    'periods': len(common_idx)
                                })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_df = results_df.sort_values('correlation', ascending=False)
    
    return results_df

# Usage:
# Adjust batch_size based on your available RAM (smaller batches = less RAM)
correlated_pairs = find_correlations_memory_efficient(pivot_df, threshold=0.8, min_periods=5, batch_size=500)
1
1
1
1
1
11
1
