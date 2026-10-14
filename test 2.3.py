# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
# 2-  Liste Kaç elemanlıdır ?
# 3-  Listenin ilk ve son elemanı nedir ?
# 4-  Mazda değerini Toyota ile değiştirin.
# 5-  Mercedes listenin bir elemanı mıdır ?
# 6-  Listenin -2 indeksindeki değer nedir ?
# 7-  Listenin ilk 3 elemanını alın.
# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# 10- Listenin son elemanını silin.
# 11- Liste elemanlarını tersten yazdırınız.


#1
car = ["BMW", "Mercedes", "Opel", "Mazda"]
#2
print(len(car))
#3
print(car[0] + car[-1])
#4
print(car)
car[3] = "Toyota"
print(car)
#5
a = "mercedes" in car 
print(a)
#6
print(car[-2])
#7
print(car[0] + car[1] + car[2])
#8
print(car)
car[-1] = "Totoya"
car[-2] = "Renault"
print(car)
#9
print(car + ["Audi", "Nissan"])
#10
del car[-1]
print(car)
#11
print(car[::-1])

