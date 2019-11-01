from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # is the home page
def classicHello():
    p = "type in /play into the url to see something cool"
    return render_template('dynamicPlayground.html', numOfSqu = 0, new_color = None, phrase = p)

@app.route('/play')  # this defaults us to the 3 bule squares
def Squ3():
    phrase = "Now type '/play/(the number of boxes you want)' into the url"
    return render_template('dynamicPlayground.html', numOfSqu=3, new_color='lightblue',phrase = phrase)

@app.route('/play/<int:num>')  # routing to multiple words printed
def repeatedSqu(num):
    phrase = "NOOOWWW type '/play/(numberof boxes you want)/(color you want)'"
    return render_template('dynamicPlayground.html', numOfSqu=num, new_color='lightblue',phrase = phrase)


@app.route('/play/<int:num>/<color>')  # routing to multiple words printed
def coloredSqu(num, color):
    phrase = None
    return render_template('dynamicPlayground.html', numOfSqu=num, new_color= color, phrase= phrase)


if __name__ == "__main__":
    app.run(debug=True)
