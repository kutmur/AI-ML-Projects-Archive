'''
Konu 4: Fonksiyonlar, Scope (Kapsam) ve Closure'lar
1. Teorik Anlatım
Python'da fonksiyonlar "First-Class Citizens" (Birinci Sınıf Vatandaş) olarak kabul edilir. 
Yani bir fonksiyonu tıpkı bir tam sayı (integer) veya string gibi bir değişkene atayabilir, 
başka bir fonksiyona parametre olarak gönderebilir veya bir fonksiyonun içinden başka bir fonksiyon 
döndürebilirsin.

Burada iki çok önemli kavram devreye girer:

Scope (Kapsam - LEGB Kuralı): Python bir değişkeni ararken şu sırayı izler: 
Local (Fonksiyonun içi) -> Enclosing (İç içe fonksiyonlarda bir üst fonksiyonun içi) -> Global 
(Dosyanın en üstü) -> Built-in (Python'ın kendi gömülü isimleri, örn: print, len).

Closure (Kapanış): Bir dış fonksiyonun, içindeki bir iç fonksiyonu (inner function) 
döndürmesi (return) ve iç fonksiyonun, dış fonksiyon çalışmasını bitirip silinse bile onun 
içindeki değişkenleri hatırlamaya devam etmesidir. Bu, Orta Seviye'de göreceğimiz "Decorators" 
(Dekoratörler) konusunun temelidir ve sınıflara (OOP) başvurmadan hafızada durum (state) tutmanın 
en hafif (lightweight) yoludur.
'''
#Temel Örnek (Scope - LEGB)
carpan = 10  # Global Scope

def hesapla(deger):
    # Local Scope
    carpan = 5 # Bu sadece bu fonksiyonun içinde geçerlidir, globali etkilemez.
    return deger * carpan

print(hesapla(2))  # Çıktı: 10 (Local carpan kullanıldı)
print(carpan)      # Çıktı: 10 (Global carpan değişmedi)
'''
3. İleri Düzey Örnek (Closure - State Tutma)
Diyelim ki bir yapay zeka modelinin eğitimindeki "Loss" (Kayıp) değerlerinin hareketli ortalamasını 
(moving average) tutmak istiyoruz. Bunun için koca bir class yazmak yerine hafif bir Closure 
kullanabiliriz:'''
def ortalama_hesaplayici():
    # Enclosing Scope (Dış fonksiyonun değişkenleri)
    gecmis_degerler = []  # Bu liste, dış fonksiyon bitse bile hafızada yaşayacak!
    
    def hesapla(yeni_deger):
        # Local Scope (İç fonksiyon)
        gecmis_degerler.append(yeni_deger)
        toplam = sum(gecmis_degerler)
        return toplam / len(gecmis_degerler)
    
    return hesapla # Fonksiyonu ÇALIŞTIRMADAN objesini döndürüyoruz.

# Closure'ı başlatalım
model_loss_takip = ortalama_hesaplayici() 
# Artık 'ortalama_hesaplayici' çalıştı ve bitti. Ama içindeki 'gecmis_degerler' listesi hala yaşıyor!

print(f"1. Epoch Loss Ortalaması: {model_loss_takip(10.0)}") # Liste: [10.0] -> Ort: 10.0
print(f"2. Epoch Loss Ortalaması: {model_loss_takip(6.0)}")  # Liste: [10.0, 6.0] -> Ort: 8.0
print(f"3. Epoch Loss Ortalaması: {model_loss_takip(2.0)}")  # Liste: [10.0, 6.0, 2.0] -> Ort: 6.0
#--------------------------------------------------------------------------------------------------------
def learning_rate_scheduler(baslangic_lr, dusme_orani):
    mevcut_lr = baslangic_lr
    adim = 0
    
    def dusur():
        nonlocal mevcut_lr, adim # Dışarıdaki değişkenleri değiştireceğimizi belirttik
        adim += 1
        
        # Her adımda mevcut LR'ı düşürelim (Lineer düşüş simülasyonu)
        mevcut_lr -= dusme_orani
        
        # Negatif değerlere düşmemesini sağlayalım (Güvenlik önlemi)
        if mevcut_lr < 0:
            mevcut_lr = 0
            
        return adim, mevcut_lr
    
    return dusur

# 1. Fabrikayı kur (Başlangıç: 0.1, Düşme: 0.01)
lr_guncelleyici = learning_rate_scheduler(0.1, 0.01)

# 2. Aracı (İşçiyi) çalıştır ve sonuçları gör
print("--- Learning Rate Scheduler Başlatıldı ---")

for i in range(4):
    epoch, yeni_lr = lr_guncelleyici()
    print(f"Epoch {epoch}: Yeni Learning Rate -> {yeni_lr:.3f}")