import psycopg2
import utils

class storage():

    def __init__(self, connection_string):
        self.conn_string = connection_string

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
            except psycopg2.DatabaseError, e:
                utils.log_warning("Database connect failed. Exception: " + str(e))

        utils.log_error("Database connect failed after trying for %d times." % retry)
        self.close()
        self.connect()

        raise Exception("Failed to get cursor")
