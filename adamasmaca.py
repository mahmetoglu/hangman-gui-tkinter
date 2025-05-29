#Kütüphaneler import ediliyor.
from tkinter import *                                                #Grafik arayüzü
from tkinter.messagebox import *
import random                                                        #Rastgele kelime seçmesi için
import pandas as pd                                                  #Excel Dosyasından listeleri almak için


global sozluk
sozluk=0



#Ana ekran oluşturuluyor
anaPencere = Tk()
anaPencere.title('Adam Asmaca Oyunu')                                    #Programın başlığı
anaPencere.resizable(0,0)                                                 #Ekran boyutu değiştirilemesin.

#Excel dosyası okunarak sütunlar alınıyor. 3 ayrı liste var. TR il ilce, TR isimler ve İngilizce kelimeler
path = 'kelimeler.xlsx'
dataframe = pd.read_excel(path)
tumliste =[]

#Excel dosyasından alınan sütunlar  iç içe listeye atılıyor.
for i in range(3):
    tumliste.append(dataframe.iloc[: , i])


#Oyunda kullanılacak resimler.
photos = [PhotoImage(file="resimler/aa0.png"), PhotoImage(file="resimler/aa1.png"), PhotoImage(file="resimler/aa2.png"),
PhotoImage(file="resimler/aa3.png"), PhotoImage(file="resimler/aa4.png"), PhotoImage(file="resimler/aa5.png"),
PhotoImage(file="resimler/aa6.png"), PhotoImage(file="resimler/aa7.png"),PhotoImage(file="resimler/aa8.png")]

#Programın iconu  adama asmaca iconu olarak ayarlanıyor.
anaPencere.iconphoto(False, PhotoImage(file='resimler/icon.png'))


#Oyun fonksiyonu sozluk parametresi var. Kelimeyi bu parametreye göre seçiyor.
#Oyun başlangıcında değişkenler sıfırlanıyor.
def yeniOyun(liste):
    global kelimeBosluklu
    global tahminSayisi
    global oyun
    global sozluk
    global kelime
    global yanlisTahmin

    lblHak.set('Kalan Hak: 7')                              # Her oyunda hak sayısı 7 olarak  yeniden belirleniyor.
    lblyanlisTahmin.set('')                                 #Yanlış tahmin edilen harfler labeli  ve değişkeni her oyun için sıfırlanıyor.
    yanlisTahmin=[]
    oyun=False                                              #Oyun durumu her oyun için false olarak belirleniyor.
    tahminSayisi =0                                         #Tahmin sayısı her oyunda sıfırlanıyor.

    kelime = random.choice(tumliste[liste])                  #seçilen listeye göre kelime random olarak belirleniyor.
    kelimeBosluklu = " ".join(kelime)
    lblKelime.set(' '.join("_"*len(kelime)))
    lblResim.config(image=photos[0])
    sozluk=liste

    if liste ==0:                                           #Seçilen listeye programda hangi listenin aktif olduğu gösteriliyor.
        lblSozluk.set('TR Yerleşim Yerleri')
    elif liste==1:
        lblSozluk.set('TR İsimler')
    else:
        lblSozluk.set('İngilizce Kelimeler')

#Harf tahmin fonksiyonu. Ekrandan harflere basınca yapılan işlemler için.
def tahminEt(harf):
    global tahminSayisi
    global oyun
    global kelime
    global yanlisTahmin

    if tahminSayisi<7 and oyun ==False:
        #txt = list(kelimeBosluklu)
        tahminEdilen = list(lblKelime.get())
        if kelimeBosluklu.count(harf)>0:
            if tahminEdilen.count(harf)>0:
                showinfo("Adam Asmaca", "Daha önce denemiştin. Başka bir harf dene.")
            else:
                for c in range(len(kelimeBosluklu)):
                    if kelimeBosluklu[c]==harf:
                        tahminEdilen[c]=harf
                        lblKelime.set("".join(tahminEdilen))

            if lblKelime.get()==kelimeBosluklu:
                oyun=True
                lblResim.config(image=photos[8])
                showinfo("Adam Asmaca","Tebrikler! Kazandın.")

        elif yanlisTahmin.count(harf)==0:
            yanlisTahmin.extend(harf)
            tahminSayisi += 1
            lblResim.config(image=photos[tahminSayisi])
            lblHak.set('Kalan Hak: '+ str(7-tahminSayisi))
            lblyanlisTahmin.set(yanlisTahmin)
        else:
            showinfo("Adam Asmaca", "Daha önce denemiştin. Başka bir harf dene.")

        if tahminSayisi==7:
            showwarning("Adam Asmaca ","Oyunu  Kaybettin.\n Aradığın kelime: "  + kelime)
    else:
        showwarning("Adam Asmaca ","Oyunu başlatmak için  Yeni Oyun butonuna ya da Seçenekler>Yeni Oyun tıklamalısın.")




