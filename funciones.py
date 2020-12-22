import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk

def Agregar(a_sku, a_producto, a_precio, a_cantidad, lista):
    sku = a_sku.get()
    producto = a_producto.get()
    precio = a_precio.get()
    cantidad = a_cantidad.get()
    
    if(sku=="" or producto=="" or precio=="" or cantidad==""):
        MessageBox.showinfo("Estado del alta de producto", "Es obligatorio completar los campos")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")        
        cursor = con.cursor()
        control="SELECT * FROM users WHERE id = {}".format(sku)
        cursor.execute(control);
        if len(cursor.fetchall())<1:
            sql ="INSERT INTO users (id, producto, precio, cantidad) VALUES (%s,%s,%s,%s)"
            val =(f"{sku}", f"{producto}", f"{precio}",f"{cantidad}")
            cursor.execute(sql, val);
            cursor.execute("commit");
            a_sku.delete(0,'end')
            a_producto.delete(0,'end')
            a_precio.delete(0,'end')
            a_cantidad.delete(0,'end')
            ver_lista(lista)
            MessageBox.showinfo("Estado del alta de producto", "Se agrego correctamente")
            con.close();
        else:
            MessageBox.showinfo("Estado del alta de producto", "El producto ya existe")
            
            

def Modificar(m_sku, m_producto, m_precio, m_cantidad, lista):
    sku = m_sku.get()
    producto = m_producto.get()
    precio = m_precio.get()
    cantidad = m_cantidad.get()
    if(sku=="" or producto=="" or precio=="" or cantidad==""):
        MessageBox.showinfo("Estado de actualizacion", "Por favor complete todos los campos")
    else:
        if MessageBox.askyesno("Estado de actualizacion","Estas seguro que deseas modificar el producto?"):
            con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")
            cursor = con.cursor()
            sql ="UPDATE users SET producto = %s, precio = %s, cantidad = %s WHERE id = {}".format(sku)
            val=(f"{producto}", f"{precio}", f"{cantidad}")
            cursor.execute(sql, val);
            cursor.execute("commit");
            m_sku.delete(0,'end')
            m_producto.delete(0,'end')
            m_precio.delete(0,'end')
            m_cantidad.delete(0,'end')
            ver_lista(lista)
            MessageBox.showinfo("Estado de actualizacion", "El producto se actualizo correctamente")
            con.close();
        else:
            MessageBox.showinfo("Estado de actualizacion", "no se realizaron cambios") 
           
           
           
def Buscar(m_sku, m_producto, m_precio, m_cantidad):
    sku=m_sku.get()
    if(sku ==""):
        MessageBox.showinfo("Estado de busqueda", "Es obligatorio colocar el sku")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")        
        cursor = con.cursor()
        control2="SELECT * FROM users WHERE id = {} ".format(sku)
        cursor.execute(control2);
        if len(cursor.fetchall())>0:
            sql="SELECT * FROM users WHERE id = {} ".format(sku)
            cursor.execute(control2);
            rows=cursor.fetchall() 
            for row in rows:
                m_producto.insert(0, row[1])
                m_precio.insert(0, row[2])
                m_cantidad.insert(0, row[3])
            MessageBox.showinfo("Estado de busqueda", "Producto encontrado")
            con.close();
        else:
            MessageBox.showinfo("Estado de busqueda", "No se encontro el producto")

def Borrar(d_sku, lista):
    sku=d_sku.get()
    if(sku == ""):
        MessageBox.showinfo("Estado de baja", "Es necesario que coloques el SKU del elemento a eliminar")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")  
        cursor = con.cursor()
        control3="SELECT * FROM users WHERE id = {} ".format(sku)
        cursor.execute(control3)
        if len(cursor.fetchall())>0:
            cursor.execute(control3);
            rows=cursor.fetchall() 
            for row in rows:
                row[0]
                row[1]
                row[2]
                row[3]    
            if MessageBox.askyesno("confirmacion",f"Realmente deseas elminiar este producto?\n {row[0]} -- {row[1]} -- {row[2]} -- {row[3]}"):        
                cursor = con.cursor()
                sql="DELETE FROM users WHERE id = {} ".format(sku)
                cursor.execute(sql);
                cursor.execute("commit");
                d_sku.delete(0,'end')
                ver_lista(lista)
                MessageBox.showinfo("Estado de baja", "El producto se borro exitosamente")
                con.close();
            else:
                MessageBox.showinfo("Estado de baja", "No se realizo cambios")
        else:
            MessageBox.showinfo("Estado de baja", "El producto no existe")
            


