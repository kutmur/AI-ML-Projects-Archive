# Customer-Segmentation-Analysis-HalilIbrahimKutmur

## Hakkında
Bu proje, denetimsiz makine öğrenmesi algoritmalarından biri olan **K-Means Kümeleme (Clustering)** yöntemini kullanarak AVM müşterilerini segmentlere ayırır. Amaç, müşterilerin yıllık gelirleri ve harcama alışkanlıklarına göre farklı grupları belirleyerek pazarlama stratejileri geliştirmektir.

Proje kapsamında **Elbow Yöntemi (Dirsek Yöntemi)** ile optimal küme sayısı belirlenmiş ve müşteriler 5 farklı hedef kitleye ayrılmıştır.

## Veri Seti
- **Dosya:** `Mall_Customers.csv`
- **Boyut:** 200 Müşteri
- **Özellikler:**
  - `CustomerID`: Müşteri kimlik numarası
  - `Gender`: Cinsiyet
  - `Age`: Yaş
  - `Annual Income (k$)`: Yıllık Gelir
  - `Spending Score (1-100)`: AVM tarafından belirlenen harcama puanı

## Kullanılan Teknolojiler
- **Python**: Veri analizi ve modelleme
- **Pandas & NumPy**: Veri manipülasyonu
- **Matplotlib & Seaborn**: Veri görselleştirme
- **Scikit-learn**: K-Means algoritması ve modelleme

## Proje Adımları
1. **Veri Analizi:** Veri setinin yüklenmesi ve eksik veri kontrolü.
2. **Özellik Seçimi:** Analiz için `Annual Income` ve `Spending Score` sütunlarının seçilmesi.
3. **WCSS & Elbow Yöntemi:** En uygun küme sayısının (K) belirlenmesi.
4. **Modelleme:** K=5 değeri ile K-Means modelinin eğitilmesi.
5. **Görselleştirme:** Oluşturulan kümelerin ve merkez noktalarının (Centroids) grafik üzerinde gösterimi.

## Kurulum
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Repoyu klonlayın veya indirin.
2. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt