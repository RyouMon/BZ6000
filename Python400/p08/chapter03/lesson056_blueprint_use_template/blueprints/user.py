from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@user_bp.route('/<int:_id>')
def user(_id):
    try:
        return render_template('%s.html' % _id)
    except TemplateNotFound:
        abort(404)
