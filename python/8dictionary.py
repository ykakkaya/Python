# {key: value} şeklinde yazılır.

plakalar={"kayseri":38,"istanbul":34,"izmir":35,"nevşehir":50}
print(plakalar)
print(plakalar["kayseri"])
print(plakalar["istanbul"])


#dictionary içinde dictionary tanımladık

users={
    'yakup':{
        'age':38,
        'email':'ykakkaya@hotmail.com',
        'job':'developer'
    },
    'yigit':{
        'age':6,
        'email':'yakkaya@hotmail.com',
        'job':'child'
    }

}

#yigit in tüm bilgilerine ulaştık

print(users['yigit'])

#yakup un alt bilgilerinden email e ulaştık

print(users['yakup']['email'])
