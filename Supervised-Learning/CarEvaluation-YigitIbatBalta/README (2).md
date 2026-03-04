Car Evaluation - Decision Tree

Bu projede car_evaluation.csv veri seti kullanılarak bir Decision Tree modeli ile araba değerlendirme sınıflandırması yapılmıştır. Veri setindeki kategorik değişkenler OrdinalEncoder ile sayısal değerlere dönüştürülmüştür ve modelin performansı test edilmiştir.

Kullanılan Kütüphaneler

- pandas
- numpy
- sklearn
- matplotlib
- seaborn

Yapılan Adımlar

1. Veri seti pandas ile yüklendi.
2. Sütun isimleri düzenlendi.
3. "doors" ve "persons" sütunlarındaki "more" ve "5more" değerleri sayısal değerlere çevrildi.
4. Veri train-test split ile eğitim ve test olarak ayrıldı.
5. Kategorik sütunlar OrdinalEncoder ile encode edildi.
6. DecisionTreeClassifier modeli oluşturuldu.
7. GridSearchCV kullanılarak en iyi hiperparametreler bulundu.
8. Model test verisi üzerinde değerlendirildi.

Model

- Model: Decision Tree Classifier
- Hyperparameter tuning: GridSearchCV

Sonuç

Modelin test doğruluk değeri:

Accuracy: 0.9398

Bu sonuç Decision Tree modelinin veri seti üzerinde oldukça iyi bir performans verdiğini göstermektedir.
