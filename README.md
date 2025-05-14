import pandas as pd
import numpy as np
from collections import defaultdict
import heapq

def find_top_correlated_companies_optimized(df, top_n=20, min_days=5):
    """
    Most memory-efficient approach for finding correlations
    
    This approach:
    1. Groups data by company
    2. Calculates correlations on-the-fly
    3. Only keeps track of top_n correlations
    """
    # Process dataframe to create a dictionary of company data by date
    company_data = defaultdict(dict)
    
    for _, row in df.iterrows():
        company = row['insm_issr_bb_co_nm']
        date = row['cob_dt']
        zscore = row['sgl_dy_pxchg_scr']
        company_data[company][date] = zscore
    
    # Get list of companies
    companies = list(company_data.keys())
    print(f"Processing {len(companies)} companies")
    
    # Initialize heap for top correlations
    min_heap = []  # will store (correlation, company1, company2)
    
    # Function to calculate Pearson correlation
    def calc_correlation(x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
        sum_x2 = sum(x_i**2 for x_i in x)
        sum_y2 = sum(y_i**2 for y_i in y)
        
        numerator = n * sum_xy - sum_x * sum_y
        denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
        
        if denominator == 0:
            return 0
        return numerator / denominator
    
    # Process all pairs
    pairs_processed = 0
    total_pairs = len(companies) * (len(companies) - 1) // 2
    
    for i, company1 in enumerate(companies):
        if i % 100 == 0 and i > 0:
            print(f"Processed {i}/{len(companies)} companies, {pairs_processed}/{total_pairs} pairs")
        
        data1 = company_data[company1]
        dates1 = set(data1.keys())
        
        for j in range(i+1, len(companies)):
            company2 = companies[j]
            data2 = company_data[company2]
            dates2 = set(data2.keys())
            
            # Find common dates
            common_dates = dates1.intersection(dates2)
            
            # Only calculate correlation if we have enough common days
            if len(common_dates) >= min_days:
                # Extract aligned data
                x = [data1[date] for date in common_dates]
                y = [data2[date] for date in common_dates]
                
                # Calculate correlation
                corr = calc_correlation(x, y)
                
                # Update top correlations
                if np.isfinite(corr):  # Ensure correlation is valid
                    if len(min_heap) < top_n:
                        heapq.heappush(min_heap, (corr, company1, company2))
                    elif corr > min_heap[0][0]:
                        heapq.heappushpop(min_heap, (corr, company1, company2))
            
            pairs_processed += 1
    
    # Sort results by correlation (descending)
    results = sorted(min_heap, key=lambda x: x[0], reverse=True)
    return results