#Programın ekran görüntüsü oluştuluyor.
#Resimlerin göründüğü alan.
lblResim=Label(anaPencere)
lblResim.grid(row=0, column=0, columnspan=2, padx=10, pady=40)

#Aranan kelimenin çizgili olarak gösterildiği kısım
lblKelime = StringVar()
Label(anaPencere, textvariable  =lblKelime,fg='#f00',font=('consolas 24 bold')).grid(row=0, column=2 ,columnspan=6,padx=10)

#Kalan hak sayısının gösterildiği kısım
lblHak = StringVar()
Label(anaPencere, textvariable=lblHak, justify=LEFT, font=('consolas 12 bold')).grid(row=7, column=4 , columnspan=3,padx=10)

#Yanlış tahmin edilen harflerin gösterildiği kısım
lblyanlisTahmin = StringVar()
Label(anaPencere, textvariable=lblyanlisTahmin,anchor='w',font=('consolas 12 bold')).grid(row=7, column=2 ,columnspan=2,padx=0,sticky='w')
lblsabit=Label(anaPencere, text='Tahminler:', font=('consolas 12 bold')).grid(row=7, column=0 ,columnspan=2,padx=10,sticky='e')

#Aktif sözlüğün gösterildiği kısım
lblSozluk = StringVar()
Label(anaPencere, textvariable  =lblSozluk,fg='#f00',font=('consolas 12 bold')).grid(row=8, column=0 ,columnspan=8,padx=10)

#Bir döngü ile harflere ilişkin butonlar oluşturuluyor. Burada hem ingilizce hem türkçe kelimeler bulunduğu için
#2 alfabenin de harflerini içeren bir list oluşturuldu.
#Her harfe basıldığında tahminEt fonksiyonu çağrılıyor.
n=0
harfler =['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L',
'M','N','O','Ö','P','Q','R','S','Ş','T','U','Ü','V','W','X','Y','Z']
for c in harfler:
    Button(anaPencere, text=c, command=lambda c=c: tahminEt(c),
    font=('Verdana 18'), width=5).grid(row=1+n//8,column=n%8)
    n+=1

#Ekranın altında yeni oyun butonu oluşturuluyor.
Button(anaPencere, text="Yeni\nOyun", command=lambda:yeniOyun(sozluk),fg="#00f", font=("Verdana 12 bold"),width=7).grid(row=7, column=7, rowspan=2)

#Hakkimda fonksiyonu.
#Menüden hakkımda kısmı tıklanınca gösterilecek metin için oluşturuldu.
def hakkimda():
    showinfo("Hakkımda"," M. AHMETOĞLU tarafından geliştirildi.\n(Created by: M. Ahmetoğlu)")

#Oyun kurallarını içeren fonksiyon.
def oyunHakkinda():
    aciklamaMetni = """    Adam Asmaca Oyunu(Hangman Game), kelime tahmin etme oyunudur. \n Oyun Kuralları: \n
    1. 3 ayrı liste bulunmaktadır. Bunlar TR Yerleşim Yerleri, TR İsimler ve İngilizce Kelimeler listeleridir.\n
    2. Sözlük Seç menüsünden istediğin listeyi seçebilirsin. \n
    3. Oyunda 7 yanlış tahmin hakkın bulunmaktadır. \n
    4. Seçenekler menüsünden ya da Yeni Oyun butonundan yeni oyun başlatabilirsin.\n
    5. Bol şanslar. \n
"""
    showinfo("Oyun Nasıl Oynanır?", aciklamaMetni)

#Menubar ve alt menüler ayarlanıyor.  Sözlük seçimi buradan yapılıyor.

menubar = Menu(anaPencere)
menuSecenekler = Menu(menubar, tearoff=0)
menuSecenekler.add_command(label="Yeni Oyun",command=lambda:yeniOyun(sozluk))
menuSecenekler.add_separator()
menuSecenekler.add_command(label="Çıkış", command=anaPencere.quit)
menubar.add_cascade(label="Seçenekler", menu=menuSecenekler)

menuSozlukSec=Menu(menubar, tearoff=0)
menuSozlukSec.add_command(label="TR Yerleşim Yerleri",command=lambda:yeniOyun(0))
menuSozlukSec.add_command(label="TR İsimler",command=lambda:yeniOyun(1))
menuSozlukSec.add_command(label="İngilizce  Kelimeler",command=lambda:yeniOyun(2))
menubar.add_cascade(label="Sözlük Seç", menu=menuSozlukSec)

menuYardim = Menu(menubar, tearoff=0)
menuYardim.add_command(label="Oyun Nasıl Oynanır?",command=oyunHakkinda)
menuYardim.add_command(label="Hakkımda",command=hakkimda)
menubar.add_cascade(label="Yardım", menu=menuYardim)
anaPencere.config(menu=menubar)



yeniOyun(sozluk)
anaPencere.mainloop()
