<div align="center">

# Katkı Rehberi (Contributing Guide)

**AI-ML-Projects-Archive** projesine katkıda bulunmak istediğiniz için teşekkürler!

</div>

---

## Katkı Süreci

### 1. Repository'yi Fork Edin

[Ana repository](https://github.com/TR-AI-ML-Community/AI-ML-Projects-Archive) sayfasına gidin ve sağ üst köşedeki **"Fork"** butonuna tıklayın.

### 2. Clone ve Branch Oluşturun

```bash
# Fork'unuzu clone edin
git clone https://github.com/KULLANICI_ADINIZ/AI-ML-Projects-Archive.git
cd AI-ML-Projects-Archive

# Yeni bir branch oluşturun
git checkout -b proje-ekleme-isim-kategori
```

### 3. Projenizi Ekleyin

İlgili kategorinin altında projeniz için klasör oluşturun:

```bash
mkdir -p Kategori/ProjeAdi-Isim
```

**Klasör İsimlendirme:**
- `LinearRegression-AhmetYilmaz`
- `SentimentAnalysis-MerveKaya`
- `MNIST-CNN-BusraOz`

### 4. Dosya Yapısı

Her proje şu yapıda olmalıdır:

```
ProjeAdi-Isim/
├── README.md              # ZORUNLU
├── main.py veya main.ipynb
├── requirements.txt
├── data/                  # Küçük veri setleri (max 5MB)
└── images/                # Sonuç görselleri
```

### 5. Commit ve Push

```bash
git add .
git commit -m "[Kategori] Proje İsmi - İsim"
git push origin proje-ekleme-isim-kategori
```

### 6. Pull Request Oluşturun

GitHub'da fork'unuza gidin ve **"Compare & pull request"** butonuna tıklayın.

---

## Kategoriler

Projenizi doğru kategoriye ekleyin:

| Kategori | İçerik |
|----------|--------|
| `Supervised-Learning/` | Regresyon, Sınıflandırma |
| `Unsupervised-Learning/` | Kümeleme, PCA |
| `Deep-Learning/` | CNN, RNN, Transfer Learning |
| `Natural-Language-Processing-NLP/` | Sentiment Analysis, Chatbot |
| `Computer-Vision-CV/` | Object Detection, Image Segmentation |
| `Reinforcement-Learning/` | Q-Learning, Game AI |

---

## README Şablonu

```markdown
# Proje Adı

## Hakkında
[Projenin ne yaptığını kısaca açıklayın]

## Veri Seti
- **Kaynak:** [Link]
- **Boyut:** X satır, Y özellik

## Kurulum
```bash
pip install -r requirements.txt
python main.py
```

## Sonuçlar
- **Doğruluk:** %XX
- **F1-Score:** XX

## Geliştirici
**[İsim]** - [@github](https://github.com/kullanici)
```

---

## Kurallar

### Yapılması Gerekenler
- README.md dosyası ekleyin
- Açıklayıcı kod yorumları yazın
- requirements.txt oluşturun
- Küçük dosyalar yükleyin (max 10MB)

### Yapılmaması Gerekenler
- Büyük model dosyaları yüklemeyin (link verin)
- Büyük veri setleri yüklemeyin (link verin)
- Başkalarının kodunu kopyalamayın

---

## Yaygın Hatalar

**Büyük Dosya Yükleme:**
```bash
# Model/veri linki verin
echo "Model: https://drive.google.com/..." > models/model_link.txt
```

**Fork Güncelleme:**
```bash
git remote add upstream https://github.com/TR-AI-ML-Community/AI-ML-Projects-Archive.git
git fetch upstream
git merge upstream/main
```

**Yanlış Kategori:**
- Deep Learning altına Linear Regression eklemeyin
- Doğru kategoriyi seçin

---

## İletişim

- **GitHub Discussions:** Sorular için
- **Issues:** Hata bildirimi için

---

<div align="center">

Made by TR AI/ML Community

</div>
