from flask import Flask, render_template,session,redirect,request
app=Flask(__name__)
app.secret_key='wordpass!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def process():
# session is memory request form is user input. 
# How to link html and python? With key names 
# if session key does not match key on html it will remember the last input
# if request.form key does not match it will show error " undefine"
    session['nm'] = request.form ['nm']
    session['lc'] = request.form ['lc']
    session['lg'] = request.form ['lg']
    session['cm'] = request.form ['cm']
    # want to redirect this form to a new page?
    # create another html page and send user selection to different page
    return redirect ('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True,port=8000)