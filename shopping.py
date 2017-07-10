from flask import Flask, render_template, request, redirect, url_for

app =  Flask(__name__)

shopping_list=['milk', 'eggs']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shopping_list.append( request.form['item'])
    return  render_template('index.html', items =shopping_list)

@app.route('/remove/<name>')
def remove_item(name):
    global shopping_list
    shopping_list.remove(name)
    #after remove redirect to index action
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)

