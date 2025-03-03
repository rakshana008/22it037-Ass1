from flask import Flask 
app = Flask(_name_)
@app.route('/')
def personal_details():
    return 'Hello,World!'

@app.route('/name')
def get_name():
    return 'RAKSHANA'
@app.route('/regno')
def get_regno():
    return '22IT037'
@app.route('/department')
def get_dept():
    return 'Information Technology'
if _name_ == '_main_':
    app.run(debug=True)
