from flask import render_template

def list(consultas):
    return render_template('consulta/index.html', consultas=consultas)

def create():
    return render_template('consulta/create.html')

def edit(consulta):
    return render_template('consulta/edit.html', consulta=consulta)
