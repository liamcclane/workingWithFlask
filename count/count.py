# Lia McClane: 11/1/2019 Friday
# playing with Flask and understanding how to get info from webpage to carry over
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'how many times we have refreshed' # set a secret key for security purposes

@app.route('/') # homepg
def homePg():
    if 'num_visits' in session:
        session['num_visits'] += 1
        print('*'*5)
        print('key exists! we are incrementing')
    else:
        session['num_visits'] = 1
        print('*'*20)
        print("we are creating a brand new key named num_visits and starting at 1 since this is the fisrt visit")
    return render_template('count.html')

@app.route('/doubleV', methods = ['POST'])
def doubleVisits():
    session['num_visits'] += 1
    return redirect('/')

@app.route('/incrementV', methods=['POST'])
def manyVisits():
    # count = 0
    print('inside of manyVisits function')
    # print(f'we are inside the while loop {count}')
    session['num_visits'] += int(request.form['increasedV'])-1
        # count += 1
    return redirect('/')


@app.route("/destroy_session")
def resettingConter():
    # session.clear() # clears all keys
    session.pop('num_visits') # clears a specific key
    # session['num_visits'] = 0
    return redirect('/')
    # return render_template('count.html')




if __name__ == "__main__":
    app.run(debug=True)
