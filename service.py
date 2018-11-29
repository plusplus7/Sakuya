#! -*- coding=utf-8 -*-
import datetime
from datetime import timedelta
import uuid
import utils
import flask
import sys
from flask import request
import storage
from dateutil.relativedelta import relativedelta

FlaskApp = flask.Flask(__name__, template_folder='statics/templates')

if len(sys.argv) == 1:
    FlaskApp.debug = True
    FlaskApp.secret_key = 'development'
    data = storage.storage("""localhost""")

else:
    data = storage.storage(sys.argv[2])

@FlaskApp.route('/')
def Homepage():

    """Render the home page."""

    return flask.render_template('homepage.html',
        title       = "home",
    )

@FlaskApp.route('/dashboard', methods=['GET', 'POST'])
def ExpenseDashboard():

    user_id = "00000000-0000-0000-0000-000000000001"

    start_time = datetime.datetime.now() - relativedelta(months=1)
    end_time = datetime.datetime.now()

    start_time_str = request.args.get('start_time')
    end_time_str = request.args.get('end_time')

    if start_time_str != None and end_time_str != None:
        start_time = utils.parse_time(start_time_str)
        end_time = utils.parse_time(end_time_str)

    expense_records = data.get_expense_records_by_daterange(user_id, start_time, end_time)
    account_dict = data.get_accounts_by_user_id(user_id)

    return flask.render_template('/dashboard.html',
        title           = "dashboard",
        start_time      = start_time,
        end_time        = end_time,
        account_dict    = account_dict,
        expenses        = expense_records,
        utils           = utils
        )

if __name__ == '__main__':
    FlaskApp.run()
