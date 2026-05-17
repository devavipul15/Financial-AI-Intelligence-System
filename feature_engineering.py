def create_features(df):

    df["transaction_velocity"] = (
        df["transaction_amount"] / (df["account_age_days"] + 1)
    )

    return df