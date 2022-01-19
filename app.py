from flask import Flask, render_template, request
import predictor

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def appRoot():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        hrs = int(request.form["hrs"])
        marks = predictor.get_predicted_marks(hrs)
        err = ""
        if (hrs == None) or (hrs <0 or hrs>24):
            err = "invalid value for hours=" + str(hrs)
        return render_template("index.html", err=err, hrs=hrs, marks=marks+hrs)

if __name__ == "__main__":
    app.run(debug=False)
