from unicodedata import name
import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
print(df)
print("************************************************")
#çalışılan departmana göre 

af=df.groupby("Departman")
for name,group in af:
    print(name)
    print(group)

print("**********************************************")

#gruplardan tek bir grubu alma
bf=df.groupby("Semt").get_group("Kadıköy")
print(bf)

print("*****************************************************")

#departmanların maaş ortalaması
cf=df.groupby("Departman")["Maaş"].mean()
print(cf)

#insan kay. ve muhasebedekilerin yaş max olanlar 
ef=df.groupby("Departman")["Yaş"].max()[["Muhasebe","İnsan Kaynakları"]]
print(ef)
print("********************************************************************")

kf=df.groupby("Departman")["Maaş"].aggregate([np.sum,np.mean,np.max,np.min])
print(kf)

lf=df.groupby("Departman")["Maaş"].aggregate([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]
print(lf)

mf=df.groupby("Departman")["Maaş"].aggregate([np.sum,np.mean,np.max,np.min]).loc[["Muhasebe","Bilgi İşlem"]]
print(mf)


