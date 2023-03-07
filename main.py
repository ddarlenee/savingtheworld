from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def index():
    with open('intro.txt', 'r') as file:
      message = file.read()
    data = None 
    numbers = [1,2,3,4,5]
    if request.method == "POST":
      data = request.form['whatever']
      with open('secret.txt', 'a') as file:
        file.write(data + "\n")
    return render_template('index.html', whatever = data, nums = numbers, intro = message)


app.run(host='0.0.0.0', port=81)
