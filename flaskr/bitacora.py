from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('bitacora', __name__)

@bp.route('/')
def index():
    db = get_db()
    bitacora = db.execute(
        'SELECT bit.id, id_mensaje, fecha, accion'
        'from bitacora bit JOIN user u ON bit.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('bitacora/index.html', bitacora = bitacora)

    