# src/main.py
from osint_tools import get_whois_info, get_ip_address, generate_social_media_links, check_data_breach
from reverse_eng_tools import analyze_image_metadata, analyze_pdf_metadata, extract_strings_from_file
import os

def main():
    print("------------------------------------------")
    print("  OSINT ve Tersine Mühendislik Analiz Aracı")
    print("------------------------------------------")

    while True:
        print("\nLütfen bir seçenek seçin:")
        print("1. OSINT Araçları")
        print("2. Tersine Mühendislik Araçları")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == '1':
            print("\n--- OSINT Araçları ---")
            osint_choice = input("1. Alan Adı/IP Sorgulama\n2. Sosyal Medya Linkleri Oluşturma\n3. Veri İhlali Kontrolü (Harici Link)\nSeçiminiz: ")
            if osint_choice == '1':
                domain = input("Analiz edilecek alan adını girin (örn: example.com): ")
                print(f"\n--- WHOIS Bilgisi ---\n{get_whois_info(domain)}")
                print(f"\n--- IP Adresi ---\n{get_ip_address(domain)}")
            elif osint_choice == '2':
                username = input("Sosyal medya linkleri için kullanıcı adını girin: ")
                links = generate_social_media_links(username)
                print("\n--- Sosyal Medya Linkleri ---")
                for platform, link in links.items():
                    print(f"{platform}: {link}")
            elif osint_choice == '3':
                email_or_username = input("Kontrol edilecek e-posta veya kullanıcı adını girin: ")
                print(f"\n--- Veri İhlali Kontrolü ---")
                print(check_data_breach(email_or_username))
            else:
                print("Geçersiz seçim.")

        elif choice == '2':
            print("\n--- Tersine Mühendislik Araçları ---")
            re_choice = input("1. Dosya Metadata Analizi (Resim/PDF)\n2. Dosyadan String Çıkarma\nSeçiminiz: ")
            if re_choice == '1':
                file_path = input("Analiz edilecek dosyanın tam yolunu girin (örn: C:\\Users\\KullaniciAdiniz\\Desktop\\resim.jpg veya /home/kullanici/belge.pdf): ")
                if not os.path.exists(file_path):
                    print("Dosya bulunamadı. Lütfen dosya yolunu doğru girdiğinizden emin olun.")
                    continue
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.tiff', '.bmp')):
                    print(f"\n--- Resim Metadata ---\n{analyze_image_metadata(file_path)}")
                elif file_path.lower().endswith('.pdf'):
                    print(f"\n--- PDF Metadata ---\n{analyze_pdf_metadata(file_path)}")
                else:
                    print("Desteklenmeyen dosya formatı. Sadece resim (jpg, png vb.) ve PDF desteklenmektedir.")
            elif re_choice == '2':
                file_path = input("Stringleri çıkarılacak dosyanın tam yolunu girin: ")
                if not os.path.exists(file_path):
                    print("Dosya bulunamadı. Lütfen dosya yolunu doğru girdiğinizden emin olun.")
                    continue
                strings = extract_strings_from_file(file_path)
                print(f"\n--- Dosyadan Çıkarılan Stringler ({file_path}) ---")
                if strings:
                    for s in strings:
                        print(s)
                else:
                    print("Dosyadan string çıkarılamadı veya dosya boş.")
            else:
                print("Geçersiz seçim.")

        elif choice == '3':
            print("Programdan çıkılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()