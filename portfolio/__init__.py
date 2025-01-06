from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://deploy-habit-tracker-f04ab8cc5a90.herokuapp.com/"
    },
    {
        "name": "Zillow Web Scraping with Beautiful Soup, NumPy, Pandas",
        "thumb": "img/Houses.jpg",
        "hero": "img/ZillowGraph.png",
        "categories": ["python", "web"],
        "slug": "zillow_web_scraping",
        "prod": "https://github.com/Dfingerhut/ZillowDataProject"
    },
    {
        "name": "Indeed Web Scraping with Beautiful Soup, NumPy, Pandas",
        "thumb": "img/datascience.webp",
        "hero": "img/datascience-header.png",
        "categories": ["python", "web"],
        "slug": "indeed_web_scraping",
        "prod": "https://github.com/Dfingerhut/JobWebscraper"
    }

]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
