import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')


def get_average(list_to_be_avg):
    list_length = len(list_to_be_avg)
    total = sum(list_to_be_avg)
    avg = total/list_length
    return avg


def get_averages_all_columns(list_to_be_avg):
    column_averages = {}
    for col in df.columns:
        if df[col].dtype in [int, float]:
            column_averages[col] = get_average(df[col])
    return column_averages


def graph_scatter_x_and_y(list_x, list_y, x_label, y_label, title):
    plt.scatter(list_x, list_y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()


graph_scatter_x_and_y(df['bmi'], df['charges'], "BMI",
                      "Charges", "BMI vs Charges")
