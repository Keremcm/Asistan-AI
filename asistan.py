import requests
from urllib.parse import urljoin
from tkinter import filedialog

def asistan(text):
    try:
        
        # İlk olarak, asistanai.pythonanywhere.com adresine istek gönderip dinamik URL'yi alıyoruz
        main_site_url = "https://asistanai.pythonanywhere.com"
        response = requests.get(main_site_url)
        dynamic_url = response.url

        # Chatbot ile etkileşim kurma işlemi için URL'yi belirliyoruz
        chatbot_url = urljoin(dynamic_url, "/api/message")  # Chatbot endpoint'inin tam URL'si
        print("Yanıt işleniyor...")

        # Kullanıcıdan alınacak metni belirleyelim
        text_input = f"{text}"
        
        # Chatbot ile etkileşim kurma isteği
        chat_response = requests.post(chatbot_url, json={"message": text_input})

        if chat_response.status_code == 200:
            bot_response = chat_response.json().get("response")
            print(bot_response)
        else:
            print("Üzgünüm, geçici olarak yapay zeka özelliklerine erişilemiyor.")

    except Exception as e:
        print("Üzgünüm bir sorun oluştu.")
        
def asistan_vision(text, img_path):
    """Görsel ve metin ile asistan API'sine istek gönderir ve yanıtı alır."""
    try:
         # İlk olarak, asistanai.pythonanywhere.com adresine istek gönderip dinamik URL'yi alıyoruz
        main_site_url = "https://asistanai.pythonanywhere.com"
        response = requests.get(main_site_url)
        dynamic_url = response.url
        vision_url = urljoin(dynamic_url, '/api/vision')  # Vision endpoint'inin tam URL'si

        def send_request(image_path, user_input):
            """Görsel ve kullanıcı metni ile POST isteği gönderir."""
            with open(image_path, 'rb') as img_file:
                response = requests.post(
                    vision_url, 
                    files={'file': img_file}, 
                    data={'user_input': user_input}
                )
                
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    print(f"Asistan Yanıtı: {response_data.get('response')}")
                    if 'image' in response_data:
                        print(f"Görsel URL: {response_data['image']}")
                except ValueError:
                    print("Yanıt JSON formatında değil.")
            else:
                print(f"İstek başarısız oldu. HTTP Durum Kodu: {response.status_code}")

        # Görsel ve kullanıcı metni ile isteği gönder
        user_input = f"{text}. Yanıt kısa olsun."
        send_request(img_path, user_input)
    
    except Exception as e:
        print(f"Bir sorun oluştu: {e}")

def main():
    try:
        while True:
            client = input("Mesajınızı giriniz: ")
            if "görsel" in client.lower():
                print("Lütfen görseli seçiniz...")
                img_path = filedialog.askopenfilename()
                client = input("Görsel için mesajınızı giriniz: ")
                asistan_vision(client, img_path)
            else:
                asistan(client)
    except Exception as e:
        print(f"Hata: {str(e)}")

main()
