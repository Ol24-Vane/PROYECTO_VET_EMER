from flask import render_template

def list(turnos):
    return render_template('turno/index.html', turnos=turnos)

def create():
    return render_template('turno/create.html')

def edit(turno):
    return render_template('turno/edit.html', turno=turno )
