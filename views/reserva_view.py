from flask import render_template

def list(reservas):
    return render_template('reserva/index.html', reservas=reservas)

def create():
    return render_template('reserva/create.html')

def edit(reserva):
    return render_template('reserva/edit.html', reserva=reserva)
