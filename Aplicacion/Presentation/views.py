   
   
   def register(mysql) 
   registerForm= forms.RegisterForm(request.form)
    datos=[]
    if request.method == 'POST' and registerForm.validate():
        

    return render_template('register.html', form=registerForm)