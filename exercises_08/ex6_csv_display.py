from IPython.display import display
import pandas as pd

df = pd.read_csv('data.csv', index_col=0)
display(df.loc['c'])