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

    return render_template('customer/create.html')





