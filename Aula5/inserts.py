import config as cfg
import cx_Oracle

def insert_bloodpress(id_bloodpressure,systolic, diastolic):
    """
        Insert a row to the billing_headers table
        :param systolic:
        :param diastolic:
        :param id_bloodpressure:
        :return:
        """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into medico(id_bloodpressure,systolic, diastolic) '
           'values(:id_bloodpressure,:systolic,:diastolic)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                               cfg.password,
                               cfg.dsn,
                               encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [id_bloodpressure,systolic, diastolic])
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)

def insert_medicos(medicos):
    for i in medicos:
        insert_medico(i['id'],i['nome'])

def insert_medico(id_medico, nome_medico):
    """
    Insert a row to the billing_headers table
    :param id_medico:
    :param nome_medico:
    :return:
    """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into medico(id_medico, nome_medico) '
        'values(:id_medico,:nome_medico)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [id_medico, nome_medico])
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


def insert_paciente(id_paciente, nome_paciente, d_nasc, age_paciente):
    """
    Insert a row to the billing_headers table
    :param id_paciente:
    :param nome_paciente:
    :param d_nasc:
    :param age_paciente:
    :return:
    """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into paciente(id_paciente, nome_paciente, d_nasc, age_paciente) '
        'values(:id_paciente, :nome_paciente, :d_nasc, :age_paciente)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [id_paciente, nome_paciente, d_nasc, age_paciente])
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


def insert_sensor(number_of_sensors,sensorid,sensornum,type_of_sensor,patient,servicecod,servicedesc,amddate,bed,bodytemp,bloodpress,bpm,sato2,timestamp,careteam):
    """
        Insert a row to the billing_headers table
        :param number_of_sensors:
        :param sensorid:
        :param sensornum:
        :param type_of_sensor:
        :param patient:
        :param servicecod:
        :param servicedesc:
        :param amddate:
        :param bed:
        :param bodytemp:
        :param bloodpress:
        :param bpm:
        :param sato2:
        :param timestamp:
        :param careteam:
        :return:
        """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into paciente(number_of_sensors,sensorid,sensornum,type_of_sensor,patient,servicecod,servicedesc,amddate,bed,bodytemp,bloodpress,bpm,sato2,timestamp,careteam) '
           'values(:number_of_sensors,:sensorid,:sensornum,:type_of_sensor,:patient,:servicecod,:servicedesc,:amddate,:bed,:bodytemp,:bloodpress,:bpm,:sato2,:timestamp,careteam)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                               cfg.password,
                               cfg.dsn,
                               encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [number_of_sensors,sensorid,sensornum,type_of_sensor,patient,servicecod,servicedesc,amddate,bed,bodytemp,bloodpress,bpm,sato2,timestamp,careteam])
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)