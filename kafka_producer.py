from kafka import KafkaProducer
from kafka.errors import KafkaError
import urllib.request,bouyData , pprint, msgpack


producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],value_serializer=msgpack.dumps)
topic = 'tideData'

cleanIDsFile = open('./config/cleanStationID','r')
cleanIDs = []

def getData():
        for ids in cleanIDs:
                temp = bouyData.bouyData(ids,False)
                if temp.fetchUrl() == -1:
                        print('removing ' + ids )
                        cleanIDs.remove(ids)         
                else:
                        pprint.pprint(temp.getJson())
                        producer.send('tideData',value=temp.getJson())
                writeToFile('./config/availableStations',cleanIDs)

def writeToFile(fileString,list):
        with open(fileString, mode='wt',encoding='utf-8') as writeFile:
                writeFile.write('\n'.join(cleanIDs))
        writeFile.close
    
    
###
# Main Code here
# 
####
for line in cleanIDsFile:
        cleanIDs.append(line.strip())
cleanIDsFile.close()
# 
getData()





