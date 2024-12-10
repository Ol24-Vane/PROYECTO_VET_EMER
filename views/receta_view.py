from flask import render_template

def list(recetas):
    return render_template('receta/index.html', recetas=recetas)

def create():
    return render_template('receta/create.html')

def edit(receta):
    return render_template('receta/edit.html', receta=receta)
