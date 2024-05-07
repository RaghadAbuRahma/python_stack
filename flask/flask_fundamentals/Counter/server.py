from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'My secret key' 

@app.route('/')
def Counter():
    if 'view_count' in session:
        print("key exists!")
        view_count = session['view_count']
        
    else:
        print("key does NOT exist")
        view_count = 0
        
    view_count += 1
    session['view_count'] = view_count
    return render_template('index.html', view_count=view_count)

@app.route("/destroy_session")
def DestroySession():
    session.clear()		
    return redirect('/')

@app.route('/x2', methods=['POST'])
def CounterX2():
    if 'view_count' in session:
        view_count = session['view_count']
    else:
        view_count = 0
    view_count += 2
    session['view_count'] = view_count
    return render_template('index.html',view_count=view_count )

@app.route('/reset', methods=['POST'])
def Reset():
    view_count = 0 
    session['view_count'] = view_count
    return render_template('index.html',view_count=view_count )




if __name__ == '__main__':
    app.run(debug=True)
