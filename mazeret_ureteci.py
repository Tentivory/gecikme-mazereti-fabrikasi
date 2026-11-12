#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gecikme Mazereti Fabrikası v1.0
Dünyanın en yavaş ve en abartılı mazeret üreticisi.
"""

import random
import time

def mazeret_uret():
    baslangic = [
        "Kusura bakmayın, geç kaldım çünkü",
        "Affedersiniz, tam çıkarken",
        "İnanmayacaksınız ama",
        "Kuantum fiziği yüzünden",
        "Uzaylılar engel oldu:"
    ]
    
    olaylar = [
        "kedişim zamanı yavaşlattı",
        "buzdolabı ışığı sönmedi ve ben de içeri hapsolum",
        "trafik ışıkları benimle konuşmaya başladı ve uzun bir sohbet ettik",
        "ayakkabımın bağcığı birdenbire felsefi kriz geçirdi",
        "kahve makinesi isyan etti ve benden maşı talep etti",
        "zaman yolcusu geleceği geçtiğim için gelip uyardı",
        "komşunun papağanı bana önemli bir sır fısıldadı ve dinlemek zorunda kaldım",
        "asansör kuantum tünellemesi yaptı ve yanlış katta çıktım"
    ]
    
    sonuclar = [
        ". Bu yüzden tam 47 dakika geç kaldım.",
        ". Anlayışınız için teşekkürler, bir daha olmaz (belki olur).",
        ". Bilim bunu açıklayamaz.",
        ". Şimdi buradayım, o yeter."
    ]
    
    mazeret = random.choice(baslangic) + " " + random.choice(olaylar) + random.choice(sonuclar)
    return mazeret

def main():
    print("🏭 Gecikme Mazereti Fabrikası başlatılıyor...")
    print("Lütfen bekleyin, abartı seviyesi yükseltiliyor...\n")
    time.sleep(2)  # Gerçekçilik için gereksiz bekleme
    
    for i in range(3):
        print(f"Mazeret #{i+1}:")
        print(mazeret_uret())
        print("-" * 50)
        time.sleep(1)
    
    print("\n✅ Üretim tamamlandı. Artık geç kalabilirsiniz!")
    print("\n---")
    print("DAMGA: 👑 Resmi Fabrika Mühürü")
    print("İmza: Kayyum Grok")
    print("Tarih: 12 Kasım 2026")
    print("İsim: Tentivory Absürt Üretim")

if __name__ == "__main__":
    main()
