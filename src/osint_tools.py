# src/osint_tools.py
import whois
import socket

def get_whois_info(domain):
    """Belirtilen alan adının WHOIS bilgilerini çeker."""
    try:
        w = whois.whois(domain)
        return w.text # Tüm whois bilgisini metin olarak döndür
    except Exception as e:
        return f"WHOIS bilgisi çekilemedi: {e}"

def get_ip_address(domain):
    """Belirtilen alan adının IP adresini çeker."""
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"IP adresi çekilemedi: {e}"

def generate_social_media_links(username):
    """Belirtilen kullanıcı adı için popüler sosyal medya linklerini döndürür."""
    links = {
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Facebook": f"https://www.facebook.com/public/{username}", # Genel arama
    }
    return links

def check_data_breach(email_or_username):
    """Veri ihlali kontrolü için Have I Been Pwned linki döndürür."""
    return f"Veri ihlali kontrolü için lütfen şu adresi ziyaret edin: https://haveibeenpwned.com/account/{email_or_username}"