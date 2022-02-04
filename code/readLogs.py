import os
import json
import time

from sammaParser import logger

file = os.getenv('FILE', 'tsunami-output.json')
parser = os.getenv('PARSER', 'tsunami')


import os.path

#Wait to file is there
FileIsNotThere = True
while FileIsNotThere:
    if os.path.isfile("/out/{0}".format(file)):
        print ("File is found /out/{0}".format(file))
        #give time so file is complete
        time.sleep(10)
        FileIsNotThere = False
    else:
        print ("Wait for file /out/{0}".format(file))
        time.sleep(10)

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