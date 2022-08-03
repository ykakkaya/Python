from cmath import pi
import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(4,100,75).reshape(15,5),columns=["col1","col2","col3","col4","col5"])
print(df)
#columns isimlerini getirir
print(df.columns)
#ilk 5 kayıtı getirir
print(df.head())
#son 5 kayıtı getirir
print(df.tail())
#col3 e ait ilk 5 kayıtı getirir
print(df["col3"].head())
filter=(df%2==0)&(df<=45)
print(filter)
print(df[filter])