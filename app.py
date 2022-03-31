# !pip install Flask flask-mongoengine
from flask import *
from flask_mongoengine import MongoEngine
from config import DB_URI

app = Flask(__name__)
app.config["MONGODB_HOST"] = DB_URI
db = MongoEngine(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", movies=Movie.objects())

@app.route("/delete/<id>")
def delete_fun(id):
    movie = Movie.objects.get_or_404(id=id)
    movie.delete()
    return redirect("/")

@app.route("/update/<id>", methods=["POST", "GET"])
def updatepage(id):
    if request.method == "POST":
        body = request.form.to_dict()
        if not isinstance(body['cast'], list):
            body["cast"] = body["cast"].split(",")
        movie = Movie.objects(id=id).first()
        movie.update(**body)
        return redirect("/")
    movie = Movie.objects(id=id).first()
    return render_template("update.html", movie=movie)

@app.route("/add", methods=["POST"])
def add_movie_input():
    if request.method == "POST":
        body = request.form.to_dict()
        if not isinstance(body['cast'], list):
            body['cast'] = body['cast'].split(",")
        movie = Movie(**body)
        movie.save()
        return redirect("/")

#REST API
@app.route("/api/movies")
def movies():
    objs = Movie.objects()
    return jsonify(objs), 200

@app.route("/api/movies/add", methods=["POST"])
def add_movie():
    body = request.json
    if not isinstance(body["cast"] , list):
        body["cast"] = body['cast'].split(",")
    movie = Movie(**body)
    movie.save()
    return jsonify("{'id', %s}" % movie.id), 201

@app.route("/api/movies/<id>", methods=["PUT", "DELETE", "GET"])
def single_movie(id):
    movie = Movie.objects.get_or_404(id=id)
    if request.method == "GET":
        return jsonify(movie), 200
    elif request.method == "PUT":
        body = request.json
        if "cast" in body and not isinstance(body["cast"], list):
            body["cast"] = body['cast'].split(",")
        movie.update(**body)
        return "", 204
    elif request.method == "DELETE":
        movie.delete()
        return "", 204



class Movie(db.Document):
    name = db.StringField()
    director = db.StringField()
    cast = db.ListField()
    year = db.IntField()
    rated = db.FloatField()

if __name__ == "__main__":
    app.run(debug=True)
