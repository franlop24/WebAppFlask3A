from flask import Blueprint, render_template

error_views = Blueprint('error', __name__)

@error_views.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html')