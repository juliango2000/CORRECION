from flask import Flask, jsonify, request,render_template,redirect,url_for
from BACKEND import Usuario,Ingreso,Administrador
import sqlite3
app= Flask(__name__)

aux=["","","",0.0,1]

@app.route("/")
def index():
    
    return render_template('ejemplo.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/registro_ok", methods=["POST"])
def registro_ok():
    usuario=request.form["username"]
    contra=request.form["pwd"]
    nombre=request.form["name"]
    obj2=Usuario(usuario,contra)
    aux=obj2.registrar(nombre)

    if aux:
        return render_template("no_registro.html")
    else:
        return render_template("registro_ok.html")


@app.route("/saludo",  methods=["GET","POST"])
def saludo():
    
    usuario=request.form["username"]
    contra=request.form["pwd"]
    print(usuario)
    print(type(usuario))
    obj1=Usuario(usuario,contra)
    aux=obj1.initSesion()
    if aux:
        
        return redirect("/cuenta?username={}".format(usuario))

    else:
        
        return render_template("no_login.html")

@app.route("/cuenta",methods=['GET'])
def cuenta():
    usuario=request.args.get('username')
    obj3=Ingreso(usuario)
    saldo=obj3.resultado()
    return render_template("cuenta.html",saldo=saldo,usuario=usuario)

@app.route("/+saldo",methods=["GET","POST"])
def sal():
    abono=float(request.form["sal"])
    usuario=request.args.get('username')
    obj4=Ingreso(usuario)
    obj4.ingresoSemanal(abono)
    return render_template("+saldo.html",abono=abono,usuario=usuario)

@app.route("/-saldo",methods=["GET","POST"])
def resta():
    abono=float(request.form["sal"])
    usuario=request.args.get('username')
    obj4=Ingreso(usuario)
    obj4.resta(abono)
    return render_template("-saldo.html",abono=abono,usuario=usuario)


@app.route("/administracion", )
def admin():
    usuario=request.args.get('username')
    obj5=Administrador(usuario)
    aux=obj5.comprobar()
    if aux:
        usuarios=obj5.Lista()
        n=[]
        for i in range(len(usuarios)):
            n.append(i)
        return render_template('admin.html',usuarios=usuarios,administrador=usuario,n=n)
    else:
        return render_template('noadmin.html',usuario=usuario)

@app.route("/alta",methods=["POST"])
def alta():
    administrador=request.form["administrador"]
    usuario=request.form["username"]
    print(usuario)
    print(type(usuario))
    obj6=Administrador(usuario)
    obj6.Alta()
    return render_template('alta.html',administrador=administrador,usuario=usuario)

@app.route("/eliminar",methods=["POST"])
def eliminar():
    administrador=request.form["administrador"]
    usuario=request.form["username"]
    obj6=Administrador(usuario)
    obj6.Eliminar()
    return render_template('eliminar.html',administrador=administrador,usuario=usuario)


if __name__ == '__main__':
    app.run(debug=True)
