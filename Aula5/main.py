#!/usr/bin/env python
# coding: utf-8

# In[31]:


import json
import urllib.request
import time
import inserts


# download raw json object
url = "http://nosql.hpeixoto.me/api/sensor/3001"
start_time = time.time()

# parse json object
while True:
    data = urllib.request.urlopen(url).read().decode()
    current_time = time.time()
    elapsed_time = current_time - start_time
    obj = json.loads(data)
    bloodpr = obj['bloodpress']
    paciente = obj['patient']
    id = 1

    inserts.insert_paciente(paciente['patientid'], paciente['patientname'],paciente['patientbirthdate'], paciente['patientage'])
    inserts.insert_medicos(obj['careteam'])
    inserts.insert_bloodpress(id,bloodpr['systolic'],bloodpr['diastolic'])
    id += 1

    # output some object attributes
    print('Blood Pressure : \n\t-Systolic: ' + str(bloodpr['systolic']) + '\n\t-Diastolic: ' + str(bloodpr['diastolic']))

    print('BPM : ' + str(obj['bpm']))
    if elapsed_time > 120 :
        print('--------BREAK--------')
        break
    else: time.sleep(5)


