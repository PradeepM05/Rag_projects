import pandas as pd
import numpy as np

# Function to process companies in chunks
def find_correlated_companies(df, chunk_size=1000, threshold=0.7):
    # Get all unique companies
    all_companies = df['insm_issr_bb_co_id'].unique()
    n_companies = len(all_companies)
    
    # Create a mapping of company IDs to names for quick lookup
    company_names = dict(zip(df['insm_issr_bb_co_id'], df['insm_issr_bb_co_nm']))
    
    # List to store results
    correlated_pairs = []
    
    # Process in chunks
    for i in range(0, n_companies, chunk_size):
        # Get current chunk of companies
        chunk_companies = all_companies[i:i+chunk_size]
        print(f"Processing companies {i} to {min(i+chunk_size, n_companies)} of {n_companies}")
        
        # Filter data for these companies
        chunk_df = df[df['insm_issr_bb_co_id'].isin(chunk_companies)]
        
        # Pivot data
        pivoted = chunk_df.pivot(index='cob_dt', 
                                columns='insm_issr_bb_co_id', 
                                values='sgl_dy_pxchg_scr')
        
        # Calculate correlation with ALL companies
        # This is the memory-intensive part but more manageable with chunks
        corr = pivoted.corrwith(df.pivot(index='cob_dt', 
                                        columns='insm_issr_bb_co_id', 
                                        values='sgl_dy_pxchg_scr'))
        
        # Find high correlations
        for company in chunk_companies:
            high_corrs = corr[abs(corr) > threshold]
            high_corrs = high_corrs[high_corrs.index != company]  # Remove self-correlation
            
            # Add to results
            for other_company, corr_value in high_corrs.items():
                if company < other_company:  # Avoid duplicates
                    correlated_pairs.append((
                        company, 
                        other_company,
                        company_names.get(company, "Unknown"),
                        company_names.get(other_company, "Unknown"),
                        corr_value
                    ))
    
    # Convert to DataFrame
    results = pd.DataFrame(correlated_pairs, 
                          columns=['Company1_ID', 'Company2_ID', 
                                  'Company1_Name', 'Company2_Name', 
                                  'Correlation'])
    
    return results.sort_values(by='Correlation', key=abs, ascending=False)

# Use the function
results = find_correlated_companies(df, chunk_size=500, threshold=0.8)
print(results.head(20))
