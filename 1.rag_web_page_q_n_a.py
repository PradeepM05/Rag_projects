# Group by child and parent company IDs
# First check which child companies have all 10 days of data
child_counts = df.groupby('insm_issr_bb_co_id').size()
valid_children = child_counts[child_counts == 10].index

# Filter dataframe to only include valid children
filtered_df = df[df['insm_issr_bb_co_id'].isin(valid_children)]

# Calculate correlations between child and parent scores
correlations = []

for (child_id, parent_id), group in filtered_df.groupby(['insm_issr_bb_co_id', 'parent_co_id']):
    if len(group) == 10:  # Double-check we have 10 days of data for this pair
        correlation = group['child_scr'].corr(group['parent_scr'])
        child_name = group['insm_issr_bb_co_nm'].iloc[0]
        parent_name = group['parent_co_nm'].iloc[0]
        correlations.append({
            'child_id': child_id,
            'child_name': child_name,
            'parent_id': parent_id,
            'parent_name': parent_name,
            'correlation': correlation
        })

# Create a dataframe of correlations and sort by absolute correlation (highest first)
corr_df = pd.DataFrame(correlations)
corr_df['abs_correlation'] = corr_df['correlation'].abs()
result = corr_df.sort_values('abs_correlation', ascending=False)

# Display top highly correlated pairs
print(result[['child_name', 'parent_name', 'correlation', 'abs_correlation']].head(10))
