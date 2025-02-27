import cgi, cgitb, shutil, glob, os # Import module which will be used later in the program.
import tubeAPI # Import class which will be used later in the program.

form = cgi.FieldStorage() # Data inputted from the form is stored so that it can be used later in the program.
station = form.getvalue('station_arrivals') # The station that the user inputted is accessed from the form and stored as the variable called "station".

# Print statements output as html lines:

print ("Content-type:text/html\n\n") # html line: defines content type so that the lines are processed and interpretted correctly by the computer.
print ("<html>") # html line: the <html> element for structuring the web page.
print ("<head>") # html line: the <head> element for structuring the web page.
print ("<title>Arrivals At Tube Stations</title>") # html line: the <title> element for distinguishing which page the user is on.
print("<link rel='stylesheet' type='text/css' href='/styles.css'>") # html line: references the file used for CSS styling of the webpage (objective 4.2).
print("<meta name='viewport' content='width=device-width, initial-scale=1'>") # html line: formats the webpage so that the content atomatically adjusts its size to fit the screen.
print ("</head>")  # html line: the closing </head> element for structuring the web page.

print("<body>") # html line: the <body> element for structuring the web page.
# Objective 3.1:
print("<div class='navbar'>") # html line: references the navbar div defined from the CSS file for structuring the web page (objective 4.1).
print("<a href='/journeyplanner.html'class='left'>Journey Planner</a>") # html line: the first part of the navbar is for the journey planner - when clicked, the website redirects to the html for the journey planner page.
print("<a href='/map.html'class='center'>Map</a>") # html line: the second part of the navbar is for the map - when clicked, the website redirects to the html for the map page.
print("<a href='/updates.html'class='center'>Status Updates</a>") # html line: the third part of the navbar is for status updates - when clicked, the website redirects to the html for the status updates page.
print("<a href='/arrivaltimes.html'>Arrival Times</a>") # html line: the fourth part of the navbar is for the arrival times - when clicked, the website redirects to the html for the arrival times page.
print("<a href='/liftupdates.html'>Lift Updates</a>") # html line: the fifth part of the navbar is for the lift updates - when clicked, the website redirects to the html for the lift updates page.
print("<a href='/index.html'class='right'>About</a>") # html line: the last part of the navbar is for the information page - when clicked, the website redirects to the html for the about page.
print("</div>") # html line: closing tag for the navbar div defined from the CSS file for structuring the web page.

print("<div class='header'>") # html line: references the header div element defined from the CSS file for structuring the web page (objective 4.1).
print("<h3>Tube Journey Planner</h3>") # html line: text within the header div element is output.
print("<h3>Farheen Fahim</h3>") # html line: text within the header div element is output.
print("</div>") # html line: closes the header div element defined from the CSS file for structuring the web page.

print("<h1>Arrivals</h1>") # html line: outputs a title for the webpage.

# Objective 3.3:
endpoint = ("https://api.tfl.gov.uk/Stoppoint/Search/?query=" + station + "&modes=tube&app_key=61cab23336c147e29c64f5de382d1d91") # the variable called "endpoint" stores the string which is the url for accessing the API information.
t = tubeAPI.Tube_API() # Instantiation: creates an object called "t" using the class called "Tube_API" from the "tubeAPI" file which was imported at the start.
ID, ICSCODE = t.get_station_id(station) # Calls the "get_station_id" method within the object called "t" with the argument "station", the values returned are stored using the identifiers called "ID" and "ICSCODE.

endpoint = ("https://api.tfl.gov.uk/Mode/tube/Arrivals/?app_key=61cab23336c147e29c64f5de382d1d91") # the variable called "endpoint" stores the string which is the url for accessing the API information.
data = t.get_data(endpoint) # Calls the "get_data" method within the object called "t" with the argument "endpoint", the value returned is stored using the identifier called "data".
all_info = [] # Creates an empty list called "all_info".
for i in range(len(data)): # For loop: iterates through the list called "data".
    dictionary = data[i] # Stores the value from the "data" list which has index position i using the identifier called "dictionary".
    if station in dictionary["stationName"]: # If the station which the user entered is in the data we are iterating through, then it is relevant, and we need to filter for this data, so run the following line of code.
        all_info.append(dictionary) # Append the relevent information to the (empty) list so that this list only contains the information on the station the user has entered.
