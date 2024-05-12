from flask import Flask, render_template, redirect,session,request
import random 	
app = Flask(__name__)
app.secret_key ='axsos'

@app.route("/")
def main():

    if 'random' not in session:
        session['random'] = random.randint(1, 100)
        session['counter'] = 0
    
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def compare():
    session['counter'] += 1
    session['guess'] = int(request.form['userinput'])
    guessed_num = session['guess']
    if guessed_num>session['random']:
        session['reply'] = 'high'
    elif guessed_num<session['random']:
        session['reply'] = 'low'
    else:
        session['reply'] = 'win'
    return redirect('/')

@app.route("/reset")
def clearsessions():
    session.clear()
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)    

