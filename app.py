from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/test')
def test():
    msg = 'Congratulations. You have discovered the secret page.'
    return render_template('test.html', title="Test", message=msg)


if __name__ == '__main__':
    app.run(debug=False)
