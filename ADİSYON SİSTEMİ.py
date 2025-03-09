import customtkinter as ctk
import random
import time
from tkinter import messagebox


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("850x750")
root.title("Restoran Adisyon Sistemi")


ust_cerceve = ctk.CTkFrame(root, height=50, corner_radius=10)
ust_cerceve.pack(side="top", fill="x", pady=10)

alt_cerceve = ctk.CTkFrame(root, height=50, corner_radius=10)
alt_cerceve.pack(side="bottom", fill="x", pady=10)

sol_cerceve = ctk.CTkFrame(root, width=600 ,height=700,corner_radius=10)
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
ara_toplam = ctk.StringVar(value="0" )
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


ctk.CTkLabel(hesap_makinesi_cerceve, text="Hesap Makinesi", font=("Arial", 18, "bold"), anchor="w").pack(fill="x")

hesap_giris_ekrani = ctk.CTkEntry(hesap_makinesi_cerceve, textvariable=hesap_giris, justify="right", font=("Arial", 14))
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
            ctk.CTkButton(cerceve, text=tus, command=lambda t=tus: hesap_makinesi_buton_tikla(t)).pack(side="left", expand=True, fill="x", padx=2, pady=2)

hesap_makinesi_tuslari()


root.mainloop()
