from datetime import time
from random import random

import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import sqlite3

baglanti =sqlite3.connect("kullanicilar.db")
islem =baglanti.cursor()
baglanti.commit()

table =islem.execute("create table if not exists kullanicilar(kullanici text,sifre text,e_posta text ,telefon int)")
baglanti.commit()

def veri_ekle(kullanici,sifre,e_posta,telefon):
    kayit="insert into kullanicilar values (?,?,?,?)"
    islem.execute(kayit,(kullanici,sifre,e_posta,telefon))
    baglanti.commit()


kayit_ol_penceresi=ctk.CTk()
kayit_ol_penceresi.title('Login')
kayit_ol_penceresi.geometry('925x500+300+200')
kayit_ol_penceresi.configure(bg="#fff")
kayit_ol_penceresi.resizable(False,False)



def geri_don():

    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)

    img = PhotoImage(file='giris1.png').subsample(4, 4)
    Label(root, image=img, bg='white').place(x=80, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    ##İlk Frame aslında bir widget sınıfıdır.,İkinci Frame ise daha önce oluşturulmuş bir nesne olabilir.

    heading = Label(frame, text='Giriş Yap', fg='#57a1f8', bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ##############----------

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ###################-----------------

    password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), show="*")
    password.place(x=30, y=150)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ############

    def giris_yap():

        kullanici_adi = user.get()
        sifre = password.get()

        if kullanici_adi == "" or sifre == "":
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş bırakılamaz!")
            return

        with sqlite3.connect("kullanicilar.db") as db:
            cursor = db.cursor()
            # Kullanıcı bilgilerini sorgula
            cursor.execute("SELECT * FROM kullanicilar WHERE kullanici = ? AND sifre = ?", (kullanici_adi, sifre))
            sonuc = cursor.fetchone()

        if sonuc:
            messagebox.showinfo("Başarılı", f"Hoş geldiniz, {kullanici_adi}!")
            anasayfa()


        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

    Button(frame, width=39, pady=7, text='Giriş Yap ', command=giris_yap, cursor='hand2', bg='#57a1f8', fg='white',
           border=2).place(x=35, y=204)
    label = Label(frame, text="Hesabınız yok mu ?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    def sign_up():

        kayit_ol_penceresi = ctk.CTk()
        kayit_ol_penceresi.title('Login')
        kayit_ol_penceresi.geometry('925x500+300+200')
        kayit_ol_penceresi.configure(bg="#fff")
        kayit_ol_penceresi.resizable(False, False)

        def geri_don():
            root = Toplevel()
            root.title('Login')
            root.geometry('925x500+300+200')
            root.configure(bg="#fff")
            root.resizable(False, False)

            img = PhotoImage(file='giris1.png').subsample(4, 4)
            Label(root, image=img, bg='white').place(x=80, y=50)

            frame = Frame(root, width=350, height=350, bg="white")
            frame.place(x=480, y=70)

            ##İlk Frame aslında bir widget sınıfıdır.,İkinci Frame ise daha önce oluşturulmuş bir nesne olabilir.

            heading = Label(frame, text='Giriş Yap', fg='#57a1f8', bg="white",
                            font=('Microsoft YaHei UI Light', 23, 'bold'))
            heading.place(x=100, y=5)

            ##############----------

            user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
            user.place(x=30, y=80)
            user.insert(0, 'Kullanıcı Adı')

            Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

            ###################------------------

            password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11),
                             show="*")
            password.place(x=30, y=150)
            password.insert(0, 'Şifre')

            Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

            ############

            Button(frame, width=39, pady=7, text='Giriş Yap ', cursor='hand2', bg='#57a1f8', fg='white',
                   border=2).place(
                x=35,
                y=204)
            label = Label(frame, text="Hesabınız yok mu ?", fg='black', bg='white',
                          font=('Microsoft YaHei UI Light', 9))
            label.place(x=75, y=270)

            sign_up = Button(frame, width=6, text="Kayıt Ol", command='kayıt_ol', border=2, bg='white', cursor='hand2',
                             fg='#57a1f8')
            sign_up.place(x=215, y=270)

            sign_in = mainloop()



    def anasayfa():

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        root = ctk.CTk()
        root.geometry("850x750")
        root.title("Restoran Adisyon Sistemi")

        ust_cerceve = ctk.CTkFrame(root, height=50, corner_radius=10)
        ust_cerceve.pack(side="top", fill="x", pady=10)

        alt_cerceve = ctk.CTkFrame(root, height=50, corner_radius=10)
        alt_cerceve.pack(side="bottom", fill="x", pady=10)

        sol_cerceve = ctk.CTkFrame(root, width=600, height=700, corner_radius=10)
        sol_cerceve.pack(side="left", fill="y", padx=60, pady=0)

        sag_cerceve = ctk.CTkFrame(root, width=400, corner_radius=10)
        sag_cerceve.pack(side="right", fill="y", padx=10, pady=0)

        hesap_makinesi_cerceve = ctk.CTkFrame(sag_cerceve, corner_radius=10)
        hesap_makinesi_cerceve.pack(fill="x", pady=10)

        sol_ust = ctk.CTkFrame(sol_cerceve, corner_radius=10)
        sol_ust.pack(fill="x", pady=5)

        sol_alt = ctk.CTkFrame(sol_cerceve, corner_radius=10)
        sol_alt.pack(fill="x", pady=5)

        fis_no = ctk.StringVar()
        tavuk_burger = ctk.StringVar(value="0")
        dana_burger = ctk.StringVar(value="0")
        patates_kizartmasi = ctk.StringVar(value="0")
        soft_icecek = ctk.StringVar(value="0")

        tarih = ctk.StringVar(value=time.strftime("%d/%m/%Y"))
        ara_toplam = ctk.StringVar(value="0")
        kdv = ctk.StringVar(value="0")
        toplam_fiyat = ctk.StringVar(value="0")
        hesap_giris = ctk.StringVar(value="")

        def hesapla():
            try:
                tavuk_fiyat = 160 * int(tavuk_burger.get())
                dana_fiyat = 180 * int(dana_burger.get())
                patates_fiyat = 80 * int(patates_kizartmasi.get())
                icecek_fiyat = 20 * int(soft_icecek.get())

                ara = tavuk_fiyat + dana_fiyat + patates_fiyat + icecek_fiyat
                kdv_oran = int(kdv.get())
                toplam = ara + (ara * kdv_oran / 100)

                ara_toplam.set(f"{ara} TL")
                toplam_fiyat.set(f"{toplam:.2f} TL")
            except ValueError:
                messagebox.showerror("Hata", "Lütfen geçerli sayılar giriniz!")

        def temizle():
            fis_no.set("")
            tavuk_burger.set("0")
            dana_burger.set("0")
            patates_kizartmasi.set("0")
            soft_icecek.set("0")
            ara_toplam.set("0")
            toplam_fiyat.set("0")

        def cikis():
            if messagebox.askyesno("Çıkış", "Çıkmak istediğinizden emin misiniz?"):
                root.destroy()

        def referans_no_uret():
            fis_no.set(f"FIS{random.randint(10000, 99999)}")

        def hesap_makinesi_buton_tikla(deger):
            if deger == "C":
                hesap_giris.set("")
            elif deger == "=":
                try:
                    sonuc = eval(hesap_giris.get())
                    hesap_giris.set(str(sonuc))
                except Exception as e:
                    hesap_giris.set("Hata")
            else:
                hesap_giris.set(hesap_giris.get() + str(deger))

        baslik = ctk.CTkLabel(ust_cerceve, text="Restoran Adisyon Sistemi", font=("Arial", 24, "bold"))
        baslik.pack()

        alt_bilgi = ctk.CTkLabel(alt_cerceve, text="Kolay Gelsin", font=("Arial", 12, "italic"))
        alt_bilgi.pack()

        ctk.CTkLabel(sol_ust, text="Sipariş Bilgileri", font=("Arial", 18, "bold"), anchor="w").pack(fill="x")

        inputs = [
            ("Fis No:", fis_no),
            ("Tavuk Burger (Adet):", tavuk_burger),
            ("Dana Burger (Adet):", dana_burger),
            ("Patates Kızartması (Adet):", patates_kizartmasi),
            ("Soft İçecek (Adet):", soft_icecek)
        ]

        for i, (text, variable) in enumerate(inputs):
            ctk.CTkLabel(sol_ust, text=text).pack(anchor="w", padx=5)
            ctk.CTkEntry(sol_ust, textvariable=variable).pack(fill="x", padx=5, pady=2)

        ctk.CTkLabel(sol_alt, text="Ödeme Bilgileri", font=("Arial", 18, "bold"), anchor="w").pack(fill="x")

        odeme_bilgileri = [
            ("Tarih:", tarih),
            ("Ara Toplam:", ara_toplam),
            ("KDV (%):", kdv),
            ("Toplam Fiyat:", toplam_fiyat)
        ]

        for text, variable in odeme_bilgileri:
            ctk.CTkLabel(sol_alt, text=text).pack(anchor="w", padx=5)
            ctk.CTkEntry(sol_alt, textvariable=variable).pack(fill="x", padx=5, pady=2)

        ctk.CTkButton(sag_cerceve, text="Hesapla", command=hesapla).pack(fill="x", pady=5)
        ctk.CTkButton(sag_cerceve, text="Referans No Üret", command=referans_no_uret).pack(fill="x", pady=5)
        ctk.CTkButton(sag_cerceve, text="Temizle", command=temizle).pack(fill="x", pady=5)
        ctk.CTkButton(sag_cerceve, text="Çıkış", command=cikis).pack(fill="x", pady=5)

        ctk.CTkLabel(hesap_makinesi_cerceve, text="Hesap Makinesi", font=("Arial", 18, "bold"), anchor="w").pack(
            fill="x")

        hesap_giris_ekrani = ctk.CTkEntry(hesap_makinesi_cerceve, textvariable=hesap_giris, justify="right",
                                          font=("Arial", 14))
        hesap_giris_ekrani.pack(fill="x", pady=5)

        def hesap_makinesi_tuslari():
            tuslar = [
                ["7", "8", "9", "/"],
                ["4", "5", "6", "*"],
                ["1", "2", "3", "-"],
                ["C", "0", "=", "+"]
            ]
            for satir in tuslar:
                cerceve = ctk.CTkFrame(hesap_makinesi_cerceve)
                cerceve.pack(fill="x")
                for tus in satir:
                    ctk.CTkButton(cerceve, text=tus, command=lambda t=tus: hesap_makinesi_buton_tikla(t)).pack(
                        side="left",
                        expand=True,
                        fill="x",
                        padx=2,
                        pady=2)

        hesap_makinesi_tuslari()

        root.mainloop()

    root.mainloop()




