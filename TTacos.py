import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from tkinter import scrolledtext
from PIL import Image, ImageTk

class TTacos:
    def __init__(self):
        self.note = {}

    def aggiungi_nota(self, titolo, testo):
        if titolo and testo:
            self.note[titolo] = testo
            messagebox.showinfo("Nota Aggiunta", "Nota aggiunta con successo!")
        else:
            messagebox.showwarning("Errore", "Inserisci titolo e testo per aggiungere una nota.")

    def visualizza_note_window(self, root):
        note_window = tk.Toplevel(root)
        note_window.title("Elenco delle Note")

        for titolo in self.note:
            tk.Button(note_window, text=titolo, command=lambda t=titolo: self.modifica_nota(t, root)).pack()

    def modifica_nota(self, titolo, root):
        modifica_window = tk.Toplevel(root)
        modifica_window.title("Modifica Nota")

        testo_attuale = self.note[titolo]

        label_titolo = tk.Label(modifica_window, text="Titolo:")
        label_titolo.grid(row=0, column=0, padx=10, pady=5)
        input_titolo = tk.Entry(modifica_window, state='readonly')
        input_titolo.insert(0, titolo)
        input_titolo.grid(row=0, column=1, padx=10, pady=5)

        label_testo = tk.Label(modifica_window, text="Testo:")
        label_testo.grid(row=1, column=0, padx=10, pady=5)
        input_testo = scrolledtext.ScrolledText(modifica_window, height=10, width=50)
        input_testo.insert(tk.END, testo_attuale)
        input_testo.grid(row=1, column=1, padx=10, pady=5)

        bottone_salva = tk.Button(modifica_window, text="Salva Modifiche", command=lambda: self.salva_modifiche(titolo, input_testo.get(1.0, tk.END), modifica_window))
        bottone_salva.grid(row=2, columnspan=2, pady=10)

    def salva_modifiche(self, titolo, nuovo_testo, window):
        self.note[titolo] = nuovo_testo
        window.destroy()
        messagebox.showinfo("Modifiche Salvate", "Modifiche salvate con successo!")

    def cancella_nota(self, titolo):
        if titolo in self.note:
            del self.note[titolo]
            messagebox.showinfo("Cancellazione", f"Nota '{titolo}' cancellata con successo!")
        else:
            messagebox.showinfo("Errore", "La nota specificata non esiste.")

class TTacosUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TTacos - Gestore di Note")

        # Impostazioni predefinite
        self.color_set = {
            "background": "white",
            "foreground": "black",
            "button_bg": "#4CAF50",  # Colore verde per i pulsanti
            "button_fg": "white",
            "label_fg": "black",
            "entry_bg": "white",
            "entry_fg": "black",
            "text_bg": "white",
            "text_fg": "black",
        }

        self.t_tacos = TTacos()

        # Crea la schermata di accesso
        self.crea_schermata_accesso()

    def crea_schermata_accesso(self):
        self.frame_accesso = ttk.Frame(self.root, padding="20", style="TFrame")
        self.frame_accesso.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        label_benvenuto = ttk.Label(self.frame_accesso, text="Benvenuto su TTacos", font=("Helvetica", 16), style="TLabel")
        label_benvenuto.grid(column=0, row=0, columnspan=2, pady=10)

        label_utente = ttk.Label(self.frame_accesso, text="Username:", style="TLabel")
        label_utente.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)

        self.input_utente = ttk.Entry(self.frame_accesso, style="TEntry")
        self.input_utente.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

        label_password = ttk.Label(self.frame_accesso, text="Password:", style="TLabel")
        label_password.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)

        self.input_password = ttk.Entry(self.frame_accesso, show="*", style="TEntry")
        self.input_password.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)

        bottone_accesso = ttk.Button(self.frame_accesso, text="Accedi", command=self.accesso, style="TButton")
        bottone_accesso.grid(column=0, row=3, columnspan=2, pady=10)

        # Configura lo stile
        self.configura_stile()

    def crea_interfaccia(self):
        self.frame = ttk.Frame(self.root, padding="20", style="TFrame")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Barra laterale
        self.crea_barra_laterale()

        self.label_titolo = ttk.Label(self.frame, text="Titolo:", style="TLabel")
        self.label_titolo.grid(column=1, row=0, pady=5, sticky=tk.W)

        self.input_titolo = ttk.Entry(self.frame, style="TEntry")
        self.input_titolo.grid(column=2, row=0, pady=5, sticky=tk.W)

        self.label_testo = ttk.Label(self.frame, text="Testo:", style="TLabel")
        self.label_testo.grid(column=1, row=1, pady=5, sticky=tk.W)

        self.input_testo = scrolledtext.ScrolledText(self.frame, height=10, width=50, style="TText")
        self.input_testo.grid(column=2, row=1, pady=5, sticky=tk.W)

        self.bottone_aggiungi = ttk.Button(self.frame, text="Aggiungi Nota", command=self.aggiungi_nota, style="TButton")
        self.bottone_aggiungi.grid(column=1, row=2, columnspan=2, pady=10)

        # Configura lo stile
        self.configura_stile()

    def crea_barra_laterale(self):
        self.frame_barra_laterale = ttk.Frame(self.root, style="TFrame")
        self.frame_barra_laterale.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.S))

        icon_settings = Image.open("settings.png").resize((30, 30), Image.ANTIALIAS)
        icon_settings = ImageTk.PhotoImage(icon_settings)
        bottone_impostazioni = ttk.Button(self.frame_barra_laterale, image=icon_settings, command=self.mostra_impostazioni, style="TButton")
        bottone_impostazioni.image = icon_settings
        bottone_impostazioni.grid(row=0, column=0, pady=5)

        bottone_visualizza = ttk.Button(self.frame_barra_laterale, text="Visualizza Note", command=self.t_tacos.visualizza_note_window, style="TButton")
        bottone_visualizza.grid(row=1, column=0, pady=5)

        bottone_cancella = ttk.Button(self.frame_barra_laterale, text="Cancella Nota", command=self.t_tacos.cancella_nota, style="TButton")
        bottone_cancella.grid(row=2, column=0, pady=5)

    def mostra_impostazioni(self):
        impostazioni_window = tk.Toplevel(self.root)
        impostazioni_window.title("Impostazioni")

        label_colori = tk.Label(impostazioni_window, text="Seleziona un set di colori:", font=("Helvetica", 12))
        label_colori.grid(row=0, column=0, columnspan=2, pady=10)

        colori_set = {
            "Set 1 (Arancione/Verde)": {"background": "white", "foreground": "black", "button_bg": "#FFA500", "button_fg": "white", "label_fg": "black", "entry_bg": "white", "entry_fg": "black", "text_bg": "white", "text_fg": "black"},
            "Set 2 (Arancione/Nero)": {"background": "black", "foreground": "white", "button_bg": "#FFA500", "button_fg": "white", "label_fg": "white", "entry_bg": "black", "entry_fg": "white", "text_bg": "black", "text_fg": "white"},
            "Set 3 (Blu/Nero)": {"background": "black", "foreground": "white", "button_bg": "blue", "button_fg": "white", "label_fg": "white", "entry_bg": "black", "entry_fg": "white", "text_bg": "black", "text_fg": "white"},
            "Set 4 (Nero/Azzurro)": {"background": "lightblue", "foreground": "black", "button_bg": "black", "button_fg": "white", "label_fg": "black", "entry_bg": "black", "entry_fg": "white", "text_bg": "black", "text_fg": "white"},
            "Set 5 (Hacker)": {"background": "black", "foreground": "#00FF00", "button_bg": "green", "button_fg": "black", "label_fg": "#00FF00", "entry_bg": "black", "entry_fg": "#00FF00", "text_bg": "black", "text_fg": "#00FF00"},
        }

        for i, (set_name, color_set) in enumerate(colori_set.items(), start=1):
            tk.Button(impostazioni_window, text=set_name, command=lambda cs=color_set: self.cambia_colori(cs)).grid(row=i, column=0, columnspan=2, pady=5)

    def cambia_colori(self, color_set):
        self.color_set = color_set
        self.configura_stile()

    def configura_stile(self):
        # Configura uno stile con i colori specificati
        self.root.style = ttk.Style()
        self.root.style.configure("TFrame", background=self.color_set["background"])
        self.root.style.configure("TLabel", foreground=self.color_set["label_fg"], background=self.color_set["background"])
        self.root.style.configure("TEntry", foreground=self.color_set["entry_fg"], background=self.color_set["entry_bg"])
        self.root.style.configure("TText", foreground=self.color_set["text_fg"], background=self.color_set["text_bg"])
        self.root.style.configure("TButton", foreground=self.color_set["button_fg"], background=self.color_set["button_bg"])

    def aggiungi_nota(self):
        titolo = self.input_titolo.get()
        testo = self.input_testo.get("1.0", tk.END)
        self.t_tacos.aggiungi_nota(titolo, testo)

    def accesso(self):
        # Qui puoi implementare la logica di accesso
        # per ora, passiamo direttamente alla schermata principale
        self.frame_accesso.destroy()
        self.crea_interfaccia()

# interfaccia
root = tk.Tk()
app = TTacosUI(root)
root.mainloop()
