import sqlite3


class Ingreso: #se define la clase ingreso
    
    def __init__(self,u):
        self.usuario=u
        
     
    def ingresoSemanal(self,abono):
        
        usuario=self.usuario
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor() 
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}'".format(usuario))
        aux=cursor.fetchall()
        saldo=aux[0][3]
        saldo=saldo+abono
        cursor.execute("UPDATE PERSONAS SET saldo='{}' WHERE usuario='{}'".format(saldo,usuario))
        conexion.commit()
        conexion.close()
        
     
    def resta(self,gasto):
        usuario=self.usuario
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor() 
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}'".format(usuario))
        aux=cursor.fetchall()
        saldo=aux[0][3]
        saldo=saldo-gasto
        cursor.execute("UPDATE PERSONAS SET saldo='{}' WHERE usuario='{}'".format(saldo,usuario))
        conexion.commit()
        conexion.close()
        
    
    def resultado(self):
        conexion=sqlite3.connect("BasedeDatos1.db")
        usuario=self.usuario
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}'".format(usuario))
        aux=cursor.fetchall()
        conexion.close()
        return aux[0][3]

        

class Usuario:
    def __init__(self,u,c):
        self.usuario=u
        self.contra=c
        
    def registrar(self,nombre):##aqui se registra un usuario en la pagina con su correo,nombre y contrasena
        conexion=sqlite3.connect("BasedeDatos1.db")
        usuario=self.usuario
        contra=self.contra
        cursor=conexion.cursor()
        auxiliar=[] 
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}'".format(usuario))
        auxiliar=cursor.fetchall()#creamos una variable auxiliar para validar si el usuario existe o no
        if auxiliar==[]:
            cursor.execute("INSERT INTO PERSONAS VALUES ('{}','{}','{}',0.0,0)".format(usuario,contra,nombre))
            conexion.commit()
            conexion.close()
            return 0
        else:
            conexion.close()
            return 1 
        
    def initSesion(self):# metodo iniciar sesion y hace la consulta pidiendo usuario y contrasena
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor()
        usuario=self.usuario
        contra=self.contra
        auxiliar=[]
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}' AND contrasena='{}'".format(usuario,contra))
        auxiliar=cursor.fetchall()
        if auxiliar==[]:#creamos la variable auxiliar para valiar
            conexion.close()
            return 0 
        else:
            conexion.close()
            return 1

class Administrador:
    def __init__(self,u):
        self.usuario=u

    def comprobar(self):
        usuario=self.usuario
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor()
        aux=[]
        cursor.execute("SELECT * FROM PERSONAS WHERE usuario='{}'".format(usuario))
        aux=cursor.fetchall()
        if aux[0][4]==1:
            return 1
        else:
            return 0

        
    def Alta(self):
        usuario=self.usuario
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor()
        cursor.execute("UPDATE PERSONAS SET key=1 WHERE usuario='{}'".format(usuario))#cuando se de alta como administrador en la columana KEY aparecera en uno o 1
        conexion.commit()
        conexion.close()
        
   
    def Lista(self):
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM PERSONAS")
        consulta=cursor.fetchall()
        conexion.close()
        return consulta
    
    def Eliminar(self):
        usuario=self.usuario
        conexion=sqlite3.connect("BasedeDatos1.db")
        cursor=conexion.cursor()
        cursor.execute("DELETE  FROM PERSONAS WHERE usuario='{}'".format(usuario))
        conexion.commit()
        conexion.close() 

