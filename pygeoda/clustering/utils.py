from ..libgeoda import gda_betweensumofsquare, gda_totalsumofsquare, gda_withinsumofsquare, flat_2dclusters

def calculate_clustering_statistics(cluster_ids, in_data, num_obs):
    """Calculate clustering statistics including sum of squares measures.
    
    Args:
        cluster_ids: Cluster assignments for each observation
        in_data: Input data in VecVecDouble format
        num_obs: Number of observations
        
    Returns:
        dict: Dictionary containing clustering statistics:
            - Total sum of squares
            - Within-cluster sum of squares
            - Between-cluster sum of squares (Total within-cluster sum of squares)
            - Ratio of between to total sum of squares
            - Clusters (flattened cluster assignments)
    """
    between_ss = gda_betweensumofsquare(cluster_ids, in_data)
    total_ss = gda_totalsumofsquare(in_data)
    ratio = between_ss / total_ss
    within_ss = gda_withinsumofsquare(cluster_ids, in_data)
    # for the case that constraint is used, the length of within_ss is not the same as cluster_ids
    # check if the length of within_ss is the same as cluster_ids
    # if not, add 0 to the within_ss to make it the same length as cluster_ids
    if len(within_ss) != len(cluster_ids):
        within_ss = [0]*(len(cluster_ids) - len(within_ss)) + list(within_ss)

    return {
        "Total sum of squares": total_ss,
        "Within-cluster sum of squares": within_ss,
        "Total within-cluster sum of squares": sum(within_ss),
        "Total between-cluster sum of squares": between_ss,
        "The ratio of between to total sum of squares": ratio,
        "Clusters": flat_2dclusters(num_obs, cluster_ids),
    }
