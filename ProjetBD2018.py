from flask import Flask, render_template, request, redirect, abort
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'projetbduser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gUPqV1qOGG4jVcn4Ab8uuPeiCV42Pm4N4Eh1hJ7SUVctzeH7cbep1EMRUVmUGNnv'
app.config['MYSQL_DATABASE_DB'] = 'ProjetBD'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    cursor.execute('''SELECT id, nom FROM Biere''')
    bieres = cursor.fetchall()
    n = request.args.get("n")
    return render_template('index.html', name=name, bieres=bieres, id=n)


@app.route('/login', methods=['GET'])
def afficher_login():
    print('afficher login')
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    pwd = request.form['password']

    print(request.form['username'])
    print(pwd) # hehehe
    print(request.form['remember'])
    if pwd == "FindMyPassword":
        return redirect("/", code=302)
    abort(401)


@app.errorhandler(401)
def error(e):
    return render_template("error.html"), 401


if __name__ == '__main__':
    app.run() #debug=True
