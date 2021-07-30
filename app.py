from flask import Flask, jsonify, render_template, request
import sqlite3
from tempfile import mkdtemp


app = Flask(__name__)
app.debug=True
# Ensure templates are autoreloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/search-courses")
def search_page():
    return render_template("index.html")


@app.route("/course")
def course():
    name = request.args.get("name")
    con = sqlite3.connect("catalog.db")
    db = con.cursor()
    result = db.execute("SELECT description, credit, isAP, isPreAp, grades, prerequisite FROM courses WHERE name=?", (name, )).fetchall()[0]
    con.commit()
    description = result[0]
    credit = result[1]
    isAp = result[2]
    isPreAp = result[3]
    grades = result[4].split(",")
    prerec = result[5]

    if isAp == "True":
        ctype = "  Advanced Placement"
    
    elif isPreAp == "True":
        ctype = "  Advanced (Pre-Ap)"
    
    else:
        ctype="  On-Level"
    return render_template("course.html", name=name, description=description, credit=credit, ctype=ctype, grades=grades, prerec=prerec)


@app.route("/learn-more")
def learn():
    return render_template("learn.html")

@app.route("/search")
def search():
    params = []
    started = False

    # Initialize Query
    query = "SELECT name FROM courses WHERE "

    # Get search from website and if it exists add it to query
    q = request.args.get("q")

    if q:
        query += "name LIKE ?"
        params.append("%" + str(q) + "%")
        started = True


    # Get grades from query and use to specify in the query
    ninth = request.args.get("ninth")
    tenth = request.args.get("tenth")
    eleventh = request.args.get("eleventh")
    twelveth = request.args.get("twelveth")

    

    # Get if user wants classes that are advanced and adding to query
    advanced = request.args.get("advanced")

    if advanced == "Yes":
        if started:
            temp = "AND "
        else:
            temp = ""
        query += temp + "isAP = \"True\" "
        started = True

    elif advanced == "No":
        if started:
            temp = "AND "
        else:
            temp = ""
        query += temp + "isAP = \"False\" "
        started = True



    # Get if user wants ap and adding that to query
    ap = request.args.get("ap")

    if ap == "Yes":
        if started:
            temp = "AND "
        else:
            temp = ""
        query += temp + "isPreAp = \"True\" "
        started = True

    elif ap == "No":
        if started:
            temp = "AND "
        else:
            temp = ""
        query += temp + "isPreAp = \"False\" "
        started = True
    
    # Gets if user wants prerec and adds to query
    prerec = request.args.get("prerec")

    if prerec:
        if started:
            temp = "AND "
        else:
            temp = ""
        if prerec == "yes":
            query += temp + "prerequisite != \"None\" "

        elif prerec == "no":
            query += temp + "prerequisite = \"None\" "


    # Gets amount of credits user wants and that to query
    credit = request.args.get("credit")

    if credit != "No Preference":
        query += "AND credit = ?"
        params.append(credit)
    

    grades = []
    if ninth:
        grades.append("9")

    if tenth:
        grades.append("10")
    
    if eleventh:
        grades.append("11")
    
    if twelveth:
        grades.append("12")
    
    if len(grades) > 0:
        temp = ""
        if started:
            temp = " AND ("
            temp2=")"
        else:
            temp = ""
            temp2 = ""
        
        started = True
        
        for i in range(len(grades)):
            if i == 0:
                query += temp + "grades LIKE ? "
            else:
                query += "OR grades LIKE ? "
            
            params.append("%" + str(grades[i]) + "%")
        query += temp2

    query += ";"

    print(query)
    if started:
        con = sqlite3.connect("catalog.db")
        db = con.cursor()
        results = db.execute(query, params).fetchall()
        con.commit()
        return jsonify(results)
    else:
        return jsonify([()])

