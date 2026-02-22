# Smartphone-Usage-Stress-Prediction-HalilIbrahimKutmur

## Hakkında
Bu proje, makine öğrenmesi (Logistic Regression) kullanarak akıllı telefon kullanıcılarının kullanım alışkanlıklarına göre stres seviyelerini tahmin eder. Model; yaş, meslek, günlük telefon/sosyal medya kullanım süresi, uyku saati, uygulama sayısı gibi 11 farklı özelliği analiz ederek çoklu sınıflandırma (1-10 stres seviyesi) yapar.

Veri seti üzerinde ön işleme (preprocessing) yapılarak kategorik veriler (Gender, Occupation, Device_Type) Label Encoding ile sayısal değerlere dönüştürülmüş ve özellikler arasındaki korelasyonlar incelenmiştir.

## Veri Seti
- **Kaynak:** [Smartphone Usage and Productivity Dataset](https://www.kaggle.com/datasets)
- **Boyut:** 50,001 satır, 13 sütun
- **Hedef Değişken:** `Stress_Level` (1-10 arası stres seviyesi)
- **Özellikler (Features):**
  - `Age`: Yaş
  - `Gender`: Cinsiyet (Male/Female/Other)
  - `Occupation`: Meslek (Student/Professional/Freelancer/Business Owner)
  - `Device_Type`: Cihaz türü (Android/iOS)
  - `Daily_Phone_Hours`: Günlük telefon kullanım süresi (saat)
  - `Social_Media_Hours`: Günlük sosyal medya süresi (saat)
  - `Work_Productivity_Score`: İş verimliliği puanı (1-10)
  - `Sleep_Hours`: Günlük uyku süresi (saat)
  - `App_Usage_Count`: Kullanılan uygulama sayısı
  - `Caffeine_Intake_Cups`: Günlük kafein tüketimi (fincan)
  - `Weekend_Screen_Time_Hours`: Hafta sonu ekran süresi (saat)

## Model Performansı
Modelin test verisi üzerindeki performansı:
- **Doğruluk (Accuracy):** ~%10 (çok sınıflı problem nedeniyle düşük)
- **F1-Score (weighted):** ~0.10

> **Not:** Stres seviyesi 1-10 arasında 10 farklı sınıfa sahip olduğundan ve veriler rastgele dağılım gösterdiğinden, Logistic Regression modeli bu problem için yeterli performans gösterememektedir. Daha iyi sonuçlar için Random Forest, Gradient Boosting veya Neural Network modelleri denenebilir.

## Kurulum
Proje dosyalarını indirdikten sonra gerekli kütüphaneleri kurun:

```bash
pip install -r requirements.txt
```

## Kullanım
Jupyter Notebook'u çalıştırın:

```bash
jupyter notebook main.ipynb
```