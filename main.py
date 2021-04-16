from flask import Flask, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>IPC2</h1>'

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    if request.method == 'GET':
        return 'Suma'
    else:
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        result = int(numero1) + int(numero2)
        return "suma realizada el resultado es: "+ str(result)

app.run(host='0.0.0.0', debug=True)