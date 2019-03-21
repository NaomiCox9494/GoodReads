
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
# def home():
#     return "Hello, World!"  # return a string

@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/Manga')
def manga():
    return render_template('manga.html')

@app.route('/comics')
def comics():
    return render_template('comics.html')

@app.route('/SciFi')
def SciFi():
    return render_template('SciFi.html')

@app.route('/fruitsbasket')
def fruitsbasket():
    return render_template('fruitsbasket.html')

@app.route('/deathNote')
def deathNote():
    return render_template('deathNote.html')

@app.route('/OuranHost')
def OuranHost():
    return render_template('OuranHost.html')

@app.route('/Watchmen')
def Watchmen():
    return render_template('Watchmen.html')

@app.route('/Saga')
def Saga():
    return render_template('Saga.html')

@app.route('/Batman')
def Batman():
    return render_template('Batman.html')

@app.route('/Dune')
def Dune():
    return render_template('Dune.html')

@app.route('/Hitchhikers')
def Hitchhikers():
    return render_template('Hitchhikers.html')

@app.route('/Enders')
def Enders():
    return render_template('Enders.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
