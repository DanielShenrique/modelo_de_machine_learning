import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(filepath_or_buffer="data/Dataset_5971.csv", sep=",")

df["LABEL"].replace("Spam", "spam", inplace=True)
df["LABEL"].replace("Smishing", "smishing", inplace=True)

df.drop(["URL", "EMAIL", "PHONE"], axis=1, inplace=True)

df.drop_duplicates(inplace=True)

df.reset_index(drop=True, inplace=True)

grafico = sns.histplot(data= df, x="LABEL")

plt.savefig("img/grafico_barra_label")