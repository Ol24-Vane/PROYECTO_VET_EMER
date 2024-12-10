from flask import render_template

def list(productos):
    return render_template('producto/index.html', productos=productos)

def create():
    return render_template('producto/create.html')

def edit(producto):
    return render_template('producto/edit.html', producto=producto)
