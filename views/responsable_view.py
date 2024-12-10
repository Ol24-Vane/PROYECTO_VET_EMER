from flask import render_template

def list(responsables):
    return render_template('responsable/index.html', responsables=responsables)

def create():
    return render_template('responsable/create.html')

def edit(responsable):
    return render_template('responsable/edit.html', responsable=responsable)
