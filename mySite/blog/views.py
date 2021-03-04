from flask import render_template, Blueprint

bp = Blueprint("blog", __name__)


@bp.route('/blog')
def blog():
    return render_template('blog/blog.html')
