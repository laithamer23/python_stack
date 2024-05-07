from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play/<int:num_box>')                           
def play(num_box):
    return render_template('play.html,num_box=num_box')

if __name__=='__main__':
    app.run(debug=True)
  
               

