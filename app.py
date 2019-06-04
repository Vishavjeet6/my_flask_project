from flask import Flask, request,render_template

app = Flask(__name__) #creating new flask object

@app.route("/") # means run "index" function when only "/" is present in the url
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    #return "<h1>Hi {}, your age is {}</h1>".format(name, age)
    return render_template("index.html", name=name, age=age)

@app.route("/login", methods=['GET', 'POST'])
def login():
    #for get request
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # for post request
        username = request.form.get('username')
        password = request.form.get('password')

        if username == password:
            return "Successfully logged in"
        else:
            return "Wrong   password"


if __name__ == "__main__":
    app.run(use_reloader=True, debug = True)
