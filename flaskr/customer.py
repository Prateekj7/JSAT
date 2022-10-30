import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

cb = Blueprint('customer', __name__, url_prefix='/customer')

@cb.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        lastPurchase = request.form['lastPurchase']
        db = get_db()
        error = None

        if not name:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif db.execute(
            'SELECT id FROM customer WHERE name = ?', (name,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO customer (name, email, phone, lastDateOfPurchase) VALUES (?, ?, ?, ?)',
                (name, email, phone, lastPurchase)
            )
            db.commit()
            return redirect(url_for('customer.register'))

        flash(error)

    return render_template('customer/register.html')


