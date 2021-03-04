from flask import render_template, Blueprint

bp = Blueprint("site", __name__)


@bp.route('/')
def home():
    return render_template('site/home.html')


@bp.route('/about')
def about():
    return render_template('site/about.html')


@bp.route('/portfolio')
def portfolio():
    return render_template('site/portfolio.html')
