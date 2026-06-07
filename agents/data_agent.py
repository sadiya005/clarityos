import pandas as pd


def analyze_data(df):

    insights = []

    insights.append(f"Rows: {df.shape[0]}")
    insights.append(f"Columns: {df.shape[1]}")

    numeric_cols = df.select_dtypes(include="number").columns

    if "Sales" in df.columns:

        insights.append(
            f"Average Sales: {round(df['Sales'].mean(), 2)}"
        )

        insights.append(
            f"Highest Sale: {round(df['Sales'].max(), 2)}"
        )

    if "Profit" in df.columns:

        insights.append(
            f"Average Profit: {round(df['Profit'].mean(), 2)}"
        )

        insights.append(
            f"Lowest Profit: {round(df['Profit'].min(), 2)}"
        )

    if "Discount" in df.columns:

        insights.append(
            f"Average Discount: {round(df['Discount'].mean(), 2)}"
        )

    if "Region" in df.columns and "Sales" in df.columns:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        best_region = region_sales.index[0]
        worst_region = region_sales.index[-1]

        insights.append(
            f"Top Performing Region: {best_region}"
        )

        insights.append(
            f"Lowest Performing Region: {worst_region}"
        )

    missing_values = df.isnull().sum().sum()

    insights.append(
        f"Missing Values: {missing_values}"
    )

    return insights