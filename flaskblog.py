from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Ryan Guide',
        'title': 'Post 1',
        'content': 'First post',
        'date_posted': 'August 10, 2020'
    },
    {
        'author': 'Trask Ulgo',
        'title': 'Endar Spire',
        'content': 'Oh boy I hope no dark Jedi are aboard',
        'date_posted': 'August 1, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)