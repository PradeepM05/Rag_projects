
def find_correlations_memory_efficient(pivot_df, threshold=0.8, min_periods=5, batch_size=500):
    """Calculate correlations between companies in memory-efficient batches with improved error handling"""
    
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
                        
                        # Safe calculation of correlation
                        try:
                            # Get series without NaN values
                            series1 = df_i[comp1].dropna()
                            series2 = df_i[comp2].dropna()
                            
                            # Find common indices (dates) where both have values
                            common_idx = series1.index.intersection(series2.index)
                            
                            if len(common_idx) >= min_periods:
                                # Check for zero variance (constant values)
                                s1 = series1.loc[common_idx]
                                s2 = series2.loc[common_idx]
                                
                                if s1.std() > 0 and s2.std() > 0:
                                    # Use pandas correlation which handles edge cases better
                                    corr = s1.corr(s2)
                                    
                                    if not pd.isna(corr) and abs(corr) >= threshold:
                                        results.append({
                                            'company1_id': comp1,
                                            'company2_id': comp2,
                                            'correlation': corr,
                                            'periods': len(common_idx)
                                        })
                        except Exception as e:
                            # Optionally log errors if needed
                            print(f"Error calculating correlation between {comp1} and {comp2}: {e}")
                            continue
            else:
                # When comparing between different batches
                batch_companies_j = all_companies[j:min(j+batch_size, num_companies)]
                df_j = pivot_df[batch_companies_j]
                
                for comp1 in batch_companies_i:
                    for comp2 in batch_companies_j:
                        try:
                            series1 = df_i[comp1].dropna()
                            series2 = df_j[comp2].dropna()
                            
                            common_idx = series1.index.intersection(series2.index)
                            
                            if len(common_idx) >= min_periods:
                                s1 = series1.loc[common_idx]
                                s2 = series2.loc[common_idx]
                                
                                if s1.std() > 0 and s2.std() > 0:
                                    corr = s1.corr(s2)
                                    
                                    if not pd.isna(corr) and abs(corr) >= threshold:
                                        results.append({
                                            'company1_id': comp1,
                                            'company2_id': comp2,
                                            'correlation': corr,
                                            'periods': len(common_idx)
                                        })
                        except Exception as e:
                            # Optionally log errors if needed
                            print(f"Error calculating correlation between {comp1} and {comp2}: {e}")
                            continue
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_df = results_df.sort_values('correlation', ascending=False)
    
    return results_df
