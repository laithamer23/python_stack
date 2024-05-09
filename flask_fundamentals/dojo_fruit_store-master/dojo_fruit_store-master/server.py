from flask import Flask, render_template, request
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():

    firstname=request.form["first_name"]
    lastname = request.form["last_name"]
    studentid =request.form["student_id"]
    strawberry=request.form["strawberry"]
    raspberry=request.form["raspberry"]
    apple=request.form["apple"]
    total=int(strawberry)+int(raspberry)+int(apple)
    print(request.form)
    print(f"changing,{firstname} {lastname} for {total} fruits")

    return render_template("checkout.html",firstname=firstname,lastname=lastname,studentid=studentid,
                           strawberry=int(strawberry),raspberry=int(raspberry),apple=int(apple),total=int(total))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    