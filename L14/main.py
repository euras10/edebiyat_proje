# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html,button_db=button_db)



@app.route('/egitim', methods=['POST', 'GET'])
def egitim():
    return render_template('egitim.html')

@app.route('/dogum', methods=['POST', 'GET'])
def dogum():
    return render_template('dogum.html')

@app.route('/eserler', methods=['POST', 'GET'])
def eserler():
    return render_template('eserler.html')

@app.route('/siyasi', methods=['POST', 'GET'])
def siyasi():
    return render_template('siyasi.html')

@app.route('/fiziksel', methods=['POST', 'GET'])
def fiziksel():
    return render_template('fiziksel.html')

@app.route('/ögretmenlik', methods=['POST', 'GET'])
def ögretmenlik():
    return render_template('ögretmenlik.html')

@app.route('/anasayfa', methods=['POST', 'GET'])
def anasayfa():
    return render_template('index.html')

@app.route('/kaynakca', methods=['POST', 'GET'])
def kaynakca():
    return render_template('kaynakca.html')

if __name__ == "__main__":
    app.run(debug=True)

