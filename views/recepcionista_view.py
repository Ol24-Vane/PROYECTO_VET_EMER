from flask import render_template

def list(recepcionistas):
    return render_template('recepcionistas/index.html', recepcionistas=recepcionistas)

def create():
    return render_template('recepcionistas/create.html')

def edit(recepcionista):
    return render_template('recepcionistas/edit.html', recepcionista=recepcionista)