def kayit_ol():
    ad_soyad = entry_ad_soyad.get()
    sifre = entry_sifre.get()
    eposta = entry_eposta.get()
    telefon = entry_telefon.get()


    if not ad_soyad or not eposta or not telefon or not sifre:
        messagebox.showerror("Hata", "Tüm alanları doldurmanız gerekmektedir!")
        return
    veri_ekle(entry_ad_soyad.get(), entry_sifre.get(),entry_eposta.get(), entry_telefon.get())

    baglanti.close()


    messagebox.showinfo("Başarılı", "Kayıt başarıyla tamamlandı!")
    #kayit_ol_penceresi.destroy()  # Kayıt Ol penceresini kapat
    kayit_ol_penceresi.deiconify()  # Ana pencereyi tekrar göster


frame = ctk.CTkFrame(kayit_ol_penceresi, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="Kayıt Ol", font=("Arial", 26))
label.pack(pady=10)


entry_ad_soyad = ctk.CTkEntry(frame, placeholder_text="Ad Soyad", width=300)
entry_ad_soyad.pack(pady=10)


entry_eposta = ctk.CTkEntry(frame, placeholder_text="E-Posta", width=300)
entry_eposta.pack(pady=10)


entry_telefon = ctk.CTkEntry(frame, placeholder_text="Telefon", width=300)
entry_telefon.pack(pady=10)


entry_sifre = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*", width=300)
entry_sifre.pack(pady=10)


button = ctk.CTkButton(frame, text="Kayıt Ol", command=kayit_ol, corner_radius=10, width=200)
button.pack(pady=20)


geri_don_button = ctk.CTkButton(frame, text="Geri Dön", command=geri_don,corner_radius=10,fg_color="red", width=200)
geri_don_button.pack(pady=10)



kayit_ol_penceresi.mainloop()
