from tkinter import messagebox
from tkinter import*
class validar():
    def Comparador(Usuario,Contraseña):
        valido=0
        def __usuario(Usuario):
            usuario1= "Victor"
            if Usuario==usuario1:
                valido=valido+1
            else:
                messagebox.showerror("error","datos incorrectos verifique")   
        def __contraseña(Contraseña):
            contraseña1=1234
            if Contraseña==contraseña1:
                valido=valido+1
            else:
                messagebox.showerror("error","datos incorrectos verifique")
        if valido==2:
            messagebox.showinfo("Ingreso","Accedio con el usuario " )
        