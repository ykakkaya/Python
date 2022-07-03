import math
import random


list=["ali",1,"veli",455]
#listeden rastgele 1 eleman seçer
print(random.choice(list))
#verilen listeden rastgele belirtilen kadar eleman seçer
print(random.sample(list,3))
#belirtilen aralıkta int tipinde rastgele sayı üretir
print(random.randint(5,10))
#belirtilen aralıkta float tipinde sayı üretir
print(random.uniform(4,9))
#verilen değeri yukarı yuvarlar
print(math.ceil(4.98))
print(math.ceil(3.01))
#verilen değeri aşagıya yuvarlar
print(math.floor(4.98))
print(math.floor(3.01))
#verilen değerin karekökünü alır
print(math.sqrt(225))
#verilen değerin faktoriyelini alır
print(math.factorial(6))

