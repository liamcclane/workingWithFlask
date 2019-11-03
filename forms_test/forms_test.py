# server


from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) # our index route will handle rendering our form

app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def homePg():
    return render_template("homePage.html", name_on_template=None, email_on_template=None, submitted = False)


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
#     print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')
    # return render_template("homePage.html", name_on_template=name_from_form, email_on_template=email_from_form, submitted = True)

# adding this method
@app.route("/show")
def show_user():
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    print('*'*25)
    print("Showing the User Info From the Form")
    # print('*'*25)
    print(request.form)
    print('*'*25)
    print(session)
    print('*'*25)
    return render_template("homePage.html",submitted = True)







if __name__ == "__main__":
    app.run(debug=True)
