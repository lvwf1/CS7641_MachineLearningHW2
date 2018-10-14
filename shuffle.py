import pandas as pd

df = pd.read_csv('SeasonsStats.csv')
df['C']=0
df['PF']=0
df['SF']=0
df['SG']=0
df['PG']=0
for index, row in df.iterrows():
    if row['Pos']==1.0:
        print('Center')
        df.set_value(index, 'C', 1)
    if row['Pos']==2.0:
        print('Power Forward')
        df.set_value(index, 'PF', 1)
    if row['Pos']==3.0:
        print('Small Forward')
        df.set_value(index, 'SF', 1)
    if row['Pos']==4.0:
        print('Shooting Guard')
        df.set_value(index, 'SG', 1)
    if row['Pos']==5.0:
        print('Point Guard')
        df.set_value(index, 'PG', 1)
df.to_csv('SeasonsStats2.csv')