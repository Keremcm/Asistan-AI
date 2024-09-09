# Asistan-AI

Bu proje, Python ile geliştirilmiş bir GPT-Turbo model yapay zeka destekli asistan API'sidir. Asistan, komutları anlayabilir, çeşitli bilgileri sağlayabilir ve sizinle etkileşime geçebilir.

## Özellikler

- **Yazılı Komutlar:** Yazılı komutları anlayabilir ve cevap verebilir.
- **Bilgi Sağlama:** Belirli konular hakkında bilgi verebilir.
- **Eğlenceli Konuşmalar:** Eğlenceli sohbetler ve etkileşimler sunar.
- **Görsel Algılama:** Komutu gönderilen görsel ile düşünerek cevap verebilir.

## Kurulum

1. **Gereksinimler**

   Asistan'ın istemcisini çalıştırmak için Python 3.11 ve gerekli paketler gereklidir. Aşağıdaki komutu kullanarak gerekli paketleri yükleyebilirsiniz:

   ```bash
   pip install -r requirements.txt
   ```
2. **Python Dosyası**

   Asistan ile etkileşimde bulunmak için gerekli kodlar "asistan.py" dosyasında verilmiştir. İlk başta "asistan.py" dosyasını indirin.
   ```bash
   python asistan.py
   ```
   Komutu ile Asistan için python API'sini çalıştırarak, yapay zekam ile etkileşime geçebilirsiniz.

## Kullanım

1. **Yazılı Mesaj**
   
  Python dosyasını çalıştırdıktan sonra "Mesajınızı girin: " ifadesine sormak veya söylemek istediğiniz ifadeyi yazınız.
  İstemci kodu kullanıcı girişi aldığı metni Asistan'a iletir ve aldığı cevabı kullanıcıya geri ileterek sohbet gerçekleştirir.

2. **Görsel/Yazılı Mesaj**

   Python dosyasını çalıştırdıktan sonra "Mesajınızı girin: " ifadesine "görsel" mesajını yazın ve göndermek istediğiniz görseli açılan pencerede seçin.
   Seçtikten sonra "Görsel ile mesajınızı gönderin: " ifadesine mesajınızı yazıp gönderdiğinizde Asistan sorguyu ve görseli işleyip kullanıcıya uygun bir
   cevap verecektir.
