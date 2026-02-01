# House-Price-Prediction-HalilIbrahimKutmur

## Hakkında
Bu proje, makine öğrenmesi (Linear Regression) kullanarak evlerin fiziksel özelliklerine göre satış fiyatını tahmin eder. Model, evin metrekaresi, oda sayısı, banyo sayısı ve mobilya durumu gibi 12 farklı özelliği analiz ederek sayısal bir fiyat tahmini (regresyon) yapar.

Veri seti üzerinde ön işleme (preprocessing) yapılarak kategorik veriler ('yes'/'no') sayısal değerlere dönüştürülmüş ve özellikler arasındaki korelasyonlar incelenmiştir.

## Veri Seti
- **Kaynak:** [Housing Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
- **Boyut:** 545 satır, 13 sütun.
- **Hedef Değişken:** `price` (Fiyat)
- **Özellikler (Features):**
  - `area`: Evin metrekaresi
  - `bedrooms`: Yatak odası sayısı
  - `bathrooms`: Banyo sayısı
  - `stories`: Kat sayısı
  - `mainroad`: Ana yola yakınlık (0/1)
  - `guestroom`: Misafir odası var mı? (0/1)
  - `basement`: Bodrum katı var mı? (0/1)
  - `hotwaterheating`: Sıcak su sistemi var mı? (0/1)
  - `airconditioning`: Klima var mı? (0/1)
  - `parking`: Otopark kapasitesi
  - `prefarea`: Tercih edilen bölge mi? (0/1)
  - `furnishingstatus`: Eşya durumu (Mobilyalı/Yarı Mobilyalı/Mobilyasız)

## Model Performansı
Modelin test verisi üzerindeki performansı:
- **R² Score:** 0.636
- **Mean Absolute Error (MAE):** 865,891

## Kurulum
Proje dosyalarını indirdikten sonra gerekli kütüphaneleri kurun:

```bash
pip install -r requirements.txt