from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""
    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            result = eval(expression)  # ⚠️ For demo only (avoid eval in production)
        except:
            result = "Error"
    return render_template("index.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
