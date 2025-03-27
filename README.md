# Araç Fiyat Tahmin Modeli Geliştirme ve Dağıtımı

## 📖 Proje Hakkında
Bu proje, araç fiyatlarını tahmin etmek için PyTorch kullanarak bir makine öğrenimi modeli geliştirmeyi amaçlamaktadır. Veri seti, 258 araç ve 9 özellik içermektedir. Model, bu özellikleri kullanarak araçların satılabilir fiyatlarını tahmin edecektir.

### Veri Seti ve Örnek Çözüm
Veri seti ve örnek çözüm için aşağıdaki bağlantılara göz atabilirsiniz:
- [Araç Fiyatlarını Tahmin Etme ile İlgili Makale](https://thecleverprogrammer.com/2020/09/21/predict-car-prices-with-machine-learning/)
- [Hugging Face - Araç Fiyat Tahmin Uygulaması](https://huggingface.co/spaces/btulftma/car_price_predict)

## 🔧 Kullanılan Kütüphaneler
Proje, veri analizi ve modelleme için aşağıdaki kütüphaneleri kullanmaktadır:
- `torch`: Derin öğrenme modelleri için.
- `pandas`: Veri analizi için.
- `numpy`: Sayısal hesaplamalar için.
- `sklearn`: Veri ön işleme için.

## 🛠️ Proje Adımları
1. **Giriş ve Veri Seti Yükleme**: Proje, gerekli kütüphanelerin yüklenmesi ve veri setinin okunması ile başlar.
2. **Veri Ön İşleme ve Temizlik**: Kategorik veriler sayısallaştırılır ve gereksiz sütunlar çıkarılır. Özellikler ölçeklendirilir.
3. **PyTorch Veri Seti Oluşturma**: Veriler eğitim ve test setlerine ayrılır ve PyTorch DataLoader'a dönüştürülür.
4. **Sinir Ağı Modeli Tasarımı**: Daha gelişmiş bir sinir ağı mimarisi oluşturulur.
5. **Model Eğitimi ve Optimizasyon**: Model, eğitim verileri ile eğitilir ve en iyi performansı elde etmek için optimizasyon yapılır.
6. **Model Değerlendirme ve Tahmin**: Eğitim sonuçları görselleştirilir ve örnek tahminler yapılır.
7. **Modelin HuggingFace için Kaydedilmesi**: Model ve ön işleme araçları kaydedilir ve HuggingFace platformuna yüklenmek üzere hazırlanır.

## 📦 Sonuç
Geliştirilen model, araç fiyat tahminlerinde başarılı sonuçlar vermektedir. Eğitim süreci boyunca validasyon kaybının düzenli olarak azalması, modelin iyi öğrendiğini göstermektedir. Bu model, otomobil piyasasında fiyat tahmini yapmak isteyen kullanıcılar için değerli bir araç olacaktır.
