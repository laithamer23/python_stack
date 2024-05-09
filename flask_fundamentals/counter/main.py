from flask import Flask,render_template,session,redirect
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' 

@app.rout('/')
def count():
 if 'counter' not in session:
    session['counter']=0
 session['counter']= session['counter']+1
 return render_template("index.html",conter=session['counter'])


@app.rout('/destroy_session',methods=['POST'])
def destroy():
   session.clear()
   return redirect('/')

@app.rout('/plus2',method=['post'])
def count2():
  if 'counter' not in session: 
   session['counter']=0
   session['counter']= session['counter']+1
   return redirect('/')


if __name__=="__main__":  
    app.run(debug=True)  