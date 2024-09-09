from IPython.display import display
import pandas as pd

df = pd.read_json('data.json')
display(df)