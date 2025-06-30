from tkinter import Tk, filedialog


def izberi_datoteko(tip):
    """
    Funkcija za izbiro datoteke z uporabo tkinter.
    Uporabnik lahko izbere Excel ali PDF datoteko.
    """
    tip = tip.lower()

    root = Tk()
    root.lift()  # v ospredje
    root.withdraw()  # skrije začetno okno
    root.wm_attributes("-topmost", 1)  # skrije začetno okno
    root.geometry("1500x1200")  # nastavi velikost okna

    začetna_datoteka = r"C:\Users"

    type_dict = {
        "excel": ("Excel datoteke", ".xlsx .xls"),
        "pdf": ("PDF datoteke", ".pdf"),
        "word": ("Word datoteke", ".docx .doc"),
        "mapa": ("Mape", ""),
    }

    if tip not in type_dict:
        raise ValueError(f"Neveljaven tip datoteke: {tip}. Uporabite {' ali '.join(type_dict)}.")
    if tip == "mapa":
        out = filedialog.askdirectory(
            parent=root,
            initialdir=začetna_datoteka,
            title="Izberi MAPO",
        )
    else:
        out = filedialog.askopenfilename(
            parent=root,
            initialdir=začetna_datoteka,
            title=f"Izberi {tip.upper()} datoteko",
            filetypes=[type_dict[tip]],
        )

    root.destroy()
    return out


if __name__ == "__main__":
    print(izberi_datoteko("mapa"))
