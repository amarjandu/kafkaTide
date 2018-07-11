from kafka import KafkaProducer
from kafka.errors import KafkaError
import urllib.request,bouyData


#producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
topic = 'tideData'

cleanIDsFile = open('./config/cleanStationID','r')
cleanIDs = []

for line in cleanIDsFile:
        cleanIDs.append(line)
cleanIDsFile.close()

for ids in cleanIDs:
        temp = bouyData.bouyData(ids,False)
        temp.fetchUrl()
        print(temp.getJson())


    
    


