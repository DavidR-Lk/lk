from tkinter import *

frm_listas = Tk()
frm_listas.title("Listas")
frm_listas.geometry("400x400")

Lmp = 300
Hrn = 3000
Btr = 500
Crg = 400
Fcs = 150
Vnt = 1500

def Agregar():
    Indices = Lst_objetos.curselection()
    for i in Indices:
        Lst_ventas.insert(i, Lst_objetos.get(i))
        Lst_objetos.delete(i)

def Quitar():
    Indices = Lst_ventas.curselection()
    for i in Indices:
        Lst_objetos.insert(i, Lst_ventas.get(i))
        Lst_ventas.delete(i)

def Total():
    Items = Lst_ventas.get(0, END)
    suma = 0
    for i in Items:
        if i == "Lamparas":
            suma += Lmp
        elif i == "Hornos":
            suma += Hrn
        elif i == "Baterias":
            suma += Btr
        elif i == "Cargadores":
            suma += Crg
        elif i == "Focos Led":
            suma += Fcs
        elif i == "Ventiladores":
            suma += Vnt
    Lst_Subtotal.delete(0, END)
    Lst_Subtotal.insert(END, f"${suma}")

Lst_objetos = Listbox(selectmode=EXTENDED)
Objects = ["Lamparas", "Hornos", "Baterias", "Cargadores", "Focos Led", "Ventiladores"]
Lst_objetos.insert(0, *Objects)
Lst_objetos.grid(row=0, column=0)

Lst_ventas = Listbox(selectmode=EXTENDED)
Lst_ventas.grid(row=0, column=2)

Lst_Subtotal = Listbox(selectmode=EXTENDED)
Lst_Subtotal.grid(row=0, column=3)

agregar_btn = Button(frm_listas, text="Agregar", command=Agregar)
agregar_btn.grid(row=1, column=0)

Quitar_btn = Button(frm_listas, text="Quitar", command=Quitar)
Quitar_btn.grid(row=1, column=1)

Total_btn = Button(frm_listas, text="Total", command=Total)
Total_btn.grid(row=1, column=2)

frm_listas.mainloop()
