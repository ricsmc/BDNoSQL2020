import config as cfg
import cx_Oracle

class Bloodpress:

    def __init__(self, id, systolic, diastolic):
        self.systolic = systolic
        self.diastolic = diastolic

    def insert(self):

        # construct an insert statement that add a new row to the billing_headers table
        sql = ('insert into medico(self.id, self.systolic, self.diastolic) '
               'values(:self.id,:self.systolic,:self.diastolic)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql, [self.id, self.systolic, self.diastolic])
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)
