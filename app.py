from api.categoria_api import CategoriaApi
from api.hello_api import HelloWorld
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource, Api 


app=Flask(__name__)
mysql = MySQL(app)
api = Api(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootcodigo'
app.config['MYSQL_DB'] = 'myblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def index():
    
    cur = mysql.connection.cursor()
    return "hello world"

class PostCategoriaApi(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute('''
           SELECT p.titulo, c.nombre
FROM myblog.post as p
LEFT JOIN myblog.categoria as c
ON p.idcategoria = c.idcategoria
WHERE p.idcategoria = ''' + id)
        result = cur.fetchall()
        return str(result)
    
class CategoriaApi(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM categoria")
        result = cur.fetchall()
        return str(result)
    
class PostApi(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM post")
        result = cur.fetchall()
        return str(result)
    
api.add_resource(HelloWorld, '/hello')
api.add_resource(CategoriaApi, '/categoria')
api.add_resource(PostApi, '/post')
api.add_resource(PostCategoriaApi,'/categoria/<id>/post')

    