from tkinter import *
import mysql.connector as mysql
from tkinter import ttk
import tkinter.messagebox as MessageBox
from funciones import *



root =Tk()
root.title("STOCK IN")
root.geometry("500x300")
root.minsize(500, 300)
root.maxsize(500, 300)

#COLOCO PANEL PARA LAS PESTAÑAS.
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)
p5 = ttk.Frame(nb)
nb.add(p1,text='Inicio')
nb.add(p2,text='Agregar')
nb.add(p3,text='Modificar')
nb.add(p4,text='Eliminar')
nb.add(p5,text='Ver listado')

fondo=Label(p1)
fondo.configure(bg="white")
fondo.place(x=10, y=11 , width=475, height=254)

bit=PhotoImage(file='img/logo.png',format='png')
lb=Label(p1, None,image=bit)
lb.place(x=75,y=50)

creador=Label(p1, text="Creado por Gabriel Pelizza")
creador.configure(bg="white")
creador.place(x=180,y=244)



#agregar

#texto
l_sku = Label(p2, text="SKU")
l_sku.place(x=20,y=30)

l_producto = Label(p2, text="Nombre de producto")
l_producto.place(x=20,y=60)

l_precio = Label(p2, text="Precio")
l_precio.place(x=20,y=90)

l_cantidad = Label(p2, text="Cantidad")
l_cantidad.place(x=20,y=120)


#Entry
a_sku=Entry(p2)
a_sku.place(x=150,y=30)
#a_sku.configure(bg="lightgray")

a_producto=Entry(p2)
a_producto.place(x=150,y=60)
#a_producto.configure(bg="lightgray")

a_precio=Entry(p2)
a_precio.place(x=150,y=90)
#a_precio.configure(bg="lightgray")

a_cantidad=Entry(p2)
a_cantidad.place(x=150,y=120)
#a_cantidad.configure(bg="lightgray")

#ejcuto la funcion
agregar=Button(p2, text="Agregar", font={"italic", 10}, bg="white", command= lambda: Agregar(a_sku, a_producto, a_precio, a_cantidad, lista))
agregar.place(x=20, y=150)



#MODIFICAR.

#texto
l_sku = Label(p3, text="SKU")
l_sku.place(x=20,y=30)
l_producto = Label(p3, text="Nombre de producto")
l_producto.place(x=20,y=60)
l_precio = Label(p3, text="Precio")
l_precio.place(x=20,y=90)
l_cantidad = Label(p3, text="Cantidad")
l_cantidad.place(x=20,y=120)


#Entry
m_sku=Entry(p3)
m_sku.place(x=150,y=30)
#m_sku.configure(bg="lightgray")

m_producto=Entry(p3)
m_producto.place(x=150,y=60)
#m_producto.configure(bg="lightgray")

m_precio=Entry(p3)
m_precio.place(x=150,y=90)
#m_precio.configure(bg="lightgray")

m_cantidad=Entry(p3)
m_cantidad.place(x=150,y=120)
#m_cantidad.configure(bg="lightgray")

#ejcuto la funcion modificar
modificar=Button(p3, text="Modificar", font={"italic", 10}, bg="white", command= lambda: Modificar(m_sku, m_producto, m_precio, m_cantidad, lista))
modificar.place(x=100, y=150)

#ejcuto la funcion buscar
buscar=Button(p3, text="Buscar", font={"italic", 10}, bg="white", command=lambda: Buscar(m_sku, m_producto, m_precio, m_cantidad))
buscar.place(x=20, y=150)

#ELIMINAR.
#texto
l_sku = Label(p4, text="SKU")
l_sku.place(x=20,y=30)

#Entry
d_sku = Entry(p4)
d_sku.place(x=150,y=30)
#d_sku.configure(bg="lightgray")

#ejecuto la funcion borrar.
borrar = Button(p4, text="Borrar", font={"italic", 10}, bg="white", command= lambda:Borrar(d_sku, lista))
borrar.place(x=20, y=140)

#VER LISTA.
lista=ttk.Treeview(p5)
#defino columnas
lista['columns']=("SKU", "PRODUCTO", "PRECIO", "CANTIDAD")
#doy formato
lista.column("#0", width=10, minwidth=25)
lista.column("SKU", anchor=W, width=80)
lista.column("PRODUCTO", anchor=W, width=150)
lista.column("PRECIO", anchor=W, width=150)
lista.column("CANTIDAD", anchor=W, width=150)
#creo cabezera
lista.heading("#0", text="-", anchor=W)
lista.heading("SKU", text="SKU", anchor=CENTER)
lista.heading("PRODUCTO",text="PRODUCTO", anchor=W)
lista.heading("PRECIO", text="PRECIO", anchor=W)
lista.heading("CANTIDAD", text="CANTIDAD", anchor=W)
lista.place(x=3,y=1, width=489, height=200)


buscador_entrada=Entry(p5)
buscador_entrada.place(x=2, y=210, width=141)

buscador=Button(p5, text="buscar", command= lambda:Buscador(buscador_entrada,resultadodebusquedaSku,resultadodebusquedaProd, resultadodebusquedaPrecio, resultadodebusquedaCant))
buscador.place(x=1, y=240)


limpiar=Button(p5, text="limpiar", command= lambda:Limpiar(buscador_entrada,resultadodebusquedaSku,resultadodebusquedaProd, resultadodebusquedaPrecio, resultadodebusquedaCant))
limpiar.place(x=96, y=240)

borrar2=Button(p5, text="borrar", command= lambda:Borrar2(buscador_entrada,lista))
borrar2.place(x=50, y=240)


resultadodebusquedaSku=Entry(p5, state="readonly")
resultadodebusquedaSku.place(x=190, y=210)
resultadodebusquedaSku.configure(bg="white")

resultadodebusquedaProd=Entry(p5, state="readonly")
resultadodebusquedaProd.place(x=340, y=210)
resultadodebusquedaProd.configure(bg="white")

resultadodebusquedaPrecio=Entry(p5, state="readonly")
resultadodebusquedaPrecio.place(x=190, y=248)
resultadodebusquedaPrecio.configure(bg="white")

resultadodebusquedaCant=Entry(p5, state="readonly")
resultadodebusquedaCant.place(x=340, y=248)
resultadodebusquedaCant.configure(bg="white")

ver_lista(lista)

root.mainloop()