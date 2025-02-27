import cgi, cgitb, requests # Import modules which will be used later in the program.
import tubeAPI # Import modules which will be used later in the program.

form = cgi.FieldStorage() # Data inputted from the form is stored so that it can be used later in the program.
line = form.getvalue("line") # The line that the user inputted is accessed from the form and stored as the variable called "line".
line = "Victoria"
# Print statements output as html lines:

print ("Content-type:text/html\n\n") # html line: defines the content type so that the lines are processed and interpretted correctly by the computer.
print ("<html>") # html line: the <html> element for structuring the web page.
print ("<head>") # html line: the <head> element for structuring the web page.
print ("<title>Status Updates for TfL</title>") # html line: the <title> element for distinguishing which page the user is on.
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
print("<h3>Status Updates</h3>") # html line: text within the header div element is output.
print("<h3>Farheen Fahim</h3>") # html line: text within the header div element is output.
print("</div>") # html line: closes the header div element defined from the CSS file for structuring the web page.

print("<h1>Status Updates</h1>") # html line: outputs a title for the webpage.

# Objective 3.3:
endpoint = ('https://api.tfl.gov.uk/Line/Mode/tube/Status?app_key=61cab23336c147e29c64f5de382d1d91') # the variable called "endpoint" stores the string which is the url for accessing the API information.

t = tubeAPI.Tube_API() # Instantiation: create an object called "t" using the class called "Tube_API" from the "tubeAPI" file which was imported at the start.
data = t.get_data(endpoint) # Calls the "get_data" method within the object called "t" with the argument "endpoint", the value returned is stored using the identifier called "data".

info_list = [] # Creates an empty list called "info_list".
line_disruption = False # Sets the Boolean value called "line_disruption" to be False.
for i in range (len (data)): # For loop: iterates through the list called "data".
    dictionary = data[i] # Stores the value from the "data" list which has index position i using the identifier called "dictionary".
    if line in dictionary["name"]: # Filter for the line that the user has given as input (only runs next lines of code if the line that the user has inputted is in the dictionary)
        disruptions = dictionary["disruptions"] # Stores the value from the dictionary called "dictionary" which corresponds to the disruptions using the identifier called "disruptions"
        if len(disruptions) == 0: # If the list containing the details of disruptions ("disruptions") is empty, then there are no disruptions, so run the following line.
            print("<h3> No disruptions </h3>") # html line: tells the user that there are no disruptions by displaying a message.
        else: # If the list containing the details of disruptions ("disruptions" is not empty, then there are disruptions, so run the following lines of code.
            for i in range (len(disruptions)): # For loop: iterates through the list called "disruptions".
                text1 = disruptions[i] # Stores the value from the "disruptions" list which has index position i using the identifier called "text1".
                print("<h3> %s </h3>" %text1) # html line: outputs the data from the API which corresponds to the line that the user entered (if there are any disruptions/ extent of disruptions).
        text2 = dictionary["lineStatuses"] # Stores the value from the dictionary called "dictionary" which corresponds to the lineStatuses using the identifier called "text2".
        text2 = text2[0] # Updates the list called "text2" so that it is the first element of that list (which is a dictionary).
        text2 = text2["statusSeverityDescription"] # Updates the dictionary called "text2" so that it becomes the value corresponding to the status severity description in the dictionary.
        print("<h3> %s </h3>" %text2) # html line: outputs the data from the API which corresponds to the line that the user entered (severity description of delays).

# Objective 4.2
print("<style>") # html line: the <style> element for styling the web page.
print(".responsive {") # html line: creates a <div> section so that an image can be styled correctly later.
print("max-width: 100%;") # html line: adjusts the maximum width of an image which uses this styling so that it is not scaled up or down (ensures that the image is displayed nicely).
print("height: auto;") # html line: adjusts the height of an image that uses this styling so that it is automatically determined based on the size of the screen/window.
print("</style>") # html line: the closing </style> element for styling the web page.

# Objective 9.2:
# If statements for choosing the image which corresponds to the line that the user has inputted in the form:
if line == "Bakerloo":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Bakerloo-line-map.png'
elif line == "Central":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Central-line-map.png'
elif line == "Circle":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Circle-line-map.png'
elif line == "District":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/District-line-map.png'
elif line == "Hammersmith & City":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Hammersmith-city-line-map.png'
elif line == "Jubilee":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Jubilee-line-map.png'
elif line == "Metropolitan":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Metropolitan-line-map.png'
elif line == "Northern":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Northern-line-map.png'
elif line == "Piccadilly":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Piccadilly-line-map.png'
elif line == "Victoria":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Victoria-line-map.png'
elif line == "Waterloo & City":
    link = 'https://www.london-tube-map.info/wp-content/uploads/2016/04/Waterloo-city-line-map.png'
img_text = "<img src=" + link + " class='responsive'>" # Stores a string in the variable called "img_text". THe string is html for outputting an image which is styled by the code above the if statements.
print(img_text) # html line: outputs the string stored in the "img_text" variable in order to output an image.


print("<h3> Want to look at other lines' status updates? </h3>") # html line: outputs text on the webpage.
print ("<a href='../updates.html'> Status Updates <a>") # html line: outputs a link for the user to use if they want to return to the previous webpage.

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

