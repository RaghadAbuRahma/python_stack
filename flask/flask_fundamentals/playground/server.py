from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/play')         
def play():
    return render_template('server.html', x=3) 



@app.route('/play/<x>')         
def hello_world(x):
    return render_template('server.html', x=int(x)) 


@app.route('/play/<x>/<color>')         
def changeColor(x,color):
    return render_template('server.html', x=int(x), color=color ) 
# @app.route('/repeat/play/<x>')
# def repeat(play,x):
#     return f"{play}"*int(x)

    
if __name__=="__main__":   
    app.run(debug=True)    

