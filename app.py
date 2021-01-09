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

@app.route('/')
def index():
    return render_template("BDBI-pantry-web-interface.html", items=Item.query.all())

@app.route('/donation')
def donate():
    return render_template("BDBI-pantry-web-interface-donation.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("base.html", items=Item.query.all())

    item = Item(content=request.form["food_label"], inventory=request.form["food_num"])
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('test'))
