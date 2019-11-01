# Flask Fundamentals: Undersanding Routing from scrach
# Lia McClane: 10/30/2019 Wednesday

from flask import Flask, render_template, url_for # Importing Flask

app = Flask(__name__) # creating a variable with the class name Flask
                      # with that comes many functions
@app.route('/') # is the home page
def classicHello():
    htmlString = "<h3>Hello World!!! continue on to see more</h3>"
    return htmlString

@app.route('/say/<name>', methods=['GET', 'POST'])
def helloPhrase(name):
    return "<h2>Greetings "+ name.capitalize() + "</h2> <p>want to play a game?</p>"
def chuckImg():
    return render_template('meme1.jfif')

@app.route('/repeat/<int:num>/<word>') # routing to multiple words printed
def repeatedWord(num , word):
    repeatedPhrase = ''
    for i in range(num):
        repeatedPhrase += f"<p>{word.capitalize()}</p>"
    return repeatedPhrase

# NINJA BONUS: For the 4th task, ensure the 2nd element in the 
    # URL is an integer (hint: http://exploreflask.com/en/latest/views.html#url-converters)
# @app.route('/repeat/<wrong>/<words>')
# def notNum(words):
#     return "you did not input a interger after /repeat/ so I cannot repeate " + {words}
# # SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, 
#     # they receive an error message saying "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)