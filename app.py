from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="AceCampusFoodPan",
    password="d2190187",
    hostname="AceCampusFoodPantry.mysql.pythonanywhere-services.com",
    databasename="AceCampusFoodPan$pantryDB",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Item(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    inventory = db.Column(db.Integer)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("BDBI-pantry-web-interface.html", items=Item.query.all())

    for i in Item.query.all(): # in all of the food data
        if (request.form[i.content] != "-"): # other than "test food" because there's a space in its name
            if (request.form[i.content] != i.content): # we want the textform that was changed to the number to be withdrawn
                i.inventory = i.inventory - int(request.form[i.content])
                db.session.commit()
    return render_template("BDBI-pantry-web-interface.html", items=Item.query.all())


@app.route('/donation', methods=["GET", "POST"])
def donate():
    if request.method == "GET":
        return render_template("BDBI-pantry-web-interface-donation.html", items=Item.query.all())

    if request.method == "POST":
        for i in Item.query.all(): # in all of the food data
            if (i.content != "test food"): # other than "test food" because there's a space in its name
                if (request.form[i.content] != i.content): # we want the textform that was changed to the number to be withdrawn
                    i.inventory = i.inventory + int(request.form[i.content])
                    db.session.commit()
        numnew = str(request.form["numnew"])
        while ('/' in numnew):
            if (request.form[numnew[0 : numnew.index('/')]].isnumeric()):
                item = Item(content = numnew[0 : numnew.index('/')], inventory = int(request.form[numnew[0 : numnew.index('/')]]))
            else:
                item = Item(content = numnew[0 : numnew.index('/')], inventory = 0)
            db.session.add(item)
            db.session.commit()
            numnew = numnew[numnew.index('/') + 1:]
            break
    return redirect(url_for('donate'))


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("base.html", items=Item.query.all())

    if request.method == "POST":
        for i in Item.query.all(): # in all of the food data
            if (i.content != "test food"): # other than "test food" because there's a space in its name
                if (request.form[i.content] != i.content): # we want the textform that was changed to the number to be withdrawn
                    i.inventory = i.inventory + int(request.form[i.content])
                    db.session.commit()
        numnew = str(request.form["numnew"])
        while ('/' in numnew):
            if (request.form[numnew[0 : numnew.index('/')]].isnumeric()):
                print("sldkjfslkdjf " + numnew[0 : numnew.index('/')])
                item = Item(content = numnew[0 : numnew.index('/')], inventory = int(request.form[numnew[0 : numnew.index('/')]]))
            else:
                item = Item(content = numnew[0 : numnew.index('/')], inventory = 0)
            db.session.add(item)
            db.session.commit()
            numnew = numnew[numnew.index('/') + 1:]
            break
    return redirect(url_for('test'))
