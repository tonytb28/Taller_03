from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('mensaje', __name__)


@bp.route('/')
def index():
    db = get_db()
    mensaje = db.execute(
        'SELECT mens.id, id_emisor, id_receptor, titulo, mensaje, enviado, recibido'
        'from mensajes mens JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('mensaje/index.html', mensaje = mensaje)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        Titulo = request.form['titulo']
        mensaje = request.form['mensaje']
        error = None

        if not Titulo: 
            error = 'Titulo requerido'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO mensajes (id_emisor, id_receptor, titulo, mensaje, enviado, receptor'
                'VALUES (?,?,?,?,?,?)',
                (id_emisor, id_receptor, Titulo, mensaje, enviado, recibido,  g.user['id'])
            )
            db.commit()
            return redirect(url_for('mensaje.index'))

        return render_template('mensaje/create.html')


def get_mensaje(id.id_emisor=True):
    mensaje = get_db().execute(
        'SELECT mens.id, id_emisor, id_receptor, titulo, mensaje, enviado, recibido'
        'FROM mensaje mens JOIN user u ON p.author_id = u.id'
        'WHERE p.id = ?',
        (id)
    ).fetchone()

    if mensaje is None:
        abort(404, "Mensaje id {0} no existe.".format(id))

    if id_emisor and mensaje['id_emisor'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update',methods=('GET', 'POST'))
@login_required
def update(id):
    mensaje = get_mensaje(id)

    if request.method == 'POST':
        Titulo = request.form['titulo']
        mensaje = request.form['mensaje']
        error = None

         if not Titulo:
            error = 'Titulo requerido.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE mensaje SET titulo = ?, mensaje = ?'
                ' WHERE id = ?',
                (Titulo, mensaje, id)
            )
            db.commit()
            return redirect(url_for('mensaje.index'))

    return render_template('mensaje/update.html', mensaje=mensaje)


@bp.route('/<int:id>/delete', methods= ('POST',))
@login_required
def delete(id):
    get_mensaje(id)
    db = get_db()
    db.execute('DELETE FROM mensaje WHERE id = ?', (id))
    db.commit()
    return redirect(url_for('mensaje.index'))
        