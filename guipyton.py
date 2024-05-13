import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# lager databasetabellen
def func_lag_tabell():
    conn = sqlite3.connect('kunde.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS kunder(
        id INTEGER PRIMARY KEY, 
        navn TEXT, 
        epost TEXT, 
        postnummer TEXT, 
        byen TEXT
    )
    ''')
    conn.commit()
    conn.close()

#funksjon for å søke etter kunder
def func_søk_kunde():
    var_søkeord = søk_innlegg.get()
    var_resultat_tabell.delete(*var_resultat_tabell.get_children())
    conn = sqlite3.connect('kunde.db')
    c = conn.cursor()
    c.execute("SELECT * FROM kunder WHERE id=? OR navn LIKE ? OR epost LIKE ? OR postnummer LIKE ? OR byen LIKE ?",
               (var_søkeord, '%'+var_søkeord+'%', '%'+var_søkeord+'%', '%'+var_søkeord+'%', '%'+var_søkeord+'%'))
    var_resultater = c.fetchall()
    for var_rad in var_resultater:
        var_resultat_tabell.insert('', 'end', text=var_rad[0], values=(var_rad[1], var_rad[2], var_rad[3], var_rad[4]))
    conn.close()

#funksjon for å legge til en ny kunde


#main funksjonen
def func_main():
    var_main = tk.Tk()
    var_main.title("Kunde Database App")

    # Opprett databasetabell hvis den ikke eksisterer
    func_lag_tabell()

    # GUI-komponenter
    søk_etikett = ttk.Label(var_main, text="Søk:")
    søk_etikett.grid(row=0, column=0, padx=10, pady=10)

    global søk_innlegg
    søk_innlegg = ttk.Entry(var_main)
    søk_innlegg.grid(row=0, column=1, padx=10, pady=10)

    søk_knapp = ttk.Button(var_main, text="Søk", command=func_søk_kunde)
    søk_knapp.grid(row=0, column=2, padx=10, pady=10)

    # lager tabell visningen
    global var_resultat_tabell
    var_resultat_tabell = ttk.Treeview(var_main, columns=('Navn', 'E-post', 'Postnummer', 'By'))
    var_resultat_tabell.heading('#0', text='Kunde ID')
    var_resultat_tabell.heading('Navn', text='Navn')
    var_resultat_tabell.heading('E-post', text='E-post')
    var_resultat_tabell.heading('Postnummer', text='Postnummer')
    var_resultat_tabell.heading('By', text='By')
    var_resultat_tabell.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # lager scrollbar for tabellen
    var_resultat_rullefelt = ttk.Scrollbar(var_main, orient='vertical', command=var_resultat_tabell.yview)
    var_resultat_rullefelt.grid(row=1, column=3, sticky='ns')
    var_resultat_tabell.configure(yscrollcommand=var_resultat_rullefelt.set)

    # Legger til "legg til kunde" teksten i gui-en
    legg_til_etikett = ttk.Label(var_main, text="Legg til ny kunde")
    legg_til_etikett.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Legger til feltene for å legge til en ny kunde
    navn_etikett = ttk.Label(var_main, text="Navn:")
    navn_etikett.grid(row=3, column=0, padx=10, pady=5)
    global var_navn_innlegg
    var_navn_innlegg = ttk.Entry(var_main)
    var_navn_innlegg.grid(row=3, column=1, padx=10, pady=5)

    epost_etikett = ttk.Label(var_main, text="E-post:")
    epost_etikett.grid(row=4, column=0, padx=10, pady=5)
    global var_epost_innlegg
    var_epost_innlegg = ttk.Entry(var_main)
    var_epost_innlegg.grid(row=4, column=1, padx=10, pady=5)

    postnummer_etikett = ttk.Label(var_main, text="Postnummer:")
    postnummer_etikett.grid(row=5, column=0, padx=10, pady=5)
    global var_postnummer_innlegg
    var_postnummer_innlegg = ttk.Entry(var_main)
    var_postnummer_innlegg.grid(row=5, column=1, padx=10, pady=5)

    by_etikett = ttk.Label(var_main, text="By:")
    by_etikett.grid(row=6, column=0, padx=10, pady=5)
    global var_by_innlegg
    var_by_innlegg = ttk.Entry(var_main)
    var_by_innlegg.grid(row=6, column=1, padx=10, pady=5)


    # Start GUI-løkke
    var_main.mainloop()

if __name__ == "__main__":
    func_main()
