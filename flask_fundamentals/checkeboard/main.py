from flask import Flask, render_template  
app = Flask(__name__)  

print(__name__)
@app.route('/')
def index():
    return render_template("main.html",row=8,col=8)



@app.route('/<int:row>')
def half(row):

    return render_template("main.html", row=row, col=8)


@app.route('/<int:row>/<int:col>')
def checkboard(row, col):

    return render_template("main.html", row=row, col=col)



                    
if __name__== "__main__":
    app.run(debug=True)