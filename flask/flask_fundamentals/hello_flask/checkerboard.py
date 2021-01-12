from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')          
def hello_world():
    return render_template("checkerboard.html", row=8, column=8)

@app.route('/4')          
def render_8x4():
    return render_template("checkerboard.html", row=8, column=4)

@app.route('/<row>/<column>')          
def render_r_c(row, column):
    return render_template("checkerboard.html", row=int(row), column=int(column))




if __name__=="__main__":   
    app.run(debug=True)  

