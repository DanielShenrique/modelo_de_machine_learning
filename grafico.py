import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(filepath_or_buffer="data/tabela_tratada.csv", sep=",")

df["LABEL"].replace( -1 , "Ham", inplace=True)
df["LABEL"].replace( 0 , "Spam", inplace=True)
df["LABEL"].replace( 1 , "Smishing", inplace=True)

sns.set_theme(style="darkgrid")
sns.set_palette("Paired")

grafico = sns.countplot(data= df, x="LABEL")

plt.xlabel("Classes")
plt.ylabel("Quantidade")

plt.savefig("img/grafico_barra_label")