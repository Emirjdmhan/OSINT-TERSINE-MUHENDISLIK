# OSINT ve Tersine Mühendislik Aracı

---

Bu proje, **OSINT (Açık Kaynak İstihbaratı)** ve **tersine mühendislik** tekniklerini bir araya getirerek dijital ayak izlerini analiz etmeye yönelik geliştirilmiş basit bir araçtır. Amacımız, herkese açık kaynaklardan akıllıca veri toplamak, bu verilerden anlamlı bağlantılar kurmak ve potansiyel güvenlik açıklarını ortaya çıkarmaktır.

## Özellikler

Uygulama, menü tabanlı bir arayüz aracılığıyla aşağıdaki temel özellikleri sunmaktadır:

* **Sosyal Medya Analizi:** Kamuoyuna açık sosyal medya hesaplarından veri toplama veya ilgili profil linklerini oluşturma yeteneği.
* **Alan Adı & IP Sorgulama:** Hedefin IP ve alan adı (domain) bilgileriyle ilgili detaylı WHOIS ve IP adresi bilgileri sağlar.
* **Veri İhlali Kontrolü:** Belirtilen e-posta adresleri veya kullanıcı adlarının geçmişte veri sızıntılarına uğrayıp uğramadığını kontrol etmek için harici kaynaklara yönlendirme yapar.
* **Tersine Mühendislik:** Dijital dosyaların (resim, PDF) içindeki temel string'leri ve metadata bilgilerini analiz eder.

## Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda kurmak ve çalıştırmak için aşağıdaki adımları takip edin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git](https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git)
    cd OSINT-TERSINE-MUHENDISLIK
    ```
    *(Yukarıdaki `https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git` linkini **kendi GitHub reponuzun doğru ve güncel HTTPS linkiyle değiştirmeyi unutmayın.)***

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    python src/main.py
    ```

## Kullanım

Uygulamayı başlattıktan sonra, terminalde karşınıza aşağıdaki gibi bir menü gelecektir. Buradan OSINT veya Tersine Mühendislik araçlarını seçerek ilgili fonksiyonları kullanabilirsiniz.git clone https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git
# OSINT ve Tersine Mühendislik Aracı

---

Bu proje, **OSINT (Açık Kaynak İstihbaratı)** ve **tersine mühendislik** tekniklerini bir araya getirerek dijital ayak izlerini analiz etmeye yönelik geliştirilmiş basit bir araçtır. Amacımız, herkese açık kaynaklardan akıllıca veri toplamak, bu verilerden anlamlı bağlantılar kurmak ve potansiyel güvenlik açıklarını ortaya çıkarmaktır.

## Özellikler

Uygulama, menü tabanlı bir arayüz aracılığıyla aşağıdaki temel özellikleri sunmaktadır:

* **Sosyal Medya Analizi:** Kamuoyuna açık sosyal medya hesaplarından veri toplama veya ilgili profil linklerini oluşturma yeteneği.
* **Alan Adı & IP Sorgulama:** Hedefin IP ve alan adı (domain) bilgileriyle ilgili detaylı WHOIS ve IP adresi bilgileri sağlar.
* **Veri İhlali Kontrolü:** Belirtilen e-posta adresleri veya kullanıcı adlarının geçmişte veri sızıntılarına uğrayıp uğramadığını kontrol etmek için harici kaynaklara yönlendirme yapar.
* **Tersine Mühendislik:** Dijital dosyaların (resim, PDF) içindeki temel string'leri ve metadata bilgilerini analiz eder.

## Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda kurmak ve çalıştırmak için aşağıdaki adımları takip edin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git](https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git)
    cd OSINT-TERSINE-MUHENDISLIK
    ```
    *(Yukarıdaki `https://github.com/Emirjdmhan/OSINT-TERSINE-MUHENDISLIK.git` linkini **kendi GitHub reponuzun doğru ve güncel HTTPS linkiyle değiştirmeyi unutmayın.)***

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    python src/main.py
    ```

## Kullanım

Uygulamayı başlattıktan sonra, terminalde karşınıza aşağıdaki gibi bir menü gelecektir. Buradan OSINT veya Tersine Mühendislik araçlarını seçerek ilgili fonksiyonları kullanabilirsiniz.
## Ekip

* **Emirhan Akdoğan** (222019042) – Geliştirici & Proje Yöneticisi
* **Ahmet Can Kılıçarslan** (2320191002) – Geliştirici & Proje Yöneticisi

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:

1.  Bu repoyu fork'layın.
2.  Yeni bir dal (branch) oluşturun (`git checkout -b feature/yeni-ozellik` veya `git checkout -b bugfix/hata-duzeltmesi`).
3.  Değişikliklerinizi yapın ve commit'leyin (mesajınız açık ve net olsun).
4.  Fork'unuza push'layın (`git push origin feature/yeni-ozellik`).
5.  GitHub üzerinden bir Pull Request açın.

Kodlama standartlarımız için `CONTRIBUTING.md` dosyasına bakabilirsiniz.

## Lisans

Bu proje **MIT Lisansı** ile yayınlanmıştır. Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz. 🚀

## Teşekkürler

* **Keyvan Arasteh:** Rehberlik ve proje şablonu desteği için.
* **Açık Kaynak Kütüphaneler:** `requests`, `BeautifulSoup4`, `python-whois`, `dnspython`, `Pillow`, `pypdf`, `python-docx` ve daha fazlası.
* **OSINT ve Tersine Mühendislik Topluluğu:** İlham verici içerikleri ve araçlarıyla.

## İletişim

Her türlü öneri, katkı veya geri bildirim için çekinmeden bize ulaşabilirsiniz:

* **Emirhan Akdoğan:** akdoganetsemirhan@gmail.com
* **Ahmet Can Kılıçarslan:** kilicarslanahmet59@gmail.com

--
