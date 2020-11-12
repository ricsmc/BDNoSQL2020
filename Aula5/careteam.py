import config as cfg
import cx_Oracle

class Careteam:

    def __init__(self, id_medico, id_sensor):
        self.id_medico = id_medico
        self.id_sensor = id_sensor

    def insert(self):

        # construct an insert statement that add a new row to the billing_headers table
        sql = ('insert into medico(self.id_medico, self.id_sensor) '
               'values(:self.id_medico,:self.id_sensor)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql, [self.id_medico, self.id_sensor])
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)

