import json
import urllib.request
import time
import medico
import careteam
import paciente
import bloodpress
import sensor

#http://nosql.hpeixoto.me/api/

# download raw json object
url = "http://nosql.hpeixoto.me/api/sensor/3001"
start_time = time.time()

# parse json object
while True:
    data = urllib.request.urlopen(url).read().decode()
    current_time = time.time()
    elapsed_time = current_time - start_time
    obj = json.loads(data)

    id_sensor = obj['sensorid']
    id_blood = 1

    pac = obj['patient']
    paciente = paciente.Paciente(pac['patientid'], pac['patientname'], pac['patientbirthdate'], pac['patientage'])
    paciente.insert()

    blood = obj['bloodpress']
    bloodpress = bloodpress.Bloodpress(id_blood, blood['systolic'], blood['diastolic'])
    bloodpress.insert()

    medicos = obj['careteam']
    for i in medicos:
        medico = medico.Medico(medicos[i]['id'], medicos[i]['nome'])
        medico.insert_medico()
        careteam = careteam.Careteam(medico.id, id_sensor)

    sensor = sensor.Sensor(obj['sensorid'], obj['sensornum'], obj['number_of_sensors'], obj['type_of_sensor'],
                           obj['servicecod'],
                           obj['servicedesc'], obj['admdate'], obj['bed'], obj['bodytemp'], obj['bpm'], obj['sato2'],
                           obj['timestamp'], id_blood, paciente.id)
    sensor.insert()

    id_blood += 1

    # output some object attributes
    print('Inserted\n')
    if elapsed_time > 120:
        print('--------BREAK--------')
        break
    else:
        time.sleep(5)
