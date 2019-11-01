from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def fillForm():
    return render_template("dojoServey.html",homepg = True,showInfo=False)

@app.route('/user', methods=['POST'])
def outPrintInfo():
    return render_template('dojoServey.html',homepg=False, showInfo=False)

if __name__ == "__main__":
    app.run(debug=True)