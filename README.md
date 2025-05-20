# Assuming df_ibs and df_corr are already loaded
# First, let's rename columns to make the joins clearer
df_ibs_copy = df_ibs.rename(columns={'insm_issr_bb_co_id': 'company_id', 
                                    'td_ins_pty_coper_id': 'coper_id'})

# Merge child companies
result = df_corr.merge(
    df_ibs_copy,
    left_on='child_co_id',
    right_on='company_id',
    how='left'
).rename(columns={'coper_id': 'child_coper_id'})

# Merge parent companies
result = result.merge(
    df_ibs_copy,
    left_on='parent_co_id',
    right_on='company_id',
    how='left',
    suffixes=('_child', '_parent')
).rename(columns={'coper_id': 'parent_coper_id'})

# Select relevant columns
final_result = result[['child_co_id', 'child_co_name', 'child_coper_id', 
                      'parent_co_id', 'parent_co_name', 'parent_coper_id', 
                      'correlation', 'abs_correlation']]

# Display the result
print(final_result)
