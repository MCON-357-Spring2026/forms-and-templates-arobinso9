from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        if not name or name.strip() == "":
            error = "Username is required."
            username = None
        # 2. Validate grade is number
        if not grade or not grade.isnumeric():
            error = "Grade is required."
        # 3. Validate grade range 0–100
        grade_numeric = int(grade)
        if grade_numeric < 0 or grade_numeric > 100:
            error = "Grade must be between 0 and 100."
        else:
            # 4. Add to students list as dictionary
            students.append({"name": name, "grade": grade_numeric})
            # 5. Redirect to /students
            return redirect(url_for("view_students"))

    return render_template("add.html", error=error, name=name, grade=grade)

# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    # - average grade
    # - highest grade
    # - lowest grade

    return render_template("summary.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
