from datetime import datetime
from datetime import timedelta

simdi=datetime.today()
result=datetime.now()
result=datetime.now().year
result=datetime.now().day
result=datetime.now().today()
#Y yıl bilgisi B ay bilgisi A gün bilgisi X saat bilgisi d ayın kaçıncı günü bilgisini bize verir
result=datetime.strftime(simdi,'%Y,%B,%A %X %d')


#%H	Hour(00-23) %M	Minute(00-59) %S Second(00-59) %x	Local version of date(12/31/18) 
#%X	Local version of time(17:41:00)
result=datetime.strftime(simdi,'%H %M %S')
print(result)

t='15 April 2022'
dt=datetime.strptime(t,"%d %B %Y")
print(dt)

bugun=datetime.now()
birthday=datetime(1984,1,11)
yas=bugun-birthday
print(yas)