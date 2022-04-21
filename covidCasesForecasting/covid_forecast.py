import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


CSV_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_cases.csv"


def load_data() -> pd.DataFrame:

    df = pd.read_csv(
        CSV_URL,
        sep=",",
        usecols=["date", "World"],
    )
    df.columns = ["date", "World"]

    df.columns.values[1] = "cases"

    df["date"] = pd.to_datetime(df["date"], format="%Y.%m.%d")
    df = df.sort_values(by="date")

    assert (pd.date_range(start=df.date.iloc[0], end=df.date.iloc[-1]) == df.date).all()

    return df


def predict_cases_in_days(df: pd.DataFrame, days_to_predict: int) -> list:

    list_days_predicted = list()
    epidemic_started_days_ago = int((df["date"].max() - df["date"].min()).days)

    x = np.array(df.index).reshape(-1, 1)
    y = np.array(df["cases"]).reshape(-1, 1)

    poly_feature = PolynomialFeatures(degree=12)
    x = poly_feature.fit_transform(x)

    model = LinearRegression()
    model.fit(x, y)

    acurracy = model.score(x, y)
    assert acurracy > 0.9

    for day in range(1, days_to_predict + 1):
        list_days_predicted.append(
            int(
                model.predict(
                    poly_feature.fit_transform([[epidemic_started_days_ago + day]])
                )
            )
        )

    return list_days_predicted


if __name__ == "__main__":
    data_frame = load_data()

    days = None

    while days is None or days < 0:
        days = input("How many days to predict? ")
        try:
            days = int(days)
        except ValueError:
            print("Please enter a valid number of days.")
            days = None

    cases_predicted = predict_cases_in_days(data_frame, days_to_predict=days)

    for day, cases in enumerate(cases_predicted):
        print(f"{day + 1} --> {cases}")
