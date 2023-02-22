import pandas as pd
import matplotlib.pyplot as plt

def csv_to_df(csv_in: str) -> pd.DataFrame:

    df = pd.read_csv(csv_in, index_col=[0])
    print(df)

    return df


def chart_data(data_df: pd.DataFrame):

    data_df.plot(kind="bar")
    plt.title("Number of software records per year registered with Gateway to Research")
    plt.xlabel("Software records")
    plt.grid(which="major", linestyle="-", linewidth="0.5", color="black")
    #plt.grid(which="minor", linestyle=":", linewidth="0.25", color="black")
    #plt.minorticks_on
    #plt.savefig("./visualisation/sware_recs_per_inst.pdf")
    plt.show()

def main():

    df = csv_to_df("software_in_GTR.csv")
    chart_data(df)

main()