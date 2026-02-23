'''
Konu 3: Akış Kontrolü ve Döngü Optimizasyonları (List Comprehensions & Generators)
1. Teorik Anlatım
Yapay zeka modellerini eğitirken veya büyük veri setlerini işlerken döngüler (for, while)
kodunun en çok vakit geçirdiği yerlerdir. Python'da standart bir for döngüsü kullanıp boş 
bir listeye .append() ile eleman eklemek oldukça yavaştır. Neden mi? Çünkü Python her adımda 
listenin boyutunu kontrol eder, gerekirse hafızada yeni yer ayırır ve fonksiyon çağırma (overhead) 
maliyeti yaratır.

Bunun yerine Python'da List Comprehension adı verilen tek satırlık döngü yapıları kullanılır. 
Bu yapılar doğrudan Python'ın yazıldığı C dilindeki alt seviye (low-level) optimizasyonları kullandığı 
için standart döngülerden genellikle %30 ila %50 daha hızlı çalışır.

Daha da büyük verilerle (örneğin 100 GB'lık bir metin dosyası) çalışırken RAM'i patlatmamak 
için ise Generator Expression kullanırız. Generator'lar tüm veriyi RAM'e yüklemek yerine, 
sadece sen "bana sıradakini ver" dediğinde o anlık veriyi üretip sonra silen (tembel - lazy evaluation) 
harika yapılardır.
'''
#2. Temel Örnek
#Klasik yöntem ve modernize edilmiş Pythonic yöntem:
sayilar = [1, 2, 3, 4, 5]

# Klasik Yöntem (Yavaş)
kareler_klasik = []
for sayi in sayilar:
    kareler_klasik.append(sayi ** 2)

# List Comprehension Yöntemi (Hızlı ve Temiz)
kareler_hizli = [sayi ** 2 for sayi in sayilar]

# Generator Expression Yöntemi (Hafıza Dostu - RAM'de yer kaplamaz)
# Köşeli parantez [] yerine normal parantez () kullanılır.
kareler_generator = (sayi ** 2 for sayi in sayilar)

#3. İleri Düzey Örnek (Hız ve Hafıza Testi Bir Arada)
#Milyonlarca veriyi işlerken List Comprehension'ın hızı ve Generator'ın hafıza dostu olmasını görelim:
import time
import sys

veri_boyutu = 10_000_000

# 1. STANDART FOR DÖNGÜSÜ
baslangic = time.time()
liste_for = []
for i in range(veri_boyutu):
    liste_for.append(i * 2)
bitis = time.time()
print(f"For Döngüsü Süresi: {bitis - baslangic:.4f} sn | Boyut: {sys.getsizeof(liste_for)} byte")

# 2. LIST COMPREHENSION
baslangic = time.time()
liste_comp = [i * 2 for i in range(veri_boyutu)]
bitis = time.time()
print(type(liste_comp))
print(f"List Comprehension Süresi: {bitis - baslangic:.4f} sn | Boyut: {sys.getsizeof(liste_comp)} byte")

# 3. GENERATOR EXPRESSION
baslangic = time.time()
generator_comp = (i * 2 for i in range(veri_boyutu))
bitis = time.time()
print(type(generator_comp))
print(f"Generator Süresi: {bitis - baslangic:.4f} sn | Boyut: {sys.getsizeof(generator_comp)} byte")
'''
Çok Önemli Bir Uyarı: "Generator Bir Kez Tüketilir"
Generator'ı bir listeye çevirdiğinde veya içinde bir kez for döngüsüyle döndüğünde o generator boşalır.

Örneğin:,

gen = (x for x in range(3))

liste_1 = list(gen) # Bu çalışır: [0, 1, 2]
liste_2 = list(gen) # Bu boş döner: [] !!!
'''

#şimdi çok iyi bir boru hattı(pipeline)örneği ekliyorum aşşağıya

# 1. ADIM: Kaynak (Range aslında bir generatordur, sayıları tek tek üretir)
# 10 milyon sayı varmış gibi hayal edelim, ama RAM'de yer kaplamaz.
sayi_kaynagi = range(10_000_000)

# 2. ADIM: Filtre Borusu (Sadece çift olanları seçer)
# Burada henüz hiçbir hesaplama yapılmadı, sadece "kural" tanımlandı.
cift_sayi_filtresi = (x for x in sayi_kaynagi if x % 2 == 0)

# 3. ADIM: İşlem Borusu (Gelen her sayının karesini alır)
# Hala RAM tertemiz, sadece borular birbirine bağlandı.
kare_alma_isleme = (y ** 2 for y in cift_sayi_filtresi)

# 4. ADIM: Motor (Veriyi çekmeye başladığımız an)
print("Boru hattı çalıştırılıyor...\n")

# Sadece ilk 5 sonucu çekip görelim (tüm listeyi bitirmemize gerek yok)
for i, sonuc in enumerate(kare_alma_isleme):
    print(f"Boru hattından çıkan {i+1}. veri: {sonuc}")
    if i == 4: # 5 tane aldık ve boru hattını durdurduk
        break

print("-" * 30)
print(f"Bütün bu boru hattı nesnesinin boyutu: {sys.getsizeof(kare_alma_isleme)} bayt")
# isterseniz kare_alma_isleme ve cift_sayi_filtresi  kısımlarındaki () ları [] ile değiştirip boyut farkını görebilirsiniz
