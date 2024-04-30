from ast import While
from tkinter import *
from tkinter import messagebox
from time import *
import pickle
from os import path, remove
from random import *
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import punctuation, ascii_lowercase, ascii_uppercase, digits

def salvesta_kasutajad_faili(kasutajad, paroolid, failinimi="kasutajad.txt"):
    """
    Salvestab kasutajate andmed tekstifaili.
    :param kasutajad: Kasutajate nimede järjend.
    :param paroolid: Paroolide järjend, kus iga parool vastab sama indeksiga kasutajale.
    :param failinimi: Faili nimi, kuhu andmed salvestatakse (vaikimisi "kasutajad.txt").
    """
    with open(failinimi, "w") as f:
        for i in range(len(kasutajad)):
            f.write(f"{kasutajad[i]}:{paroolid[i]}\n")
    print(f"Kasutajad on edukalt salvestatud faili '{failinimi}'.")

from string import punctuation, ascii_lowercase, ascii_uppercase, digits

def registreerimine(kasutajad, paroolid, nimi_entry, parool_entry):
    nimi = nimi_entry.get()
    parool = parool_entry.get()
    
    if len(parool) == 0:
        messagebox.showwarning("Tühi parool", "Palun sisestage parool.")
        return

    if nimi not in kasutajad:
        if len(parool) >= 8:
            flag_p = False
            flag_l = False
            flag_u = False
            flag_d = False
            parool_list = list(parool)
            for p in parool_list:
                if p in punctuation:
                    flag_p = True
                elif p in ascii_lowercase:
                    flag_l = True
                elif p in ascii_uppercase:
                    flag_u = True
                elif p in digits:
                    flag_d = True
            print("Flags:", flag_p, flag_l, flag_u, flag_d)  # Отладочное сообщение
            if flag_p and flag_u and flag_l and flag_d:
                kasutajad.append(nimi)
                paroolid.append(parool)
                salvesta_kasutajad_faili(kasutajad, paroolid)
                messagebox.showinfo("Registreerimine õnnestus", "Registreerimine õnnestus!")
            else:
                messagebox.showwarning("Nõrk salasõna", "Nõrk salasõna! Salasõna peab sisaldama vähemalt 8 tähemärki, sh suur- ja väiketähti ning numbreid.")
        else:
            messagebox.showwarning("Nõrk salasõna", "Nõrk salasõna! Salasõna peab sisaldama vähemalt 8 tähemärki, sh suur- ja väiketähti ning numbreid.")
    else:
        messagebox.showwarning("Kasutaja juba olemas", "Selline kasutaja on juba olemas!")

def autoriseerimine():
    global kasutajad, paroolid, nimi_entry, parool_entry
    nimi = nimi_entry.get()
    parool = parool_entry.get()
    if nimi in kasutajad and parool == paroolid[kasutajad.index(nimi)]:
        messagebox.showinfo("Tere tulemast", f"Tere tulemast, {nimi}!")
    else:
        messagebox.showwarning("Vale nimi või parool", "Vale nimi või parool!")

    nimi_entry.delete(0, END)
    parool_entry.delete(0, END)


root = Tk()
root.geometry("600x420")
root.title("Registreerimine")
root.configure(bg="#b3e0ff")
root.iconbitmap("task581.ico")
 
kasutajad = []
paroolid = []

nimi_label = Label(root, text="Kasutajanimi:", bg="#ffffff")
nimi_label.pack()
nimi_entry = Entry(root)
nimi_entry.pack()

parool_label = Label(root, text="Parool:", bg="#ffffff")
parool_label.pack()
parool_entry = Entry(root, show="*")
parool_entry.pack()

registreeri_button = Button(root, text="Registreeri", bg="#ffffff", fg="#4d4dff", font="Betoni_MT_Black 12", width=16, command=lambda: registreerimine(kasutajad, paroolid, nimi_entry, parool_entry))
registreeri_button.pack()


root = Tk()
root.geometry("600x500")
root.title("Autoriseerimine ja parooli muutmine")
root.configure(bg="#b3e0ff")
root.iconbitmap("task581.ico")

nimi_label = Label(root, text="Kasutajanimi:", bg="#ffffff")
nimi_label.grid(row=0, column=0, padx=5, pady=5)
nimi_entry = Entry(root)
nimi_entry.grid(row=0, column=1, padx=5, pady=5)

parool_label = Label(root, text="Parool:", bg="#ffffff")
parool_label.grid(row=1, column=0, padx=5, pady=5)
parool_entry = Entry(root, show="*")
parool_entry.grid(row=1, column=1, padx=5, pady=5)

autoriseeri_button = Button(root, text="Autoriseeri", bg="#ffffff", fg="#4d4dff", font="Betoni_MT_Black 12", width=16, command=autoriseerimine)
autoriseeri_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def parooli_muutmine(parooli_muutmine_uus_parool_entry):
    global kasutajad, paroolid, nimi_entry
    nimi = nimi_entry.get()
    vana_parool = parooli_muutmine_vana_parool_entry.get()
    uus_parool = parooli_muutmine_uus_parool_entry.get()
    if nimi in kasutajad:
        indeks = kasutajad.index(nimi)
        if paroolid[indeks] == vana_parool:
            paroolid[indeks] = uus_parool
            messagebox.showinfo("Parooli muutmine", "Parooli muutmine õnnestus!")
        else:
            messagebox.showwarning("Vale vana parool", "Sisestatud vana parool ei ole õige!")
    else:
        messagebox.showwarning("Kasutajat pole", "Sellist kasutajat pole!")

    parooli_muutmine_vana_parool_entry.delete(0, END)
    parooli_muutmine_uus_parool_entry.delete(0, END)


parooli_muutmine_label = Label(root, text="Parooli muutmine", bg="#ffffff")
parooli_muutmine_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

parooli_muutmine_vana_parool_label = Label(root, text="Vana parool:", bg="#ffffff")
parooli_muutmine_vana_parool_label.grid(row=4, column=0, padx=5, pady=5)
parooli_muutmine_vana_parool_entry = Entry(root, show="*")
parooli_muutmine_vana_parool_entry.grid(row=4, column=1, padx=5, pady=5)

parooli_muutmine_uus_parool_label = Label(root, text="Uus parool:", bg="#ffffff")
parooli_muutmine_uus_parool_label.grid(row=5, column=0, padx=5, pady=5)
parooli_muutmine_uus_parool_entry = Entry(root, show="*")
parooli_muutmine_uus_parool_entry.grid(row=5, column=1, padx=5, pady=5)

parooli_muutmine_button = Button(root, text="Muuda parool", bg="#ffffff", fg="#4d4dff", font="Betoni_MT_Black 12", width=16, command=parooli_muutmine)
parooli_muutmine_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    n=int(input("Mitu: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'a',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'w')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
       remove(failinimi)
       print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
def loe_ankeet(fail:str)->any:
    """
    """
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    for line in fail:
        n=line.find(":")  #разделить
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    fail.close()
    return kus,vas

