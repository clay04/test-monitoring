import time
from bruteforce_detector import detect_bruteforce_attempts
from gemini_analyzer import analyze_log_with_gemini
from whatsapp_notifier import send_whatsapp_notification
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

def main():
    log_data = detect_bruteforce_attempts()
    if log_data:
        print("Brute-force attempt detected!")
        analysis = analyze_log_with_gemini(log_data)
        send_whatsapp_notification(analysis)
    else:
        print("No brute-force attempts detected.")

if __name__ == "__main__":
    main()
    #send_whatsapp_notification("🚀 Tes manual: Jika ini muncul, artinya pengiriman berhasil.")
    
