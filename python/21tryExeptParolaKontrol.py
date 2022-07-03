from logging import exception
import re
startCheck=True

def checkPassword(passw):
    
    if len(passw)<7:
        raise Exception("parola enaz 7 karakter omalıdır.")
    elif not re.search("[a-z]",passw):
         raise Exception("parola enaz bir küçük harf içermelidir.")
    elif not re.search("[A-Z]",passw):
        raise Exception("parolanız enaz bir büyük harf içermelidir.")
    elif not re.search("[.$?]",passw):
        raise Exception("parolanız [.#${[]}\!%&/()?] karakterlerinden enaz birini içermelidir.")
    

while(startCheck):
    try:
        password=input("şifrenizi giriniz: ")
    
        checkPassword(password)
    except Exception as ex:
        print(ex)
    else:
        print(f"parolanız güvenli yeni parolanız {password} ")
        startCheck=False


