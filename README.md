# Step 1: Create the unique source (equivalent to your CTE)
unique_source = (pnc_results_output_table
                 .filter(F.col("lexicon_id") == 58)
                 .select("caseno", "rule_id", "keywords", "category1", "category2", "category3")
                 .distinct())

# Step 2: INNER JOIN and aggregate (matches your SQL exactly)
pnc_aggregated = (unique_source.alias("u")
                  .join(df_rpt_custint_concerns.alias("r"),
                        (F.col("u.caseno") == F.col("r.cmplnid")) &
                        (F.col("r.cdt1_subcmplnid") == 1) & 
                        (F.col("r.cncrn_cncrnid") == 1),
                        "inner")  # INNER JOIN like your SQL
                  .groupBy("u.caseno", "r.cmplnid", "r.cdt1_subcmplnid", "r.cncrn_cncrnid")
                  .agg(
                      F.concat_ws(",", F.collect_set("u.rule_id")).alias("ruleid"),
                      F.concat_ws(",", F.collect_set("u.keywords")).alias("keywords"),
                      F.concat_ws(",", F.collect_set("u.category1")).alias("reg_bucket"),
                      F.concat_ws(",", F.collect_set("u.category2")).alias("reg_bucket_2"),
                      F.concat_ws(",", F.collect_set("u.category3")).alias("categorylevel3")
                  ))

# Step 3: Now join this back to get ALL original columns
df_rpt_custint_concerns_with_pnc = (df_rpt_custint_concerns
                                   .join(pnc_aggregated,
                                         df_rpt_custint_concerns.cmplnid == pnc_aggregated.cmplnid,
                                         "left")
                                   .drop(pnc_aggregated.cmplnid)
                                   .drop(pnc_aggregated.cdt1_subcmplnid)
                                   .drop(pnc_aggregated.cncrn_cncrnid)
                                   .drop("caseno"))
