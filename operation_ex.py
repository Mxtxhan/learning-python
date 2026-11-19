x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir?
#2- y'nin x'e kalansız bölümünü hesaplayınız.
#3- (x,y,z) toplamının mod 3'ü nedir?
#4- y'nin x. kuvvetini hesaplayınız.
#5- x *y, z numbers işlemine göre z'nin küpü kaçtır?
#6- x, *y, z = numbers işlemine göre y'nin değerleri topamı kaçtır?
'''1'''
int(input("Birinci Sayıyı Giriniz): ")) * int(input("İkinci Sayıyı Giriniz: ")) - (x + y + z)
'''2'''
print(y//x)
'''3'''
print((x+y+z)%3)
'''4'''
print(y**x)
'''5'''
x, *y , z = numbers
print(z**3)
'''6'''
x, *y , z = numbers
print(sum(y)) 
print(y[0] + y[1] + y[2])


# 1- Girilen 2 sayıdan hangisi büyüktür ?
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)
'''1'''
a = [str(input("Birinci Sayıyı Giriniz: ")), str(input("İkinci Sayıyı Giriniz: "))]
print(max(a) + " sayısı daha büyüktür.")
'''2'''
vize1 = int(input("Birinci Vize Notunu Giriniz: "))
vize2 = int(input("İkinci Vize Notunu Giriniz: "))
final = int(input("Final Notunu Giriniz: "))
ort = (vize1 + vize2)/2 * 0.6 + final * 0.4
print("Ortalamanız: " + str(ort))
print("Dersten Geçildi Mi?: " + str(ort >= 50))
'''3'''
sayig = int(input("Bir Sayı Giriniz: "))
print("Girilen Sayı Çift Mi?: " + str(sayig % 2 == 0))
print("Girilen Sayı Tek Mi?: " + str(sayig % 2 != 0))
'''4'''
sayig2 = int(input("Bir Sayı Giriniz: "))
print("Girilen Sayı Pozitif Mi?: " + str(sayig2 > 0))
print("Girilen Sayı Negatif Mi?: " + str(sayig2 < 0))
print("Girilen Sayı Sıfır Mı?: " + str(sayig2 == 0))
'''5'''
email = "metehan0bayhan@icloud.com"
sifre = "abc123"
useremail = input("Email Adresinizi Giriniz: ")
userpass = input("Parolanızı Giriniz: ")
print("Email Doğru Mu?: " + str(useremail == email))
print("Parola Doğru Mu?: " + str(userpass == sifre))

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = 'email@sadikturan.com'
# password = 'abc123'
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
'''1'''
a = int(input("Bir Sayı Giriniz: "))
print("Girilen Sayı 0-100 Arasında Mı?: " + str((a > 0 and a < 100)))
'''2'''
a = int(input("Bir Sayı Giriniz: "))
print("Girilen Sayı Pozitif Çift Mi?: " + str((a > 0 and a % 2 == 0)))
'''3'''
useremail = input("Email Adresinizi Giriniz: ")
userpass = input("Parolanızı Giriniz: ")
print("Giriş Başarılı Mı?: " + str((useremail == email and userpass == sifre)))
print("Giriş Başarısız Mı?: " + str((useremail != email or userpass != sifre)))
'''4'''
sayi1 = int(input("Birinci Sayıyı Giriniz: "))
sayi2 = int(input("İkinci Sayıyı Giriniz: "))
sayi3 = int(input("Üçüncü Sayıyı Giriniz: "))
liste = [sayi1, sayi2, sayi3]
print("Girilen Sayıların Sıralaması: " + str(sorted(liste, reverse=True)))
'''5'''
vize1 = int(input("Birinci Vize Notunu Giriniz: "))
vize2 = int(input("İkinci Vize Notunu Giriniz: "))
final = int(input("Final Notunu Giriniz: "))
ort = (vize1 + vize2)/2 * 0.6 + final * 0.4
print("Geçtiniz Mi?: " + str((ort >= 50 and final >= 50) or final >= 70))
'''6'''
usrname = input("Adınızı Giriniz: ")
usrweight = float(input("Kilonuzu Giriniz (kg): "))
usrheight = float(input("Boyunuzu Giriniz (m): "))
print("Kilo İndeksiniz: " + str(usrweight / (usrheight ** 2)))
print("Zayıf Mısınız?: " + str(usrweight / (usrheight ** 2) < 18.5 and usrweight / (usrheight ** 2) > 0))
print("Normal Misin?: " + str(usrweight / (usrheight ** 2) >= 18.5 and usrweight / (usrheight ** 2) <= 24.9))
print("Fazla Kilolu Musunuz?: " + str(usrweight / (usrheight ** 2) >= 25.0 and usrweight / (usrheight ** 2) <= 29.9))
print("Şişman Mısınız?: " + str(usrweight / (usrheight ** 2) >= 30.0 and usrweight / (usrheight ** 2) <= 34.9))
