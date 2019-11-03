from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def fillForm():
    return render_template("dojoServey.html",homepg = True,showInfo=False ,arr = [])

@app.route('/results', methods=['POST'])
def outPrintInfo():
    print('*'*20)
    print('Got Post Info')
    print('*'*20)
    name_from_py = request.form['name_input']
    location_from_py = request.form['location_input']
    favLan_from_py = request.form['favLan_input']
    comments_from_py = request.form['comment_input']
    arrOfRequests = [name_from_py,location_from_py,favLan_from_py,comments_from_py]

    return render_template('dojoServey.html',homepg=False, showInfo=True,arr=arrOfRequests)

if __name__ == "__main__":
    app.run(debug=True)