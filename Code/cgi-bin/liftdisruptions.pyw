import csv, requests, json, cgi, cgitb, shutil, glob, os # Import modules which will be used later in the program.
import tubeAPI # Import modules which will be used later in the program.

#form will allow them to input any station AND if they want to see toilets, ramp routes, step free changes
form = cgi.FieldStorage() # Data inputted from the form is stored so that it can be used later in the program.

station = form.getvalue('station_lifts') # The station that the user inputted is accessed from the form and stored as the variable called "station".

# Print statements output as html lines:

print ("Content-type:text/html\n\n") # html line: defines the content type so that the lines are processed and interpretted correctly by the computer.
print ("<html>") # html line: the <html> element for structuring the web page.
print ("<head>") # html line: the <head> element for structuring the web page.
print ("<title>Lift Disruptions</title>") # html line: the <title> element for distinguishing which page the user is on.
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

print("<h1>Lift Updates</h1>") # html line: outputs a title for the webpage.

t = tubeAPI.Tube_API() # Instantiation: create an object called "t" using the class called "Tube_API" from the "tubeAPI" file which was imported at the start.
ID, ICSCODE = t.get_station_id(station) # Calls the "get_station_id" method within the object called "t" with the argument "station", the values returned are stored using the identifiers called "ID" and "ICSCODE.

# Objective 3.3:
endpoint = ("https://api.tfl.gov.uk/Disruptions/Lifts/v2/?app_key=61cab23336c147e29c64f5de382d1d91") # the variable called "endpoint" stores the string which is the url for accessing the API information.
data = t.get_data(endpoint) # Calls the "get_data" method within the object called "t" with the argument "endpoint", the value returned is stored using the identifier called "data".
empty = [] # Creates an empty list called "empty".
for i in range(len(data)): # For loop: iterates through the list called "data".
    dictionary = data[i] # Stores the value from the "data" list which has index position i using the identifier called "dictionary".
    if ID in dictionary["stationUniqueId"]: # If the station which the user entered is in the data we are iterating through, then it is relevant, and we need to filter for this data, so run the following line of code.
        empty.append(data[i]) # Append the relevent information to the (empty) list so that this list only contains the information on the station the user has entered.
data = empty # Stores the list already stored in empty using the identifier "data".
if len(data) == 0: # If the length of the list called "data" is 0, there is no information on any lift disruptions at this station at the moment, so run the following line of code.
    print("<h3> No lift disruptions at this station at the moment :) </h3>") # html line: since there is no information on any lift disruptions at this station at the moment, this line displays a relevant message for the user.
else: # If the length of the list called "data" is not 0, then there is information on lift disruptions at the station the user has entered, so run the following lines of code to display the information accessed from the API.
    for i in range(len(data)): # For loop: iterates through the list called "data" so that all lift disruptions are outputted for the user.
        dictionary = data[i] # Stores the value from the "data" list which has index position i using the identifier called "dictionary".
        #Creating strings which are ready to be output (involves concatenating strings with strings accessed from the dictionary with information on the lift disruption):
        text1 = "Message: " + str(dictionary["message"]) # Stores a string (which contains a description of the lift disruption) in the variable called "text1".
        text2 = "Lift Affected (Unique Lift ID): " + str(dictionary["disruptedLiftUniqueIds"]) # Stores a string (which contains the lift ID of the lift which is affected by the disruption) in the variable called "text2".
        text0 = "Lift " + str(i+1) # Stores a string (which helps to label each lift disruption when outputting it for the user) in the variable called "text0".
        print("<h3> %s</h3>" % text0) # html line: outputs a line which orders the data by adding a subtitle for which lift disruption it is (e.g. lift disruption 1, 2, 3 etc).
        print("<br>") # html line: <br> tag for line breaks between content
        print("<h3> %s</h3>" % text1) # html line: outputs the data from the API which corresponds to the station that the user entered (message describing how long the lift will be affected).
        print("<h3> %s</h3>" % text2) # html line: outputs the data from the API which corresponds to the station that the user entered (which lift is affected).
        print("<br>") # html line: <br> tag for line breaks between content

print("<br>") # html line: <br> tag for line breaks between content
print("<br>") # html line: <br> tag for line breaks between content
print("<h3> Want to look at other stations' lift disruptions? </h3>") # html line: outputs text on the webpage.
print ("<a href='../liftupdates.html'> Lift Updates <a>") # html line: outputs a link for the user to use if they want to return to the previous webpage.

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
    
    
    

