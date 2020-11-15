import config as cfg
import cx_Oracle

class Sensor:

    def __init__(self, id, num_sensor, n_of_sensors, type_of_sensor, service_cod, service_desc, admdate, bed, bodytemp, bpm, sato2, timestamp, id_blood, id_pac):
        self.id = id
        self.num_sensor = num_sensor
        self.n_of_sensors = n_of_sensors
        self.type_of_sensor = type_of_sensor
        self.service_cod = service_cod
        self.service_desc = service_desc
        self.admdate = admdate
        self.bed = bed
        self.bodytemp = bodytemp
        self.bpm = bpm
        self.sato2 = sato2
        self.timestamp = timestamp
        self.id_blood = id_blood
        self.id_pac = id_pac

    def insert(self):

        # construct an insert statement that add a new row to the billing_headers table
        sql = ('insert into sensor(self.id,self.num_sensor,self.n_of_sensors,self.type_of_sensor,self.service_cod,self.service_desc,self.admdate,'
               'self.bed,self.bodytemp,self.bpm,self.sato2,self.timestamp,self.id_blood, self.id_pac) '
               'values(:self.id,:self.num_sensor,:self.n_of_sensors,:self.type_of_sensor,:self.service_cod,:self.service_desc,:self.amddate,'
               ':self.bed,:self.bodytemp,:self.bpm,:self.sato2,:self.timestamp,:self.id_blood,:self.id_pac)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql, [self.id, self.num_sensor, self.n_of_sensors, self.type_of_sensor, self.service_cod, self.service_desc,
                                         self.admdate, self.bed, self.bodytemp, self.bpm, self.sato2, self.timestamp, self.id_blood,self.id_pac])
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)
