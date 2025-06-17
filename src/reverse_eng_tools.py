# src/reverse_eng_tools.py
from PIL import Image
import PyPDF2
import os

def analyze_image_metadata(file_path):
    """Resim dosyasının EXIF metadata bilgilerini analiz eder."""
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                # Sadece temel, okunabilir bilgileri döndürelim
                readable_exif = {}
                for tag_id, value in exif_data.items():
                    tag_name = Image.TAGS.get(tag_id, tag_id)
                    readable_exif[tag_name] = str(value)
                return readable_exif
            else:
                return "EXIF metadata bulunamadı."
    except Exception as e:
        return f"Resim metadata analizi hatası: {e}"

def analyze_pdf_metadata(file_path):
    """PDF dosyasının metadata bilgilerini analiz eder."""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            info = reader.metadata
            if info:
                return {key: info[key] for key in info}
            else:
                return "PDF metadata bulunamadı."
    except Exception as e:
        return f"PDF metadata analizi hatası: {e}"

def extract_strings_from_file(file_path, min_len=4):
    """Bir dosyadan okunabilir string'leri çıkarır."""
    strings = []
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            current_string = bytearray()
            for byte in content:
                if 32 <= byte <= 126 or byte in [9, 10, 13]: # Okunabilir ASCII, tab, newline, carriage return
                    current_string.append(byte)
                else:
                    if len(current_string) >= min_len:
                        try:
                            strings.append(current_string.decode('utf-8', errors='ignore'))
                        except UnicodeDecodeError:
                            pass
                    current_string = bytearray()
            if len(current_string) >= min_len: # Son kalan string'i de ekle
                try:
                    strings.append(current_string.decode('utf-8', errors='ignore'))
                except UnicodeDecodeError:
                    pass
    except Exception as e:
        return [f"Dosya string analizi hatası: {e}"]
    return strings