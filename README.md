# Programlama Dilleri Laboratuvarı Projesi - Siber Matrix
---

![Siber Matrix Logo](assets/matrixfont.png)

---
> **Not:** Oyundaki tüm sprite'lar kendimizin olup hazır sprite'lar kullanılmamıştır.

## Oyun Hakkında

***Siber Matrix***, Matrix filminden esinlenilmiş, Python ve Arcade kütüphanesi kullanılarak geliştirilmiş 2D bir kaçış oyunudur. Oyuncu, düşen engellerden kaçınarak yüksek skor yapmaya çalışır. Oyun, Matrix evreninin ikonik yeşil kod yağmuru arka planı ve temalarıyla süslenmiştir.

## 🎮 Oyun Özellikleri

- **Zorluk Sistemi**
  - Oyun ilerledikçe artan zorluk seviyeleri
  - Süreye bağlı olarak hızlanan oynanış
  - Rastgele oluşturulan engel desenleri

- **Görsel ve Ses**
  - Matrix temalı retro-fütüristik arayüz
  - Orijinal Matrix müzikleri ve efektleri
  - Özel karakter ve engel tasarımları

- **Oyun İçi Özellikler**
  - Anlık skor ve en yüksek skor takibi
  - Oyun içi yardım menüsü
  - Kolay öğrenilen, ustalaşması zor oynanış
  - Oyunu duraklatma ve devam ettirme

- **Kullanıcı Deneyimi**
  - Basit ve etkili kontroller
  - Duyarlı karakter hareketleri
  - Net ve anlaşılır arayüz

---

## 🖼️ Oyun Görselleri

| Ana Menü | Oyun İçi Görünüm |
|:---:|:---:|
| <img src="assets/readme/ana_menu.png" width="400"> | <img src="assets/readme/oyun_ici.png" width="400"> |


| Morpheus Karşılaşması | Nasıl Oynanır |
|:---:|:---:|
| <img src="assets/readme/morpheus_ekrani.png" width="400"> | <img src="assets/readme/nasil_oynanir.png" width="400"> |

| Oyun Sonu |
|:---:|
| <img src="assets/readme/game_over.png" width="400"> |


> 🖥️ *Oyun içi görseller yüksek kalitede Matrix temalı grafikler içerir*

---

## 🎮 Nasıl Oynanır ?

### 🚀 Başlangıç
- Ana menüden __"OYNA"__ butonuna tıklayarak oyunu başlatın
- İstersen arkaplan müziğini açıp kapatabilirsin
- Oyuna başlamadan önce nasıl oynanır bilgisi için __"Nasıl Oynanır"__ butonuna tıklayabilirsin

### 🎯 Oyunun Amacı
- Düşen engellerden kaçınarak mümkün olduğunca uzun süre hayatta kalmak
- Yüksek skor yaparak en iyi skorunuzu kırmak
- Farklı zorluk seviyelerinde başarılı olmak

### 🎮 Kontroller
| Tuş | İşlev |
|------|--------|
| ⬅️ Sol Ok | Karakteri sola hareket ettirir |
| ➡️ Sağ Ok | Karakteri sağa hareket ettirir |
| ⏯️ ESC | Oyunu duraklatır/devam ettirir |
| ❌ Q | Oyunu kapatır |


### 🏆 Zorluk Sistemi
- Oyunda her seviye arttıkça oyun hızlanır
- Her seviyeyi geçmek için farklı zorluk !!
- En yüksek skorunuz kaydedilir ve bir sonraki oyununuzda görüntülenir.

## 🎭 Karakterler ve Öğeler

### 🦉 Ana Karakter - PauSiber Baykuşu
- Oyunun ana karakteri olan PauSiber'in ihtişamlı baykuşu
- Düşen engellerden kaçınmak için sola ve sağa hareket eder
- Hızlı reflekslerle en yüksek skora ulaşmaya çalışır

### 💊 Seçim Hapı
| Hap | Etkisi | Sonuç | Görünüm |
|-----|--------|--------|---------|
| 🔴 Kırmızı Hap | Mücadeleye devam etme seçeneği | Oyun içinde kalıp savaşmaya devam edersin | ![Kırmızı Hap](assets/heroes/red_pill.png) |
| 🔵 Mavi Hap | Gerçeği görme seçeneği | Oyunu bırakıp ana menüye döner | ![Mavi Hap](assets/heroes/blue_pill.png) |


> **Not:** Matrix'te olduğu gibi, mavi hap seni güvenli bir yere götürürken, kırmızı hap gerçekleri görmeni ve mücadeleye devam etmeni sağlar.

### ⚠️ Engeller
Oyun boyunca karşılaşacağınız 9 farklı engel bulunmaktadır. Her engelin boyutu ve puan değeri farklıdır. Engellerden kaçınarak hayatta kalmaya çalışın!

---

## ⚙️ Kurulum Rehberi

### 1. Python'un Kurulumu
1. [Python'un resmi web sitesini](https://www.python.org/downloads/) ziyaret edin
2. İşletim sisteminize uygun olan en son Python sürümünü indirin
3. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretlediğinizden emin olun

### 2. Gerekli Kütüphanelerin Yüklenmesi
Terminal veya komut istemini açıp aşağıdaki komutları çalıştırın:

```bash
# Arcade kütüphanesini yükleme
pip install arcade==2.6.12

# GIF hareketleri için gerekli kütüphaneler
pip install pillow==9.5.0

# Oyunun çalışması için gerekli diğer bağımlılıklar
pip install pyglet==2.0.10
```

### 3. Oyunu İndirme ve Çalıştırma

#### Windows Kullanıcıları İçin:

1. **[İndir](https://github.com/mlihgenel/siber-matrix/archive/refs/heads/main.zip)** butonuna tıklayarak oyunu indirin
2. İndirilen `siber-matrix-main.zip` dosyasına sağ tıklayıp "Tümünü çıkar..." seçeneğini seçin
3. Açılan klasörde `main.py` dosyasına çift tıklayın

Eğer çalışmazsa:
1. `main.py` dosyasına sağ tıklayın
2. "Birlikte Aç" > "Python" seçeneğini seçin

Veya komut istemcisi (CMD) ile:
```
git clone https://github.com/kullaniciadi/siber-matrix.git
cd siber-matrix
python main.py
```

#### macOS/Linux Kullanıcıları İçin:
```bash
# Projeyi klonlama
git clone https://github.com/kullaniciadi/siber-matrix.git

# Klasöre geçiş yapma
cd siber-matrix

# Oyunu başlatma
python3 main.py
```

## 👥 Geliştirici Ekibi

| Ad Soyad | E-posta |
|----------|---------|
| Ahmet Melih Genel  | [mlihgenel@gmail.com](mailto:mlihgenel@gmail.com)
| Mehmet Mert Kırgıl | [kirgilmert@gmail.com](mailto:kirgilmert@gmail.com)

