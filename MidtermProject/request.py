#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9090/predict'

water_id = 'water_potability'
water = {'ph':'5.400301780729467',
    'hardness':'198.76735125945606',
    'solids':'21167.500098968772',
    'chloramines':'10.056852484033495',
    'sulfate':'323.5963490101317',
    'conductivity':'444.47888250689795',
    'organic_carbon':'11.256381166909478',
    'trihalomethanes':'79.84784281372556',
    'turbidity':'4.528522696326911'}

response = requests.post(url, json=water).json()
print('Water potability predicted : %f' % response['water_potability'])

