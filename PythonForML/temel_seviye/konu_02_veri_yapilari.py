'''
Konu 2: İleri Düzey Veri Yapıları (List, Dict, Set, Tuple) ve Big-O Karmaşıklığı
1. Teorik Anlatım
Python'da verileri hangi yapıda (structure) tuttuğun, uygulamanın hızını doğrudan belirler.
Örneğin, bir uygulamanın arka planında binlerce kullanıcının yetenek (skill) havuzunu tararken 
veya bir makine öğrenmesi modeline metin verisi beslerken yanlış veri yapısını seçmek, 
kodunun dakikalarca donmasına sebep olabilir.

Burada Big-O Notation (Algoritmik Karmaşıklık) devreye girer:

List (Liste): Esnektir ama içinde bir eleman aramak (örn: if x in liste:) O(N) zaman alır. 
Yani listede 1 milyon eleman varsa, Python arka planda en kötü senaryoda 1 milyon kez kontrol yapar.

Set (Küme) ve Dict (Sözlük): Arka planda "Hash Table" (Özet Tablosu) mantığıyla çalışırlar. 
İçlerinde milyonlarca veri olsa bile bir elemanın var olup olmadığını bulmak O(1) (neredeyse anında) sürer. Eşsiz veri tutmak ve süper hızlı arama yapmak için Set kullanılır.

Tuple (Demet): Listelere benzer ama değiştirilemezler (immutable). Değiştirilemez oldukları için Python 
onları bellekte daha sıkı paketler ve listelerden daha az RAM tüketirler. Sabit kalacak koordinatlar 
veya model hiperparametreleri için idealdir.
'''
################################################################################################################
#2. Temel Örnek
#Farklı veri yapılarının temel tanımlamaları:

# List: Sıralı ve değiştirilebilir
yetenekler_listesi = ["Python", "C", "Flutter", "Machine Learning"]

# Tuple: Sıralı ama değiştirilemez (Hafıza dostu)
model_input_boyutu = (1920, 1080, 3) 

# Set: Sırasız, eşsiz elemanlar ve süper hızlı arama
benzersiz_kullanici_idleri = {101, 102, 103, 104}

# Dict: Anahtar-Değer (Key-Value) çiftleri, hızlı erişim
kullanici_profili = {
    "isim": "Ali",
    "premium_mu": True,
    "uygulama_surumu": "1.0.0"}

################################################################################################################
#3. İleri Düzey Örnek (O(N) vs O(1) Hız Testi)

#Hız farkını gözlerimizle görmek için time modülünü kullanarak bir performans testi yapalım:

import time
import sys

# 10000 milyon elemanlı bir liste ve bir küme oluşturalım
buyuk_liste = list(range(10_000_000))
buyuk_kume = set(range(10_000_000))

aranan_sayi = 9_999_999 # En sondaki eleman

# LİSTE ARAMASI (O(N) - Yavaş)
baslangic = time.time()
var_mi = aranan_sayi in buyuk_liste
bitis = time.time()
print(f"Listede arama süresi: {bitis - baslangic:.6f} saniye")

# KÜME ARAMASI (O(1) - Çok Hızlı)
baslangic = time.time()
var_mi = aranan_sayi in buyuk_kume
bitis = time.time()
print(f"Kümede arama süresi:  {bitis - baslangic:.6f} saniye")
print(f"kapladıkları alan list:{sys.getsizeof(buyuk_liste)},set:{sys.getsizeof(buyuk_kume)}")
#(Bu kodu çalıştırdığında Küme'nin Listeden binlerce kat daha hızlı olduğunu göreceksin.)


e_posta = list(range(1_000_000))
e_posta2 = set(range(1_000_000))

aradigimiz_sayi = -1

baslangic1 = time.time()
bulunuyor_mu = aradigimiz_sayi in e_posta
bitis1 = time.time()
print(f"Listede arama süresi: {bitis1 - baslangic1:.6f} saniye")

baslangic2 = time.time()
bulunuyor_mu = aradigimiz_sayi in e_posta2
bitis2 = time.time()
print(f"kümede arama süresi: {bitis2 - baslangic2:.6f} saniye")


