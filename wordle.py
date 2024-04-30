import tkinter as tk
from tkinter import messagebox, simpledialog
from random import shuffle

class WordleMäng:
    def __init__(self, master):
        self.meister = master
        self.meister.title("Wordle")
        self.meister.configure(bg="lightblue")
        self.meister.geometry("400x650")

        self.sõnad = self.lae_sõnad()
        shuffle(self.sõnad)
        self.praegune_sõna_indeks = 0
        self.sõna = self.sõnad[self.praegune_sõna_indeks]
        self.jäänud_katsed = 6

        self.haldus_raam = tk.Frame(self.meister, bg="lightblue")
        self.haldus_raam.pack(side="top", pady=10)

        self.pealkiri_silt = tk.Label(self.haldus_raam, text="Arva päeva sõna", font=("Helvetica", 16), bg="lightblue")
        self.pealkiri_silt.grid(row=0, column=0, padx=5)

        self.lisa_nupp = tk.Button(self.haldus_raam, text="Lisa Sõna", bg="white", command=self.lisa_sõna)
        self.lisa_nupp.grid(row=0, column=1, padx=5)

        self.eemalda_nupp = tk.Button(self.haldus_raam, text="Eemalda Sõna", bg="white", command=self.eemalda_sõna)
        self.eemalda_nupp.grid(row=0, column=2, padx=5)

        self.ochist_nupp = tk.Button(self.haldus_raam, text="Puhasta Ruudustik", bg="white", command=self.puhasta_ruudustik)
        self.ochist_nupp.grid(row=0, column=3, padx=5)

        self.loo_sõnaruudustik()
        self.loo_tähestikuruudustik()
        self.loo_kinnituse_nupp()
        self.loo_katsete_loendur()

        self.aja_uuendamine()

    def lae_sõnad(self):
        with open("wordle.txt", "r") as fail:
            return [sõna.strip().lower() for sõna in fail.readlines()]

    def salvesta_sõnad(self):
        with open("wordle.txt", "w") as fail:
            for sõna in self.sõnad:
                fail.write(sõna + "\n")

    def lisa_sõna(self):
        sõna = simpledialog.askstring("Lisa Sõna", "Sisesta lisatav sõna:")
        if sõna:
            self.sõnad.append(sõna.lower())
            self.salvesta_sõnad()

    def eemalda_sõna(self):
        if self.sõnad:
            sõna = simpledialog.askstring("Eemalda Sõna", "Sisesta eemaldatav sõna:")
            if sõna.lower() in self.sõnad:
                self.sõnad.remove(sõna.lower())
                self.salvesta_sõnad()
            else:
                messagebox.showwarning("Hoiatus", "Sõna ei leitud loendist!")

    def puhasta_ruudustik(self):
        for rida in self.sõna_kastid:
            for kast in rida:
                kast.delete(0, tk.END)
                kast.config(bg="black", fg="blue")

    def loo_sõnaruudustik(self):
        self.sõna_raam = tk.Frame(self.meister, bg="lightblue")
        self.sõna_raam.pack(side="top", pady=10)

        self.sõna_kastid = []
        for i in range(6):
            rida_kastid = []
            for j in range(5):
                kast = tk.Entry(self.sõna_raam, width=3, font=("Helvetica", 24), state="normal", bg="pink", fg="blue")
                kast.grid(row=i, column=j)
                rida_kastid.append(kast)
            self.sõna_kastid.append(rida_kastid)

    def loo_tähestikuruudustik(self):
        self.tähestiku_raam = tk.Frame(self.meister, bg="lightblue")
        self.tähestiku_raam.pack(side="top")

        tähestik = "abcdefghijklmnopqrstuvwxyz"

        for i, täht in enumerate(tähestik):
            rida = i // 9
            nupp = tk.Button(self.tähestiku_raam, text=täht, width=3, font=("Helvetica", 16), bg="pink", command=lambda t=täht: self.vali_täht(t))
            nupp.grid(row=rida, column=i % 9)

    def loo_kinnituse_nupp(self):
        self.kinnituse_nupp = tk.Button(self.meister, text="Kinnita", bg="white", command=self.kontrolli_sõna)
        self.kinnituse_nupp.pack(side="top", pady=10)

    def loo_katsete_loendur(self):
        self.katsete_silt = tk.Label(self.meister, text="Katseid jäänud: 6", font=("Helvetica", 12), bg="lightblue")
        self.katsete_silt.pack(side="top")

    def vali_täht(self, täht):
        if self.jäänud_katsed == 0:
            return

        for rida in self.sõna_kastid:
            for kast in rida:
                if kast.get() == "":
                    kast.delete(0, tk.END)
                    kast.insert(0, täht)
                    return

    def kontrolli_sõna(self):
        # Вернуть все ячейки обратно к черному цвету
        for rida in self.sõna_kastid:
            for kast in rida:
                kast.config(bg="black")

        praegune_sõna = [kast.get() for rida_kastid in self.sõna_kastid for kast in rida_kastid]
        print("Загаданное слово:", self.sõna)
        print("Введенное слово:", praegune_sõna)
        if not any(praegune_sõna):
            return

        õiged_tähed = []
        vale_positsioonid = []
        for i, täht in enumerate(praegune_sõna):
            if i < len(self.sõna):
                if täht == self.sõna[i]:
                    õiged_tähed.append(i)
                elif täht in self.sõna:
                    vale_positsioonid.append(i)

        for i in range(len(praegune_sõna)):
            if i in õiged_tähed:
                self.sõna_kastid[i // 5][i % 5].config(bg="lightgreen")
            elif i in vale_positsioonid:
                self.sõna_kastid[i // 5][i % 5].config(bg="lightyellow")

        if len(õiged_tähed) == len(self.sõna):
            self.jäänud_katsed = 6
            self.aja_uuendamine()
            messagebox.showinfo("Tulemus", "Õige!")
            self.praegune_sõna_indeks += 1
            if self.praegune_sõna_indeks == len(self.sõnad):
                self.näita_sõnumit("Palju Õnne", "Sa arvasid kõik sõnad ära!")
                self.meister.destroy()
            else:
                self.sõna = self.sõnad[self.praegune_sõna_indeks]
                self.aja_uuendamine()
        else:
            self.jäänud_katsed -= 1
            self.aja_uuendamine()
            messagebox.showinfo("Tulemus", "Vale!")
            if self.jäänud_katsed == 0:
                self.mäng_läbi()

    def aja_uuendamine(self):
        self.katsete_silt.config(text=f"Katseid jäänud: {self.jäänud_katsed}")

    def näita_sõnumit(self, pealkiri, sõnum):
        messagebox.showinfo(pealkiri, sõnum)

def käivita_mäng():
    juur = tk.Tk()
    mäng = WordleMäng(juur)
    juur.mainloop()

if __name__ == "__main__":
    käivita_mäng()
