from flask import Flask, render_template, request
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'ProjetBD'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    # cursor.execute('''SELECT * FROM test''')
    # data = cursor.fetchall()
    n = request.args.get("n")
    data = [["IPA", "IPA du nord est"], ["Blanche", "Blanche de Chambly"]]
    return render_template('index.html', name=name, data=data, id=n)


if __name__ == '__main__':
    app.run()
