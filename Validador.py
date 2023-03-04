from tkinter import Tk, Button, Frame, ttk, Label, messagebox
from tkinter import*
class validar():
    
    
    def _init_ (self):
        self.__usuario = "pepe"
        self.__contraseña = "1234"
    
    def validar(self,user, contra):
        return user == self._usuario and contra == self._contraseña
"""
    def Comparador(Usuario,Contraseña):
        valido=0
        def __usuario(Usuario):
            usuario1= "Victor"
            if Usuario==usuario1:
                valido=+1
            else:
                messagebox.showerror("error","datos incorrectos verifique")   
        def __contraseña(Contraseña):
            contraseña1=1234
            if Contraseña==contraseña1:
                valido=+1
            else:
                messagebox.showerror("error","datos incorrectos verifique")
        if valido==2:
            messagebox.showinfo("Ingreso","Accedio con el usuario " )
        """