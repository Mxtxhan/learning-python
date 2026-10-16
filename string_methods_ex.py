website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
# 6-  'website' içinde '.com' ifadesi var mı?
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

#SOLN
print(" Hello World ".strip())   #1
print(website[11:21])  #2
print(course.lower()) #3
print(website.count("a"))         #4
print(website.startswith("www"), website.endswith(".com"))  #5
print(website.find(".com"))      #6
print(course.isalpha())         #7
print(website.center(50,"*"))        #8
print(course.replace(" ", "-"))   #9
print("Hello World".replace("World", "There")) #10
print(course.split()) #11