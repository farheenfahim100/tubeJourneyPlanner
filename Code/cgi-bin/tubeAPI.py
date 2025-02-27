import requests, json, cgi, cgitb, shutil, glob, os # Import modules which will be used later in the program.

# Objective 3.3:

class Tube_API(): # Creates a class for the tube API.
    
    def get_data(self,url): # Creates a method called "get_data" which takes a single argument which is the endpoint/url the data is being accessed from. 
        response = requests.get(url, timeout=10) # Uses "get" method in the "requests" module to access/GET the webpage corresponding to the "url" parameter.
        if response.status_code >= 400: # If statement: if the status_code from the previous line is greater than or equal to 400, this means that there was an error, so run the following line.
            raise RuntimeError(f'Request failed: { response.text }') # Handling the error: If there is an error, the user will know as this message will be output.
        return response.json() # Return the information/data which was accessed from the API as json content.

    def get_station_id(self,station): # Creates a method called "get_station_id" which takes a single argument which is the station the user is requesting data on. 
        endpoint = "https://api.tfl.gov.uk/Stoppoint/Search/?query=" + station + "&modes=tube&app_key=61cab23336c147e29c64f5de382d1d91" # The variable called "endpoint" stores the string which is the url for accessing the API information.
        data = self.get_data(endpoint) # Calls the "get_data" method within the class with the argument "endpoint", the value returned is stored using the identifier called "data".
        info = data["matches"] # Stores the value corresponding to the "matches" key in the dictionary called "data" using the identifier called "info".
        info = info[0] # 
        ID = info["id"] # Stores the value corresponding to the "id" key in the dictionary called "info" using the identifier called "ID".
        ICSCODE = info["icsId"] # Stores the value corresponding to the "icsID" key in the dictionary called "info" using the identifier called "ICSCODE".
        return ID, ICSCODE # Returns the unique TfL station codes for the station the user has inputted. This is used to identify which station the information is about in the API.
