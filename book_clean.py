import pandas as pd
import numpy as np

df = pd.read_csv('Datasets/olympics.csv', header=1)

new_names = {'Unnamed: 0': 'Country',
            '? Summer': 'Summer',
            '01 !': 'Gold',
            '02 !': 'Silver',
            '03 !': 'Bronze',
            '? Winter': 'Winter',
            '01 !.1': 'Gold 1',
            '02 !.1': 'Silver 1',
            '03 !.1': 'Bronze 1',
            '? Games': '# of Games',
            '01 !.2': 'Gold 2',
             '02 !.2': 'Silver 2',
             '03 !.2': 'Bronze 2'}

df.rename(columns=new_names, inplace=True)
column_names = df.columns



extr = df['Country'].str.extract(r'^(\D{8})', expand=False)
#print(extr.head())
#print(df.loc[])
