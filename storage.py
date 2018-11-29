import psycopg2
import utils
from models import ExpenseRecord, Account

class storage():

    def __init__(self, connection_string):
        self.conn_string = connection_string
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(self.conn_string)

    def close(self):
        if self.connection != None:
            self.connection.close()

    def get_cursor(self, retry = 5):

        """ Should we explicit close a cursor: https://stackoverflow.com/questions/24661754/necessity-of-explicit-cursor-close """

        while retry > 0:

            retry = retry - 1

            try:
                if self.connection != None:
                    return self.connection.cursor()
            except psycopg2.DatabaseError as e:
                utils.log_warning("Database connect failed. Exception: " + str(e))
            self.close()
            self.connect()

        utils.log_error("Database connect failed after trying for %d times." % retry)

        raise Exception("Failed to get cursor")

    def get_expense_records_by_daterange(self, user_id, start_time, end_time):

        cursor = self.get_cursor()
        cursor.execute(
            """SELECT id, user_id, from_account, to_account, amount, description, transaction_time, created_time FROM ExpenseRecords WHERE user_id = '%s' AND transaction_time >= '%s' AND transaction_time <= '%s' """
            % (user_id, start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"))
        )

        result = cursor.fetchall()

        return list(map(lambda x: ExpenseRecord(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]), result))

    def get_accounts_by_user_id(self, user_id):

        cursor = self.get_cursor()
        cursor.execute(
            """SELECT id, user_id, display_name, balance FROM Accounts WHERE user_id = '%s' """
            % (user_id, )
        )

        result = cursor.fetchall()

        account_list = list(map(lambda x: Account(x[0], x[1], x[2], x[3]), result))

        return dict(zip(map(lambda x: x.id, account_list), account_list))

s = storage("""dbname='postgres' user='SakuyaPgSqlAdmin@sakuya-pgsql-int' host='sakuya-pgsql-int.postgres.database.azure.com' password='asdfGHJK1234!@#$' port='5432'""")

import datetime
from datetime import timedelta

s.connect()
print (s.get_accounts_by_user_id('00000000-0000-0000-0000-000000000001'))
# s.get_expense_records_by_daterange('00000000-0000-0000-0000-000000000001', datetime.datetime.now() - timedelta(days=1), datetime.datetime.now() + timedelta(days=1))
