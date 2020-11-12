import config as cfg
import cx_Oracle

class Medico:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def insert(self):
        # construct an insert statement that add a new row to the billing_headers table
        sql = ('insert into medico(self.id, self.nome) '
               'values(:self.id, :self.nome)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql, [self.id, self.nome])
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)

