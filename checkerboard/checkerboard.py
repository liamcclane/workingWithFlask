# Lia McClane: 10/31/2019 Thurs

# Checkerboad Project, create a dynamic checkerboad where users can typeinto the url the 
# dimensions of the size of the board they want
# this is the python routing page

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/') # homepage with default with the classic chekerboard layout
def classicBoard():
    p = "hello, move along you can choose the height by going into the url and adding an integer after the /"
    return render_template('checkerboard.html', x = 8, y = 8, phrase = p)

@app.route('/<int:num>')
def yChangingBoard(num):
    p = 'you can choose you whole chess board size by typing into the url /x/y '
    p += 'x length and y is the height of the board'
    return render_template('checkerboard.html', x = num, y = 8, phrase = p)

@app.route('/<int:length>/<int:height>')
def xyChangingBoard(length, height):
    p = "yay we did it if you want you can pick the colors now tooooo with the slashes"
    return render_template('checkerboard.html', x = length, y = height, phrase = p)

@app.route('/<int:length>/<int:height>/<notBlack>/<notRed>')
def xyColorChangingBoard(length, height, notBlack, notRed):
    p = "yay we did it if you want you can pick the colors now tooooo with the slashes"
    return render_template('checkerboard.html', x = length, y = height, phrase = p ,oldB = notBlack, oldR = notRed)


if __name__ == "__main__":
    app.run(debug=True)
