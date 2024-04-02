from flask import Flask, render_template, request

app = Flask(_name_)

def check_pass_fail(marks):
    # Assuming passing marks are 40
    pass_marks = 40
    result = []
    for mark in marks:
        if mark >= pass_marks:
            result.append("Pass")
        else:
            result.append("Fail")
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    marks = []
    for i in range(1, 7):
        marks.append(int(request.form[f'mark{i}']))
    results = check_pass_fail(marks)
    return render_template('result.html', marks=marks, results=results)

if _name_ == '_main_':
    app.run(debug=True)