from flask import Flask, render_template, request

app =  Flask(__name__)

shopping_list=['milk', 'eggs']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shopping_list.append( request.form['item'])
    return  render_template('index.html', items =shopping_list)

if __name__ == '__main__':
    app.run(debug=True)

