from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
import flask
from flask.globals import request
from flask.wrappers import Request
from Database import db
import forms, functions

def registraUsuario(mysql):
    registerForm= forms.RegisterForm(request.form)
    datos=[]
    datos.append(request.form['usuario'])
    datos.append(request.form['nombre'])
    datos.append(request.form['apellido'])
    datos.append(request.form['mail'])
    datos.append(request.form['contrasenia'])
    datos.append(request.form['sexo'])
    datos.append(request.form['fechaNacimiento'])
    datos.append(request.form['altura'])
    datos.append(request.form['peso'])
    datos.append(request.form['cintura'])
    datos.append(request.form['cuello'])
    datos.append(request.form['caderas'])

    x= (i for i in datos if i.strip()=="")
    lista = list(x) 
        if (len(lista)!=0):
            flash('Complete todos los datos')
        else:

            coincidenciasUsuario= db.coincidenciasMail(datos, mysql)
            coincidenciasMail= db.coincidenciasUsuario(datos, mysql)
            if (len(coincidenciasMail)==0 and len(coincidenciasUsuario)==0):
                db.registrarUsuario(datos, mysql)
                flash('Registrado correctamente')
                return redirect(url_for('Index', success=True))
            else:
                if (len(coincidenciasUsuario)!=0):
                    flash('El usuario ya esta registrado')
                if (len(coincidenciasMail)!=0):
                    flash('El mail ya esta registrado')
                return redirect(url_for('Register'))