import methods
from flask import Flask
from flask import render_template
from flask import request
app =Flask(__name__)


@app.route('/',methods = ["GET","POST"])
def home1():
    locations = methods.all_locations()
    types = methods.all_types()
    industries = methods.all_industries()
    return render_template("index.html",locations= locations,types=types,industries = industries)

@app.route('/result_table',methods = ["GET","POST"])
def home2():
    if request.method =="POST":
        location = request.form.get("location")
        rating  = request.form.get("rating")
        ty = request.form.get("type")
        industry = request.form.get("industry")
        if not location:
            location = "all"
        if not rating :
            rating = "all"
        if not ty:
            ty = "all"
        if not industry:
            industry = "all"
        data = methods.search(location,rating,ty,industry).to_csv().split("\n")
    if len (data) >2:
        return render_template("result_table.html",data = data)
    else:
        return render_template("result_table.html",data = None)


@app.route('/result_visualize',methods = ["GET","POST"])
def home3():
    if request.method =="POST":
        location = request.form.get("location")
        rating  = request.form.get("rating")
        ty = request.form.get("type")
        industry = request.form.get("industry")
        if not location:
            location = "all"
        if not rating :
            rating = "all"
        if not ty:
            ty = "all"
        if not industry:
            industry = "all"
        data = methods.search(location,rating,ty,industry)
    if len(data) > 2:
        methods.img1(data)
        methods.img2(data)
        return render_template("result_visualize.html",data = True)
    else:
        return render_template("result_visualize.html",data = False)

app.run(host = "localhost",port = 5001, debug = True)