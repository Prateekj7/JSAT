from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

obp = Blueprint('order', __name__)

@obp.route('/')
def index():
    db = get_db()
    orders = db.execute(
        'SELECT o.id, c.name, orderDate, o.price'
        ' FROM customer_purchase o JOIN customer c ON o.customer_id = c.id'
        ' ORDER BY orderDate DESC'
    ).fetchall()
    return render_template('order/index.html', orders=orders)

@obp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        orderDate = request.form['orderDate']
        price = request.form['price']
        error = None

        if not customer_id:
            error = 'Customer is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO customer_purchase (orderDate, customer_id, price)'
                ' VALUES (?, ?, ?)',
                (orderDate, customer_id, price)
            )
            db.commit()
            return redirect(url_for('order.index'))

    return render_template('order/create.html')

def get_order(id):
    order = get_db().execute(
        'SELECT o.id, orderDate, customer_id, price'
        ' FROM customer_purchase o '
        ' WHERE o.id = ?',
        (id,)
    ).fetchone()

    if order is None:
        abort(404, "Order id {0} doesn't exist.".format(id))

    return order

@obp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    order = get_order(id)

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        orderDate = request.form['orderDate']
        price = request.form['price']
        error = None

        if not customer_id:
            error = 'Customer is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE customer_purchase SET orderDate = ?, customer_id = ?, price = ?'
                ' WHERE id = ?',
                (orderDate, customer_id, price, id)
            )
            db.commit()
            return redirect(url_for('order.index'))

    return render_template('order/update.html', order=order)

@obp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_order(id)
    db = get_db()
    db.execute('DELETE FROM customer_purchase WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('order.index'))





