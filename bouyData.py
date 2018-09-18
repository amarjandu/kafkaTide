import time, urllib.request , json, pprint

class bouyData:
    noaaURL = 'https://tidesandcurrents.noaa.gov/api/datagetter?'
    dataRequest = '&date=latest&format=json&time_zone=gmt&units=english' 
    epoch_time = time.time()
    url = None
    data = {}
    def __init__(self,id,fetch=False):
        if id:
            self.id = id.strip()
            tempURL = self.noaaURL+'station='+ self.id + self.dataRequest
            waterLevelTemp = tempURL + '&product=water_level&datum=MTL'
            waterTemp =  tempURL + '&product=water_temperature' 
            windTemp = tempURL + '&product=wind'
            self.urlDict = {'waterLevelTemp':waterLevelTemp,'waterTemp':waterTemp,'windTemp':windTemp}
            if fetch == True:   
                self.fetchUrl()
        
    def fetchUrl(self):
        if len(self.urlDict) > 0:
            for  url in self.urlDict:
                if url != None:
                    try:
                        # dont know how to have
                        self.data[url] = json.loads(urllib.request.urlopen(self.urlDict[url]).read().decode("utf-8"))
                        if 'error' in self.data[url]:
                            print('error hit')
                            return -1
                        self.error = None
                    except urllib.error.URLError:
                        self.requestData = None
                        self.error = urllib.error.URLError

    def getJson(self):
        if len(self.data) > 0:
            return {json.dumps({self.id:self.data})}
