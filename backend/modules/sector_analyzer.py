
def get_sector_weight(sector):
    weights = {
        "L1": 88,
        "DeFi": 75,
        "NFT": 42,
        "AI": 64,
        "Gaming": 51
    }
    return weights.get(sector, 50)
