from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'movintarg'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/completedForm', methods=['POST'])
def completedForm():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comments cannot be greater than 120 characters!")
        return redirect('/')
    else:
        return render_template('form.html', name=name, location=location, language=language, comment=comment)

app.run(debug = True)