import config as cfg
import cx_Oracle

class Paciente:

    def __init__(self, id, nome, data, idade):
        self.id = id
        self.nome = nome
        self.data = data
        self.idade = idade

    def insert(self):

        # construct an insert statement that add a new row to the billing_headers table
        sql = ('insert into paciente(self.id, self.nome, self.data, self.idade) '
               'values(:self.id, :self.nome, :self.data, :self.idade)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql, [self.id, self.nome, self.data, self.idade])
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)
