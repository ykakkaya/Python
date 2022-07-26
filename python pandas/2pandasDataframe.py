import pandas as pd


s1=pd.Series([3,2,6,0])
s2=pd.Series([7,3,9,10])

data = dict (apples=s1 , oranges=s2)
df=pd.DataFrame(data)
print(df)


#kolonlara isim vermediğimiz için 0-1 gibi devam eder
data1=[["ali",75],["yiğit",95],["elif",100],["damla",70]]
df1=pd.DataFrame(data=data1)
print(df1)

#bu şekilde kolon isimlerini parametre olarak verebiliriz
df2=pd.DataFrame(data1,columns=["name","grade"])
print(df2)

#dataframe e dict yapısı verebiliriz sütun sütun veriler
dict={"name":["ali","ayşe","fatma","mehmet"],"grade":[65,85,100,70]}
df3=pd.DataFrame(dict)
print(df3)

#list içerisinde dict olarak satırları yollayabiliriz
data_list=[{"name":"ali","grade":56},
{"name":"ayşe","grade":75},
{"name":"ahmet","grade":96},
{"name":"elif","grade":100}
]

df4=pd.DataFrame(data_list)
print(df4)