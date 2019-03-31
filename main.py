from flask import Flask, render_template, request


app = Flask('cfg')


@app.route('/', methods=['GET','POST'])
def home():
    return 'Home'

@app.route('/about')
def hello():
    return 'About This Site'

app.run(debug=True)
