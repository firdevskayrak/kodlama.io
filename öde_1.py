# -*- coding: utf-8 -*-
"""öde-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uAekdW81F866MxKPkucsX0dhgRI2P5eH
"""

#Sayılar: Python'da tamsayılar (integer), ondalıklı (float) ve karmaşık sayılar (complex) gibi farklı sayı türleri bulunur.
x = 20          # tamsayı (integer)
y = 20.7        # kayan noktalı sayı (float)
z = 2 - 7j      # karmaşık sayı (complex)

#Metin (string): Python'da metin verileri string olarak adlandırılır. Stringler tek tırnak veya çift tırnak içine alınır.
isim = 'Fİrdevs'
mesaj = "Kodlama.io"

#Boolean: True ve False olmak üzere iki değere sahip olan veri tipidir.
x = True
y = False

#Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.
#List: Elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.
günler = ['pazartesi', 'salı', 'çarşamba','perşembe','cuma','cumartesi','pazar']
#Tuple: Elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.
günler = ('pazartesi', 'salı', 'çarşamba','perşembe','cuma','cumartesi','pazar')
#Set: Elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.
myset = {"elma", "muz", "kiraz"}
#Sözlük (dictionary): Key ve value şeklinde verileri saklayabileceğimiz bir veri yapısıdır
ogrenci = {
  "numara": "102",
  "ad": "Firdevs",
  "soyad": "Kayrak"
}



devam = True
while devam:
    # Kullanıcıdan bir girdi al
    girdi = input("Lütfen bir girdi yapın: ")

    # Bir sonraki sayfaya gitmek isteyip istemediğini sor
    cevap = input("Bir sonraki sayfaya gitmek istiyor musunuz? (E/H)")

    # Kullanıcının cevabına göre bir sonraki sayfaya git veya döngüyü sonlandır
    if cevap.upper() == "E":
        webbrowser.open('http://www.example.com/next_page')
        devam = False
    elif cevap.upper() == "H":
        devam = False