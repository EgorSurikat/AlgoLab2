import pandas as pd
from seaborn import lineplot
import matplotlib.pyplot as plt


# создает графики с логарифмическими осями по заданным в файле данным
# файл был создан вручную
def create_preparation_graph(column_name):
    data_file = pd.read_csv("../data/data.csv")
    lineplot(data_file, x="rectangles", y=column_name, hue="alg")
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


create_preparation_graph("time_total")