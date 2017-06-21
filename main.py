from flask import Flask,render_template

app=Flask(__name__)




@app.route("/profile/<name>")
def pofile(name):
    return render_template("profile.html",name=name)

@app.route("/")
@app.route("/<user>")
def index(user=None):

    return render_template("user.html",user=user)


@app.route("/shopping")
def shopping():
    food = ["Cheese","Tuna","Beef"]
    return render_template("shopping.html",food=food)

if __name__=="__main__":
    app.run(debug=True)