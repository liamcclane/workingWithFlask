# Lia McClane: 11/1/2019 Friday

# I'm thinking of a number between 1 and 100...
# Create a site that allows a user to play this guessing game. Upon loading, 
# the server should "pick" a random number between 1-100; store the number in session. 
# Allow the user to guess the number--tell them when they are too high or too low. 
# If they guess the correct number, notify them and offer to play again.

from flask import Flask, render_template, request, redirect, session

import random # import the random module
random.randint(1, 100) # random number between 1-100

app = Flask(__name__)
app.secret_key = 'idk what this represents' 

@app.route('/')
def homepg():
    # print('*-'*5,'We are in the homePg function', '*-'*35)

    if 'results' not in session:          # only run this code if we are restarting the game
        session['compNum'] = random.randint(1, 100)
        session['capOfGuesses'] = 5

    # print('the com number is ', session['compNum'])
    # print('user has ', session['capOfGuesses'], ' left to guess correctly')
    # print(session)

    # print('*-'*50)
    return render_template('great_number_game.html')


@app.route('/guessed', methods=['POST'])
def winLose():
    
    # print('*'*25, 'we are inside the winLose function', '*'*25 )
    if request.form['num_guess'] == '':
        return redirect('/')
    session['userGuess'] = int(request.form['num_guess'])
    # print('the user has passed : ', session['userGuess'])
    # print('the computer is working with : ', session['compNum'])
    
    if session['userGuess'] < session['compNum']:
        session['capOfGuesses'] -= 1
        session['results'] = 'tooLow'
    
    elif session['userGuess'] > session['compNum']:
        session['capOfGuesses'] -= 1
        session['results'] = 'tooHigh'
    
    else:                                          # when user guesses correctly move them to the succes page 
        session['results'] = 'success' 
        return render_template('successPg.html')
        # return redirect('/successPg')

    if session['capOfGuesses'] == 0:               # redirect if we run out of guesses
        return render_template('/loserPG.html')
        # return redirect('/ranOutOfGuesses')

    # print("the user's guess was not seccessful the are " , session['results'])
    # print('*'*75)
    return redirect('/')                           # go back to the homepage if the guess was unsuccessful

@app.route('/successPg')
def successFun():
    return render_template('successPg.html')

@app.route('/ranOutOfGuesses')
def lostGame():
    return render_template('/loserPG.html')

@app.route('/playAgain')
def newGame():
    print('*-'*10, 'inside the newgame function' ,'*'*50)
    session.clear()
    session['compNum'] = random.randint(1, 10)
    session['capOfGuesses'] = 6
    # print('what I need to clear',session['results'])
    # session.pop('results')
    # print('what was cleared',session['results'])
    print('-*-'*15)
    return redirect('/')


if(__name__) == "__main__":
    app.run(debug=True)