if len(all_info) == 0: # If the length of the list called "all_info" is 0, there is no information on any arrivals to this station at the moment, so run the following line of code.
    print("<h3> No arrivals at this station at the moment, sorry :( </h3>") # html line: since there is no information on any arrivals to this station at the moment, this line displays a relevant message for the user.
else: # If the length of the list called "all_info" is not 0, then there is information on one or many arrivals at the station the user has entered, so run the following lines of code to display the information accessed from the API.
    # Objective 9.1:
    for i in range(len(all_info)): # For loop: iterates through the list called "all_info" so that all arrivals are outputted for the user.
        information = all_info[i] # Stores the value from the "all_info" list which has index position i using the identifier called "information".
        text = station # Assigns the value stored in the variable "station" to the variable called "text".
        #Creating strings which are ready to be output (involves concatenating strings with strings accessed from the dictionary with information on the arrival):
        text0 = "Arrival " + str(i+1) # Stores a string (which helps to label each arrival when outputting it for the user) in the variable called "text0".
        text1 = "Line name: " + information["lineName"] # Stores a string (which contains information about the line name of the arriving train) in the variable called "text1".
        text2 = "Platform name: " + information["platformName"] # Stores a string (which contains information about the platform name of the arriving train) in the variable called "text2".
        text3 = "Direction: " + information["direction"] # Stores a string (which contains information about the direction of the arriving train) in the variable called "text3".
        text4 = "Destination name: " + information["destinationName"] # Stores a string (which contains information about the destination name of the arriving train) in the variable called "text4".
        text5 = "Current Location: " + information["currentLocation"] # Stores a string (which contains information about the current location of the arriving train) in the variable called "text5".
        text6 = "Towards: " + information["towards"] # Stores a string (which contains information about the station that the arriving train is going towards) in the variable called "text6".
        text7 = "Expected arrival:" + information["expectedArrival"] # Stores a string (which contains information about the expected arrival time of the arriving train) in the variable called "text7".
        print("<h3> %s</h3>" % text) # html line: outputs a line which adds a title for which station the user is loking at arrivals for.
        print("<br>") # html line: <br> tag for line breaks between content
        print("<h3> %s</h3>" % text0) # html line: outputs a line which orders the data by adding a subtitle for which arrival it is (e.g. arrival 1, 2, 3 etc).
        print("<h3> %s</h3>" % text1) # html line: outputs the data from the API which corresponds to the station that the user entered (which line is used for the arrival).
        print("<h3> %s</h3>" % text2) # html line: outputs the data from the API which corresponds to the station that the user entered (which platform the arrival will be at).
        print("<h3> %s</h3>" % text3) # html line: outputs the data from the API which corresponds to the station that the user entered (the direction the train is travelling).
        print("<h3> %s</h3>" % text4) # html line: outputs the data from the API which corresponds to the station that the user entered (the destination of the train).
        print("<h3> %s</h3>" % text5) # html line: outputs the data from the API which corresponds to the station that the user entered (the train's current location).
        print("<h3> %s</h3>" % text6) # html line: outputs the data from the API which corresponds to the station that the user entered (where the train is going towards).
        print("<h3> %s</h3>" % text7) # html line: outputs the data from the API which corresponds to the station that the user entered (the expected arrival time of the train).
        print("<br>") # html line: <br> tag for line breaks between content

print("<h3> Want to look at other station arrivals? </h3>") # html line: outputs text on the webpage.
print ("<a href='../arrivaltimes.html'> Arrivals At Each Station <a>") # html line: outputs a link for the user to use if they want to return to the previous webpage.

print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content

print("<div class='footer'>") # html line: references the footer div element defined from the CSS file for structuring the web page (objective 4.1).
print("<h3>Computer Science: Non-Exam Assessment</h3>") # html line: text within the footer div element is output.
print("<h3>2022/23</h3>") # html line: text within the footer div element is output.
print("</div>") # html line: closes the footer div element defined from the CSS file for structuring the web page.

print ("</body>") # html line: the closing </body> element for structuring the web page
print ("</html>") # html line: the closing </html> element for structuring the web page
            
