# server


from flask import Flask, render_template, request, redirect

app = Flask(__name__) # our index route will handle rendering our form

@app.route('/')
def homePg():
    return render_template("homePage.html", name_on_template=None, email_on_template=None, submitted = False)


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
#     print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("homePage.html", name_on_template=name_from_form, email_on_template=email_from_form, submitted = True)


if __name__ == "__main__":
    app.run(debug=True)
