
def check_correlation(child_token):
    chain_mapping = {
        "JUPUSDT": "SOLUSDT",
        "GMXUSDT": "ARBUSDT"
    }
    leader = chain_mapping.get(child_token, None)
    if leader:
        return {"leader": leader, "correlation_score": 0.87}
    return {"leader": None, "correlation_score": 0}