def ver_lista(lista):
    con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")        
    cursor = con.cursor()
    sql="SELECT * FROM users"
    cursor.execute(sql);
    rows=cursor.fetchall()
    lista.delete(*lista.get_children())
    for i in rows:
        lista.insert('', 'end', values=i)
    con.close();
    
    
def Buscador(buscador_entrada, resultadodebusquedaSku, resultadodebusquedaProd, resultadodebusquedaPrecio, resultadodebusquedaCant):
    sku=buscador_entrada.get()
    if(sku ==""):
        MessageBox.showinfo("Estado de busqueda", "Es obligatorio colocar el sku")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")        
        cursor = con.cursor()
        control2="SELECT * FROM users WHERE id = {} ".format(sku)
        cursor.execute(control2);
        if len(cursor.fetchall())>0:
            sql="SELECT * FROM users WHERE id = {} ".format(sku)
            cursor.execute(control2);
            rows=cursor.fetchall() 
            for row in rows:
                row[1]
                row[2]
                row[3]
            resultadodebusquedaSku.config(state='normal')
            resultadodebusquedaSku.delete(0,'end')
            resultadodebusquedaSku.insert(0, str(f"SKU: ${row[0]}"))
            resultadodebusquedaSku.config(state='readonly')
            
            resultadodebusquedaProd.config(state='normal')
            resultadodebusquedaProd.delete(0,'end')
            resultadodebusquedaProd.insert(0, str(f"Prod: {row[1]}"))
            resultadodebusquedaProd.config(state='readonly')
            buscador_entrada.delete(0,'end')
            
            resultadodebusquedaPrecio.config(state='normal')
            resultadodebusquedaPrecio.delete(0,'end')
            resultadodebusquedaPrecio.insert(0, str(f"Precio:  {row[2]}"))
            resultadodebusquedaPrecio.config(state='readonly')
            
            resultadodebusquedaCant.config(state='normal')
            resultadodebusquedaCant.delete(0,'end')
            resultadodebusquedaCant.insert(0, str(f"Cant:  {row[3]}"))
            resultadodebusquedaCant.config(state='readonly')
            
            buscador_entrada.delete(0,'end')
            MessageBox.showinfo("Estado de busqueda", "Producto encontrado")
            con.close();
        else:
            MessageBox.showinfo("Estado de busqueda", "No se encontro el producto")

def Limpiar(buscador_entrada, resultadodebusquedaSku, resultadodebusquedaProd, resultadodebusquedaPrecio, resultadodebusquedaCant):
    buscador_entrada.delete(0,'end')
    resultadodebusquedaSku.config(state='normal')
    resultadodebusquedaSku.delete(0,'end')
    resultadodebusquedaSku.config(state='readonly')
    
    buscador_entrada.delete(0,'end')
    resultadodebusquedaProd.config(state='normal')
    resultadodebusquedaProd.delete(0,'end')
    resultadodebusquedaProd.config(state='readonly')
    
    buscador_entrada.delete(0,'end')
    resultadodebusquedaPrecio.config(state='normal')
    resultadodebusquedaPrecio.delete(0,'end')
    resultadodebusquedaPrecio.config(state='readonly')
    buscador_entrada.delete(0,'end')
    
    resultadodebusquedaCant.config(state='normal')
    resultadodebusquedaCant.delete(0,'end')
    resultadodebusquedaCant.config(state='readonly')
    
    
def Borrar2(buscador_entrada, lista):
    sku=buscador_entrada.get()
    if(sku == ""):
        MessageBox.showinfo("Estado de baja", "Es necesario que coloques el SKU del elemento a eliminar")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="ejemplo")  
        cursor = con.cursor()
        control3="SELECT * FROM users WHERE id = {} ".format(sku)
        cursor.execute(control3)
        if len(cursor.fetchall())>0:
            cursor.execute(control3);
            rows=cursor.fetchall() 
            for row in rows:
                row[0]
                row[1]
                row[2]
                row[3]    
            if MessageBox.askyesno("confirmacion",f"Realmente deseas elminiar este producto?\n {row[0]} -- {row[1]} -- {row[2]} -- {row[3]}"):        
                cursor = con.cursor()
                sql="DELETE FROM users WHERE id = {} ".format(sku)
                cursor.execute(sql);
                cursor.execute("commit");
                buscador_entrada.delete(0,'end')
                ver_lista(lista)
                MessageBox.showinfo("Estado de baja", "El producto se borro exitosamente")
                con.close();
            else:
                MessageBox.showinfo("Estado de baja", "No se realizo cambios")
        else:
            MessageBox.showinfo("Estado de baja", "El producto no existe")
 