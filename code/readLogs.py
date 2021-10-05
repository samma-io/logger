import os
import json
from sammaParser import logger

file = os.getenv('FILE', 'tsunami-output.json')


#Json file Tsunami
#Read the file and send line by line to the samma parser
f = open("/out/{0}".format(file), "r")
json_file = json.load(f)
statusJson={}
statusJson['scanStatus']=json_file['scanStatus']
logger(statusJson)
for target in json_file["reconnaissanceReport"]["targetInfo"]["networkEndpoints"]:
    logger(target)

for target in json_file["reconnaissanceReport"]["networkServices"]:
    logger(target)