import pandas as pd
import numpy as np

df=pd.read_csv("datasets//nba.csv")
print(df.head())
print(df.info())
af=df.dropna()
print(af)
print("******************************************")
af["Name"]=af["Name"].str.upper()
print(af)
print("******************************************")
af["Team"]=af["Team"].str.replace(" ","-")
print(af)
print("******************************************")

bf=af[af["Position"].str.contains("PG")]
filt=(bf["Age"]<25) & (bf["Weight"]>=180)
print(bf[filt].count()["Name"])

print("******************************************")

filt2=(af["College"]=="Kentucky") & (af["Team"]=="Utah-Jazz")
print(af[filt2])