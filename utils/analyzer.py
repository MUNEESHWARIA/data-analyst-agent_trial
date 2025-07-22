def analyze_data(df):
    ans1 = df[(df["Worldwide gross"] >= 2e9) & (df["Year"] < 2020)].shape[0]
    ans2 = df[df["Worldwide gross"] >= 1.5e9].sort_values("Year").iloc[0]["Title"]
    corr = df["Rank"].corr(df["Worldwide gross"])
    return ans1, ans2, corr
