from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def defaultBoard(x=8,y=8):
    return render_template("index.html",x=int(x),y=int(y))

@app.route('/<x>')
def multipleBlocks(x,y=8):
    return render_template("index.html", x=int(x), y=int(8))

@app.route('/<x>/<y>')
def multipleBlocks2(x,y):
    return render_template("index.html", x=int(x),y=int(y))



if __name__=="__main__":
    app.run(debug=True)