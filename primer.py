
from tkinter import Tk, filedialog

root = Tk() 
root.lift() # v ospredje
root.withdraw() # skrije začetno okno
root.wm_attributes('-topmost', 1) # skrije začetno okno
root.geometry("1500x1200") # nastavi velikost okna

# Primer excel in/ali PDF
xlsx = filedialog.askopenfilename(parent=root, initialdir='Documents', title='Izberi Excel datoteko', filetypes=[("Excel datoteke", ".xlsx .xls")]) # show an "Open" dialog box and return the path to the selected file 
pdf = filedialog.askopenfilename(parent=root, initialdir='Documents', title='Izberi PDF datoteko', filetypes=[("PDF datoteke", ".pdf")]) # show an "Open" dialog box and return the path to the selected file 

root.destroy()
