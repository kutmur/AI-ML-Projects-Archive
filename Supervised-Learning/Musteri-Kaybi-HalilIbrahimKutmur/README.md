# Customer-Churn-Prediction-HalilIbrahimKutmur

## Hakkında
Bu proje, makine öğrenmesi (Logistic Regression) kullanarak müşterilerin aboneliklerini iptal etme (churn) riskini tahmin eder. Model; yaş, kullanım sıklığı, müşteri hizmetleri aramaları, ödeme gecikmesi ve toplam harcama gibi 12 farklı müşteri etkileşim özelliğini analiz ederek ikili sınıflandırma (ayrılacak/kalacak) yapar.

## Veri Seti
- **Kaynak:** Müşteri Kaybı Veri Seti (`customer_churn_dataset.csv`)
- **Boyut:** 64.374 satır, 12 özellik (Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay, Subscription Type, Contract Length, Total Spend, Last Interaction, Churn vb.)

## Kurulum
Proje dosyalarını indirdikten sonra gerekli kütüphaneleri kurmak için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt