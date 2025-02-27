import requests, json, cgi, cgitb, shutil, glob, os

class Tube_API():
    
    def get_data(self,url): 
        response = requests.get(url, timeout=10) 
        if response.status_code >= 400: 
            raise RuntimeError(f'Request failed: { response.text }')
        return response.json() 

    def get_station_id(self,station): 
        endpoint = "https://api.tfl.gov.uk/Stoppoint/Search/?query=" + station + "&modes=tube&app_key=61cab23336c147e29c64f5de382d1d91"
        data = self.get_data(endpoint)
        info = data["matches"] 
        info = info[0] 
        ID = info["id"] 
        ICSCODE = info["icsId"] 
        return ID, ICSCODE 
