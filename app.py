from flask import Flask,render_template
app = Flask(__name__)

movies= [
    {"title":"Iron Man",
     "genre":"Sci-fi",
     "rating":"9.2"},

     {"title":"Alive",
     "genre":"Zombie Thriller",
     "rating":"8.9"},

     {"title":"Obsession",
     "genre":"Horror-Thriller",
     "rating":"9.0"}
]

@app.route("/")
def home():
    name = "Nandini"
    return render_template("home.html", name=name, movies=movies)

@app.route("/movies")
def movie_page():
    return render_template("movies.html",movies=movies) 

@app.route("/movies/<title>")  
def movie_details(title):
    for movie in movies:
        if movie["title"]==title:
            return render_template("movie.html",movie=movie)
    return "Movie not found"

if  __name__=="__main__":
    app.run(debug=True)
