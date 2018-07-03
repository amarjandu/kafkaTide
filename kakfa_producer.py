from kafka import KafkaProducer
from kafka.errors import KafkaError
import urllib.request


producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
topic = 'tideData'
noaaURL = 'https://tidesandcurrents.noaa.gov/api/datagetter?'
dataRequest = '&date=latest&format=json&time_zone=gmt&units=english'
cleanIDsFile = open('./config/cleanStationID','r')
cleanIDs = []

for line in cleanIDsFile:
        cleanIDs.append(line)
cleanIDsFile.close()

def getData(ids,outArray):
        tempURL = noaaURL+'station='+ ids.strip() + dataRequest
        waterLevelTemp = tempURL + '&product=water_level&datum=MTL'
        waterTemp = tempURL + '&product=water_temperature'
        windTemp = tempURL + '&product=wind'
        urlArray = [waterLevelTemp,waterTemp,windTemp]
        for urls in urlArray:
                requestData = urllib.request.urlopen(urls))


    
    


