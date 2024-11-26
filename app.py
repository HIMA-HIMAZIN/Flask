from flask import Flask, request, jsonify
from libs import my_module


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/flask_app')
def hello_flask():
    return "Hello Flask!"

@app.route('/my_module')
def hello_my_module():
    res = my_module.hello_module()
    return res

@app.route('/my_module2')
def hello_my_module2():
    res = my_module.hello_module2()
    return res

@app.route('/get_text', methods=['GET'])
def get_text():
    text = request.args.get('value')
    res = my_module.text_processing(text)
    return res

@app.route('/get_text2', methods=['GET'])
def get_text2():
    text = request.args.get('value')
    res = my_module.text_processing3(text)
    return res

if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=8080)