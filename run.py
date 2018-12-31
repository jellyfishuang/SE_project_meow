from flask import Flask, render_template, request
from  controller.home import home
from  controller.login import login
from  controller.title import title
from  controller.lottery import lottery
#from views.Board import Board


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(title)
app.register_blueprint(lottery)
@app.route('/')
def router():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
