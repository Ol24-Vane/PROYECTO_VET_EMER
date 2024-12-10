from flask import render_template

def list(doctores):
    return render_template('doctores/index.html', doctores = doctores)

def create():
    return render_template('doctores/create.html')

def edit(doctor ):
    return render_template('doctores/edit.html', doctor = doctor)