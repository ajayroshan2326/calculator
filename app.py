from flask import Flask, render_template, request

app = Flask(__name__)

# Basic calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    error = None

    if request.method == "POST":
        expression = request.form.get("expression", "")
        button = request.form.get("button")

        if button == "C":
            expression = ""
        elif button == "=":
            try:
                if '+' in expression:
                    num1, num2 = expression.split('+')
                    result_value = add(float(num1), float(num2))
                    expression = str(result_value)
                elif '-' in expression:
                    num1, num2 = expression.split('-')
                    result_value = subtract(float(num1), float(num2))
                    expression = str(result_value)
                elif '*' in expression:
                    num1, num2 = expression.split('*')
                    result_value = multiply(float(num1), float(num2))
                    expression = str(result_value)
                elif '/' in expression:
                    num1, num2 = expression.split('/')
                    result_value = divide(float(num1), float(num2))
                    expression = str(result_value)
                else:
                    error = "Invalid Expression. Include an operator."
            except:
                error = "Invalid input. Please enter valid numbers."
        else:
            expression += button

    return render_template("index.html", expression=expression, error=error)

if __name__ == "__main__":
    app.run(debug=True)
