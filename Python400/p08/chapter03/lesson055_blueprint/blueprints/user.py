from flask import Blueprint


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/<int:_id>')
def user(_id):
    return f'user {_id}.'
