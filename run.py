from flask import Flask, render_template,request
app = Flask(__name__)

usuarios=[
    {
        "nombre": "juan",
        "contraseña": "admin",
        "mensaje": "Bienvenido administrador juan"
    },
    {
        "nombre": "pepe",
        "contraseña": "user",
        "mensaje": "Bienvenido usuario pepe"
    }]

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/ejercicio2", methods=['GET','POST'])
def ejercicio2():
        if request.method =='POST':
            nombre=request.form['nombre']
            contrasennia=request.form['contrasennia']
            mensaje=""
            for recorre in usuarios:
                if recorre.get("nombre")==nombre and recorre.get("contraseña")==contrasennia:
                     mensaje=recorre.get("mensaje")
            if(len(mensaje)==0):
                 mensaje="Usuario o contraseña incorrectos"
            return render_template('ejercicio2.html',nombre=nombre,contrasennia=contrasennia,mensaje=mensaje)
        return render_template('ejercicio2.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
        if request.method =='POST':
            try:
                nombre=request.form['nombre']
                edad=int(float(request.form['edad']))
                tarros=int(float(request.form['tarros']))
                total=tarros*9000
                descuento=0
                totalConDescuento=total
                if 30>=edad>=18:
                    descuento=round(total*(0.15))
                    totalConDescuento-=descuento
                elif edad>30:
                    descuento=round(total*(0.15))
                    totalConDescuento-=descuento   
                return render_template('ejercicio1.html',nombre=nombre,edad=edad,tarros=tarros,total=total,descuento=descuento,totalConDescuento=totalConDescuento)                   
            except :
                 error='error'
                 return render_template('ejercicio1.html',error=error) 
        return render_template('ejercicio1.html') 

#ejecucion en el servidor
if __name__ == '__main__':
    app.run(debug=True)
