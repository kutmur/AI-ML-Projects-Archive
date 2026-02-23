#Konu Anlatımı
'''
1.
C gibi daha alt seviye dillerde değişken tanımlarken bellekte tam olarak o verinin tipine göre 
(örneğin bir integer için 4 byte) yer ayrılır ve değişken doğrudan o hafıza adresini temsil eder. 
Ancak Python'da her şey bir objedir ve değişkenler sadece bu objelere işaret eden "etiketlerdir".

x = 5 yazdığında bellekte sadece 5 değeri tutulmaz; bu objenin referans
sayacı (reference count), tip bilgisi ve boyutu gibi ekstra meta veriler de saklanır.
Bu yüzden Python'da basit bir tam sayı, C'deki karşılığına göre bellekte çok daha fazla yer kaplar
(genellikle 28 byte civarı). Özellikle yapay zeka ve makine öğrenmesi algoritmaları geliştirirken devasa 
veri setleriyle (tensörler, devasa matrisler) çalışacağın için, arka planda hafızanın nasıl yönetildiğini bilmek,
ileride bellek sızıntılarını (memory leak) ve "Out of Memory" hatalarını önlemenin ilk adımıdır.

2.
Python'da tip belirtmek zorunlu değildir, atanan değere göre tip dinamik olarak belirlenir:

Python
epoch_sayisi = 100         # int
ogrenme_orani = 0.005      # float
model_adi = "YapaySinirAgi" # str

3.
Kodun okunabilirliğini artırmak, hataları önceden yakalamak ve otomatik tamamlamayı 
güçlendirmek için Type Hinting kullanırız. sys kütüphanesi ile de objelerin gerçekte 
ne kadar RAM tükettiğine bakarız:

Python
import sys
from typing import List

# Type hinting ile değişken tanımlama
learning_rate: float = 0.01
batch_size: int = 32
layer_sizes: List[int] = [128, 64, 32]

# Hafıza tüketimi kontrolü (Bayt cinsinden)
print(f"Bir float ({learning_rate}) hafızada {sys.getsizeof(learning_rate)} bayt kaplar.")
print(f"Bir int ({batch_size}) hafızada {sys.getsizeof(batch_size)} bayt kaplar.")
print(f"Bir liste ({layer_sizes}) hafızada {sys.getsizeof(layer_sizes)} bayt kaplar.")

'''
import sys 
#örnek makine öğrenmesi modeli parametreleri 
epoch_sayisi:int = 40
learning_rate:float = 0.01
model_ismi:str ="Valentein"
aktif_mi:bool = True
#kapladıkları yerlere bakalım 
print("epoch_sayisi değişkeninin boyutu:",sys.getsizeof(epoch_sayisi),"byte")
print("learning_rate değişkeninin boyutu:",sys.getsizeof(learning_rate),"byte")
print("model_ismi değişkeninin boyutu:",sys.getsizeof(model_ismi),"byte")
print("aktif_mi değişkeninin boyutu:",sys.getsizeof(aktif_mi),"byte")


