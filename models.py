import uuid
import datetime
import utils

"""
    All the time in models should be:
        * A string in ISO 8601 format.
        * In UTC time zone.

    e.g. 1985-04-12T23:20:50.52
"""

class User():
    
    def __init__(self,
                 id,
                 display_name,
                 others,
                 register_time = datetime.datetime.utcnow()):

        self.id             = id
        self.display_name   = display_name
        self.others         = others
        self.register_time  = utils.format_time(register_time)

class ExpenseRecord():

    def __init__(self,
                 id,
                 user_id,
                 from_account,
                 to_account,
                 amount,
                 description = "",
                 transaction_time = datetime.datetime.utcnow(),
                 created_time = datetime.datetime.utcnow()):

        self.id                 = id
        self.user_id            = user_id
        self.from_account       = from_account
        self.to_account         = to_account
        self.amount             = amount
        self.description        = description
        self.transaction_time   = transaction_time
        self.created_time       = created_time

class Account():

    def __init__(self,
                 id,
                 user_id,
                 display_name,
                 balance):

        self.id = id
        self.user_id = user_id
        self.display_name = display_name
        self.balance = balance
