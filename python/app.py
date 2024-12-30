from flask import Flask , request, render_template , flash , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Update these values according to your MySQL setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python_user:HOODQUAN67@localhost/python_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(100), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   
   def __repr__(self):
      return f"<User {self.username}>"


# CRUD FUNCTIONS
def create_user(username ,email):
   new_user = User(username=username, email=email)
   db.session.add(new_user)
   db.session.commit()
def get_all_users():
   return User.query.all()

def get_user_by_id(id):
   return User.query.get(id)

def update_username_by_id(user_id, new_username):
   user = get_user_by_id(user_id)
   if user:
      user.username = new_username
      db.session.commit()
def delete_user_by_id(user_id):
   user = get_user_by_id(user_id)
   if user:
      db.session.delete(user)
      db.session.commit()


app.secret_key = "secret"

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/contact-us", methods=["GET", "POST"])
def contact():
    method = request.method
    if method == "GET":
       return render_template("contact.html")
    name = request.form.get("name")
    subject = request.form.get("subject")
    message = request.form.get("message")

    if not name or not subject or not message:
       flash("Provide all fields", "error")
       return redirect(url_for("contact"))
    flash("Success!! All fields submitted", "success")   
    return redirect(url_for("contact"))

@app.route("/blog/<id>")
def blog(id):
   return f"id is {id}"

@app.route("/account")
def account():
   if "version" in request.args:
     version = request.args.get("version")
     return f"The version is {version}"
   else:
      return "input version"

@app.route("/submit", methods=["GET","POST"])
def submit():
   method = request.method
   if method == "GET":
      return "User call with GET"
   elif method == "POST":
      return "User call with POST"

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
  app.run(debug=True)
