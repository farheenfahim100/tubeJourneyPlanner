import cgi, cgitb, math # Import modules which will be used later in the program.

form = cgi.FieldStorage() # Data inputted from the form is stored so that it can be used later in the program.

# Objective 1:

station1=form.getvalue('station1') # The start station (that the user inputted) is accessed from the form and stored as the variable called "station1".
station2=form.getvalue('station2') # The end station (that the user inputted) is accessed from the form and stored as the variable called "station2".
rush_hour=form.getvalue('rush_hour') # The  value for rush hour (that the user inputted) is accessed from the form and stored as the variable called "rush_hour".
weekend=form.getvalue('weekend') # The value for if it is the weekend (that the user inputted) is accessed from the form and stored as the variable called "weekend".
step_free=form.getvalue('stepfree') # The value for if the journey is step-free (that the user inputted) is accessed from the form and stored as the variable called "stepfree".

# Print statements output as html lines:

print ("Content-type:text/html\n\n") # html line: defines the content type so that the lines are processed and interpretted correctly by the computer.
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

print ("<h1>Route</h1>") # html line: outputs a title for the webpage.

class JourneyPlanner: # Creates a class for the journey planner called "JourneyPlanner".
    def __init__ (self,station1,station2,rush_hour,weekend): # Defines the constructor method which takes 4 arguments (other than the object parameter).
        # This method is used to define class attributes.
        
        self.station1 = station1 # Assigns value stored in the parameter "station1" as the "self.station1" attribute.
        self.station2 = station2 # Assigns value stored in the parameter "station2" as the "self.station2" attribute.
        self.rush_hour = rush_hour # Assigns value stored in the parameter "rush_hour" as the "self.rush_hour" attribute.
        self.weekend = weekend # Assigns value stored in the parameter "weekend" as the "self.weekend" attribute.

        # Objectives 1.3, 1.4, 1.5:
        # Objectives 2.1, 2.2:
        # Objective 7:

        # Creates an adjacency dictionary attribute called "self.stations_adjacency_dict" containing keys which represent the station you are at, and values which are dictionaries as well.
        # These dictionaries contain keys which represent the station you can travel to, and the values are the number of seconds taken to travel there.
        self.stations_adjacency_dict= {
            "Paddington CircleLine": {"Bayswater CircleLine":85.7,"Edgware Road CircleLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington DistrictLine": 300,"Paddington HammersmithLine":300},
            "Paddington DistrictLine": {"Bayswater DistrictLine":85.7,"Edgware Road DistrictLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington CircleLine": 300,"Paddington HammersmithLine":300},
            "Paddington HammersmithLine":{"Edgware Road HammersmithLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington CircleLine": 300,"Paddington DistrictLine":300},
            "Paddington BakerlooLine": {"Edgware Road BakerlooLine":75.3, "Paddington ElizabethLine": 300,"Paddington DistrictLine": 300,"Paddington CircleLine": 300,"Paddington HammersmithLine":300},
            "Paddington ElizabethLine": {"Tottenham Court Road ElizabethLine":241.6,"Paddington BakerlooLine":300,"Paddington DistrictLine": 300,"Paddington CircleLine": 300,"Paddington HammersmithLine":300},
            "Bayswater CircleLine": {"Paddington CircleLine":85.7, "Notting Hill Gate CircleLine":86.1,"Bayswater DistrictLine":300},
            "Bayswater DistrictLine": {"Paddington DistrictLine":85.7, "Notting Hill Gate DistrictLine":86.1,"Bayswater CircleLine":300},
            "Notting Hill Gate CircleLine": {"Bayswater CircleLine":86.1, "High Street Kensington CircleLine":87.3, "Notting Hill Gate CentralLine":300,"Notting Hill Gate DistrictLine":300},
            "Notting Hill Gate DistrictLine": {"Bayswater DistrictLine":86.1, "High Street Kensington DistrictLine":87.3, "Notting Hill Gate CentralLine":300,"Notting Hill Gate CircleLine":300},
            "Notting Hill Gate CentralLine":{"Queensway CentralLine":68.5, "Notting Hill Gate CircleLine":300,"Notting Hill Gate DistrictLine":300},
            "High Street Kensington CircleLine": {"Gloucester Road CircleLine":150.1,"Notting Hill Gate CircleLine":87.3,"High Street Kensington DistrictLine":300},
            "High Street Kensington DistrictLine": {"Earl's Court DistrictLine":175.6,"Notting Hill Gate DistrictLine": 87.3,"High Street Kensington CircleLine": 300},
            "Earl's Court DistrictLine": {"High Street Kensington DistrictLine":175.6, "Gloucester Road DistrictLine":91.4, "Earl's Court PiccadillyLine":300},
            "Earl's Court PiccadillyLine": {"Gloucester Road PiccadillyLine":91.4, "Earl's Court DistrictLine":300},
            "Gloucester Road PiccadillyLine": {"Earl's Court PiccadillyLine":91.4,"South Kensington PiccadillyLine":76.6,"Gloucester Road CircleLine":300,"Gloucester Road DistrictLine":300},
            "Gloucester Road CircleLine":{"South Kensington CircleLine":78.2, "High Street Kensington CircleLine":150.1,"Gloucester Road DistrictLine":300,"Gloucester Road PiccadillyLine":300},
            "Gloucester Road DistrictLine":{"South Kensington DistrictLine":78.2, "Earl's Court DistrictLine":91.4,"Gloucester Road CircleLine":300,"Gloucester Road PiccadillyLine":300},
            "South Kensington CircleLine": {"Gloucester Road CircleLine":78.2,"Sloane Square CircleLine":110.4,"South Kensington DistrictLine":300,"South Kensington PiccadillyLine":300},
            "South Kensington DistrictLine":{"Gloucester Road DistrictLine":78.2, "Sloane Square DistrictLine":110.4 , "South Kensington CircleLine":300,"South Kensington PiccadillyLine":300},
            "South Kensington PiccadillyLine": {"Knightsbridge PiccadillyLine":156.8,"Gloucester Road PiccadillyLine":76.6,"South Kensington DistrictLine":300,"South Kensington CircleLine":300},
            "Sloane Square CircleLine": {"South Kensington CircleLine":110.4,"VictoriaStation CircleLine":88.7,"Sloane Square DistrictLine":300},
            "Sloane Square DistrictLine": {"South Kensington DistrictLine":110.4,"VictoriaStation DistrictLine":88.7,"Sloane Square CircleLine":300},
            "VictoriaStation CircleLine": {"Sloane Square CircleLine":88.7,"St. James's Park CircleLine":75.1,"VictoriaStation DistrictLine":300,"VictoriaStation VictoriaLine":300},
            "VictoriaStation DistrictLine": {"Sloane Square DistrictLine":88.7,"St. James's Park DistrictLine":75.1,"VictoriaStation CircleLine":300,"VictoriaStation VictoriaLine":300},
            "VictoriaStation VictoriaLine": {"Pimlico VictoriaLine":82.3,"Green Park VictoriaLine":78.4,"VictoriaStation CircleLine":300,"VictoriaStation DistrictLine":300},
            "St. James's Park CircleLine": {"VictoriaStation CircleLine":75.1,"Westminster CircleLine":86.1,"St. James's Park DistrictLine":300},
            "St. James's Park DistrictLine": {"VictoriaStation DistrictLine":75.1,"Westminster DistrictLine":86.1,"St. James's Park CircleLine":300},
            "Westminster CircleLine": {"St. James's Park CircleLine":86.1,"Embankment CircleLine":81.6,"Westminster DistrictLine":300,"Westminster JubileeLine":300},
            "Westminster DistrictLine": {"St. James's Park DistrictLine":86.1,"Embankment DistrictLine":81.6,"Westminster CircleLine":300,"Westminster JubileeLine":300},
            "Westminster JubileeLine": {"WaterlooStation JubileeLine":78.1,"Green Park JubileeLine":99.8,"Westminster DistrictLine":300,"Westminster CircleLine":300},
            "Embankment CircleLine": {"Westminster CircleLine":81.6,"Temple CircleLine":66.4,"Embankment DistrictLine":300,"Embankment BakerlooLine":300,"Embankment NorthernLine":300},
            "Embankment DistrictLine": {"Westminster DistrictLine":81.6,"Temple DistrictLine":66.4,"Embankment CircleLine":300,"Embankment BakerlooLine":300,"Embankment NorthernLine":300},
            "Embankment BakerlooLine": {"WaterlooStation BakerlooLine":49.5,"Charing Cross BakerlooLine":93.4,"Embankment DistrictLine":300,"Embankment CircleLine":300,"Embankment NorthernLine":300},
            "Embankment NorthernLine": {"WaterlooStation NorthernLine":49.5,"Charing Cross NorthernLine":93.4,"Embankment DistrictLine":300,"Embankment BakerlooLine":300,"Embankment CircleLine":300},
            "Temple CircleLine": {"Embankment CircleLine":66.4,"Blackfriars CircleLine":86.6,"Temple DistrictLine":300},
            "Temple DistrictLine": {"Embankment DistrictLine":66.4,"Blackfriars DistrictLine":86.6,"Temple CircleLine":300},
            "Blackfriars CircleLine": {"Temple CircleLine":86.6,"Mansion House CircleLine":90.9,"Blackfriars DistrictLine":300},
            "Blackfriars DistrictLine": {"Temple DistrictLine":86.6,"Mansion House DistrictLine":90.9,"Blackfriars CircleLine":300},
            "Mansion House CircleLine": {"Blackfriars CircleLine":90.9,"Cannon Street CircleLine":61.9,"Mansion House DistrictLine":300},
            "Mansion House DistrictLine": {"Blackfriars DistrictLine":90.9,"Cannon Street DistrictLine":61.9,"Mansion House CircleLine":300},
            "Cannon Street CircleLine": {"Mansion House CircleLine":61.9,"Monument CircleLine":66.3,"Cannon Street DistrictLine":300},
            "Cannon Street DistrictLine": {"Mansion House DistrictLine":61.9,"Monument DistrictLine":66.3,"Cannon Street CircleLine":300},
            "Monument CircleLine": {"Cannon Street CircleLine":66.3,"Tower Hill CircleLine":92.5,"Monument DistrictLine":300},
            "Monument DistrictLine": {"Cannon Street DistrictLine":66.3,"Tower Hill DistrictLine":92.5,"Monument CircleLine":300},
            "Tower Hill CircleLine": {"Monument CircleLine":92.5,"AldgateStation CircleLine":95.9,"Tower Hill DistrictLine":300},
            "Tower Hill DistrictLine": {"Monument DistrictLine":92.5,"Aldgate East DistrictLine":132.9,"Tower Hill CircleLine":300},
            "Aldgate East DistrictLine": {"Tower Hill DistrictLine":132.9,"Aldgate East HammersmithLine":300},
            "Aldgate East HammersmithLine":{"Liverpool Street HammersmithLine":128.4,"Aldgate East DistrictLine":300},
            "AldgateStation CircleLine": {"Tower Hill CircleLine":95.9,"Liverpool Street CircleLine":102.9},
            "Liverpool Street CircleLine": {"AldgateStation CircleLine":102.9,"Moorgate CircleLine":70.6,"Liverpool Street HammersmithLine":300,"Liverpool Street CentralLine":300,"Liverpool Street ElizabethLine":300},
            "Liverpool Street HammersmithLine": {"Aldgate East HammersmithLine":128.4,"Moorgate HammersmithLine":70.6,"Liverpool Street CircleLine":300,"Liverpool Street CentralLine":300,"Liverpool Street ElizabethLine":300},
            "Liverpool Street CentralLine":{"Bank CentralLine":97.5,"Liverpool Street CircleLine":300,"Liverpool Street HammersmithLine":300,"Liverpool Street ElizabethLine":300},
            "Liverpool Street ElizabethLine":{"Farringdon ElizabethLine":96.0, "Liverpool Street CircleLine":300,"Liverpool Street HammersmithLine":300,"Liverpool Street CentralLine":300},
            "Moorgate CircleLine": {"Liverpool Street CircleLine":70.6,"Barbican CircleLine":72.1,"Moorgate HammersmithLine":300,"Moorgate NorthernLine":300},
            "Moorgate HammersmithLine": {"Liverpool Street HammersmithLine":70.6,"Barbican HammersmithLine":72.1,"Moorgate CircleLine":300,"Moorgate NorthernLine":300},
            "Moorgate NorthernLine": {"Bank NorthernLine":88.5,"Old Street NorthernLine":99.5,"Moorgate CircleLine":300,"Moorgate HammersmithLine":300},
            "Barbican CircleLine": {"Moorgate CircleLine":72.1,"Farringdon CircleLine":67.6,"Barbican HammersmithLine":300},
            "Barbican HammersmithLine": {"Moorgate HammersmithLine":72.1,"Farringdon HammersmithLine":67.6,"Barbican CircleLine":300},
            "Farringdon ElizabethLine": {"Liverpool Street ElizabethLine":96.0,"Tottenham Court Road ElizabethLine":138.8,"Farringdon CircleLine":300,"Farringdon HammersmithLine":300},
            "Farringdon CircleLine": {"Barbican CircleLine":67.6,"King's Cross St. Pancras CircleLine":164.0,"Farringdon ElizabethLine":300,"Farringdon HammersmithLine":300},
            "Farringdon HammersmithLine": {"Barbican HammersmithLine":67.6,"King's Cross St. Pancras HammersmithLine":164.0,"Farringdon ElizabethLine":300,"Farringdon CircleLine":300},
            "King's Cross St. Pancras CircleLine": {"Farringdon CircleLine":164.0,"Euston Square CircleLine":83.2,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300},
            "King's Cross St. Pancras HammersmithLine": {"Farringdon HammersmithLine":164.0,"Euston Square HammersmithLine":83.2,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300},
            "King's Cross St. Pancras NorthernLine": {"EustonStation NorthernLine":95.8,"Angel NorthernLine":119.7,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300},
            "King's Cross St. Pancras VictoriaLine": {"EustonStation VictoriaLine":87.4,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras PiccadillyLine":300},
            "King's Cross St. Pancras PiccadillyLine": {"Russell Square PiccadillyLine":89.2,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras CircleLine":300},
            "Euston Square CircleLine": {"King's Cross St. Pancras CircleLine":83.2,"Great Portland Street CircleLine":65.9,"Euston Square HammersmithLine":300},
            "Euston Square HammersmithLine": {"King's Cross St. Pancras HammersmithLine":83.2,"Great Portland Street HammersmithLine":65.9,"Euston Square CircleLine":300},
            "Great Portland Street CircleLine": {"Euston Square CircleLine":65.9,"Baker Street CircleLine":88.4,"Great Portland Street HammersmithLine":300},
            "Great Portland Street HammersmithLine": {"Euston Square HammersmithLine":65.9,"Baker Street HammersmithLine":88.4,"Great Portland Street CircleLine":300},
            "Baker Street CircleLine": {"Great Portland Street CircleLine":88.4,"Edgware Road CircleLine":110.7,"Baker Street HammersmithLine":300,"Baker Street BakerlooLine":300,"Baker Street JubileeLine":300},
            "Baker Street HammersmithLine": {"Great Portland Street HammersmithLine":88.4,"Edgware Road HammersmithLine":110.7,"Baker Street CircleLine":300,"Baker Street BakerlooLine":300,"Baker Street JubileeLine":300},
            "Baker Street BakerlooLine": {"Marylebone BakerlooLine":64.3,"Regent's Park BakerlooLine":98.9,"Baker Street HammersmithLine":300,"Baker Street CircleLine":300,"Baker Street JubileeLine":300},
            "Baker Street JubileeLine": {"Bond Street JubileeLine":112.5,"Baker Street HammersmithLine":300,"Baker Street BakerlooLine":300,"Baker Street CircleLine":300},
            "Edgware Road CircleLine": {"Baker Street CircleLine":110.7,"Paddington CircleLine":110.8,"Edgware Road HammersmithLine":300,"Edgware Road DistrictLine":300,"Edgware Road BakerlooLine":300},
            "Edgware Road HammersmithLine": {"Baker Street HammersmithLine":110.7,"Paddington HammersmithLine":110.8,"Edgware Road CircleLine":300,"Edgware Road DistrictLine":300,"Edgware Road BakerlooLine":300},
            "Edgware Road DistrictLine": {"Paddington DistrictLine":93.1,"Edgware Road HammersmithLine":300,"Edgware Road CircleLine":300,"Edgware Road BakerlooLine":300},
            "Edgware Road BakerlooLine": {"Paddington BakerlooLine":75.3,"Marylebone BakerlooLine":69.1,"Edgware Road HammersmithLine":300,"Edgware Road DistrictLine":300,"Edgware Road CircleLine":300},
            "Marylebone BakerlooLine": {"Edgware Road BakerlooLine":69.1,"Baker Street BakerlooLine":64.3},
            "Angel NorthernLine": {"King's Cross St. Pancras NorthernLine":119.7,"Old Street NorthernLine":122.4},
            "Old Street NorthernLine": {"Angel NorthernLine":122.4,"Moorgate NorthernLine":99.5},
            "EustonStation NorthernLine": {"King's Cross St. Pancras NorthernLine":95.8,"Warren Street NorthernLine":65.6,"EustonStation VictoriaLine":300},
            "EustonStation VictoriaLine": {"King's Cross St. Pancras VictoriaLine":87.4,"Warren Street VictoriaLine":58.7,"EustonStation NorthernLine":300},
            "Queensway CentralLine": {"Notting Hill Gate CentralLine":68.5,"Lancaster Gate CentralLine":98.6},
            "Lancaster Gate CentralLine": {"Queensway CentralLine":98.6,"Marble Arch CentralLine":101.2},
            "Marble Arch CentralLine": {"Lancaster Gate CentralLine":101.2,"Bond Street CentralLine":100.5},
            "Bond Street CentralLine": {"Marble Arch CentralLine":100.5,"Oxford Circus CentralLine":83.3,"Bond Street JubileeLine":300},
            "Bond Street JubileeLine": {"Baker Street JubileeLine":112.5,"Green Park JubileeLine":94.3,"Bond Street CentralLine":300},
            "Green Park JubileeLine": {"Bond Street JubileeLine":94.3,"Westminster JubileeLine":99.8,"Green Park PiccadillyLine":300,"Green Park VictoriaLine":300},
            "Green Park PiccadillyLine": {"Hyde Park Corner PiccadillyLine":116.1,"PiccadillyCircus PiccadillyLine":67.0,"Green Park JubileeLine":300,"Green Park VictoriaLine":300},
            "Green Park VictoriaLine": {"Oxford Circus VictoriaLine":77.6,"VictoriaStation VictoriaLine":78.4,"Green Park PiccadillyLine":300,"Green Park JubileeLine":300},
            "Knightsbridge PiccadillyLine": {"South Kensington PiccadillyLine":156.8,"Hyde Park Corner PiccadillyLine":71.0},
            "Hyde Park Corner PiccadillyLine": {"Knightsbridge PiccadillyLine":71.0,"Green Park PiccadillyLine":116.1},
            "PiccadillyCircus PiccadillyLine": {"Green Park PiccadillyLine":67.0,"Leicester Square PiccadillyLine":68.9,"PiccadillyCircus BakerlooLine":300},
            "PiccadillyCircus BakerlooLine": {"Oxford Circus BakerlooLine":99.5,"Charing Cross BakerlooLine":66.5,"PiccadillyCircus PiccadillyLine":300},
            "Oxford Circus CentralLine": {"Bond Street CentralLine":83.3,"Tottenham Court Road CentralLine":70.3,"Oxford Circus BakerlooLine":300,"Oxford Circus VictoriaLine":300},
            "Oxford Circus BakerlooLine": {"PiccadillyCircus BakerlooLine":99.5,"Regent's Park BakerlooLine":105.8,"Oxford Circus CentralLine":300,"Oxford Circus VictoriaLine":300},
            "Oxford Circus VictoriaLine": {"Green Park VictoriaLine":77.6,"Warren Street VictoriaLine":71.5,"Oxford Circus BakerlooLine":300,"Oxford Circus CentralLine":300},
            "Regent's Park BakerlooLine": {"Baker Street BakerlooLine":98.9,"Oxford Circus BakerlooLine":105.8},
            "Tottenham Court Road CentralLine": {"Oxford Circus CentralLine":70.3,"Holborn CentralLine":79.9,"Tottenham Court Road ElizabethLine":300,"Tottenham Court Road NorthernLine":300},
            "Tottenham Court Road ElizabethLine": {"Farringdon ElizabethLine":138.8,"Paddington ElizabethLine":241.6,"Tottenham Court Road CentralLine":300,"Tottenham Court Road NorthernLine":300},
            "Tottenham Court Road NorthernLine": {"Goodge Street NorthernLine":63.2,"Leicester Square NorthernLine":49.6,"Tottenham Court Road ElizabethLine":300,"Tottenham Court Road CentralLine":300},
            "Goodge Street NorthernLine": {"Tottenham Court Road NorthernLine":63.2,"Warren Street NorthernLine":50.9},
            "Warren Street NorthernLine": {"Goodge Street NorthernLine":50.9,"EustonStation NorthernLine":65.6,"Warren Street VictoriaLine":300},
            "Warren Street VictoriaLine": {"EustonStation VictoriaLine":58.7,"Oxford Circus VictoriaLine":71.5,"Warren Street NorthernLine":300},
            "Holborn CentralLine": {"Tottenham Court Road CentralLine":79.9,"Chancery Lane CentralLine":48.5,"Holborn PiccadillyLine":300},
            "Holborn PiccadillyLine": {"Russell Square PiccadillyLine":84.7,"Covent Garden PiccadillyLine":86.7,"Holborn CentralLine":300},
            "Russell Square PiccadillyLine": {"King's Cross St. Pancras PiccadillyLine":89.2,"Holborn PiccadillyLine":84.7},
            "Leicester Square NorthernLine": {"Tottenham Court Road NorthernLine":49.6,"Charing Cross NorthernLine":67.6,"Leicester Square PiccadillyLine":300},
            "Leicester Square PiccadillyLine": {"PiccadillyCircus PiccadillyLine":68.9,"Covent Garden PiccadillyLine":44.9,"Leicester Square NorthernLine":300},
            "Covent Garden PiccadillyLine": {"Leicester Square PiccadillyLine":44.9,"Holborn PiccadillyLine":86.7},
            "Chancery Lane CentralLine": {"Holborn CentralLine":48.5,"St. Paul's CentralLine":87.0},
            "Charing Cross NorthernLine": {"Embankment NorthernLine":93.4,"Leicester Square NorthernLine":67.6,"Charing Cross BakerlooLine":300},
            "Charing Cross BakerlooLine": {"Embankment BakerlooLine":50.4,"PiccadillyCircus BakerlooLine":66.5,"Charing Cross NorthernLine":300},
            "WaterlooStation JubileeLine": {"Westminster JubileeLine":78.1,"Southwark JubileeLine":49.5,"WaterlooStation NorthernLine":300,"WaterlooStation BakerlooLine":300,"WaterlooStation WaterlooLine":300},
            "WaterlooStation NorthernLine": {"Kennington NorthernLine":169.8,"Embankment NorthernLine":49.5,"WaterlooStation JubileeLine":300,"WaterlooStation BakerlooLine":300,"WaterlooStation WaterlooLine":300},
            "WaterlooStation BakerlooLine": {"Lambeth North BakerlooLine":87.8,"Embankment BakerlooLine":50.4,"WaterlooStation NorthernLine":300,"WaterlooStation JubileeLine":300,"WaterlooStation WaterlooLine":300},
            "WaterlooStation WaterlooLine": {"Bank WaterlooLine":213.4,"WaterlooStation NorthernLine":300,"WaterlooStation BakerlooLine":300,"WaterlooStation JubileeLine":300},
            "Southwark JubileeLine": {"WaterlooStation JubileeLine":49.5,"London Bridge JubileeLine":92.2},
            "London Bridge JubileeLine": {"Southwark JubileeLine":92.2,"London Bridge NorthernLine":300},
            "London Bridge NorthernLine": {"Bank NorthernLine":79.8,"Borough NorthernLine":79.0,"London Bridge JubileeLine":300},
            "Borough NorthernLine": {"Elephant & Castle NorthernLine":94.2,"London Bridge NorthernLine":79.0},
            "Lambeth North BakerlooLine": {"WaterlooStation BakerlooLine":87.8,"Elephant & Castle BakerlooLine":151.1},
            "Elephant & Castle NorthernLine": {"Borough NorthernLine":94.2,"Kennington NorthernLine":100.7,"Elephant & Castle BakerlooLine":300},
            "Elephant & Castle BakerlooLine": {"Lambeth North BakerlooLine":151.1,"Elephant & Castle NorthernLine":300},
            "St. Paul's CentralLine": {"Chancery Lane CentralLine":87.0,"Bank CentralLine":96.3},
            "Bank CentralLine": {"St. Paul's CentralLine":96.3,"Liverpool Street CentralLine":97.5,"Bank NorthernLine":300,"Bank WaterlooLine":300},
            "Bank NorthernLine": {"London Bridge NorthernLine":79.8,"Moorgate NorthernLine":88.5,"Bank CentralLine":300,"Bank WaterlooLine":300},
            "Bank WaterlooLine": {"WaterlooStation WaterlooLine":213.4,"Bank NorthernLine":300,"Bank CentralLine":300},
            "Battersea Power Station NorthernLine": {"Nine Elms NorthernLine":98.8},
            "Nine Elms NorthernLine": {"Battersea Power Station NorthernLine":98.8,"Kennington NorthernLine":168.5},
            "Kennington NorthernLine": {"Nine Elms NorthernLine":168.5,"WaterlooStation NorthernLine":169.8,"Elephant & Castle NorthernLine":100.7},
            "Pimlico VictoriaLine": {"Vauxhall VictoriaLine":62.1,"VictoriaStation VictoriaLine":82.3},
            "Vauxhall VictoriaLine": {"Pimlico VictoriaLine":62.1}
            }
        self.stations_list = list(self.stations_adjacency_dict.keys()) # Assigns keys of the stations adjacency dictionary as the "self.stations_list" attribute.
        self.num_of_stations = len(self.stations_list) # Assigns the length of the stations adjacency dictionary as the "self.num_of_stations" attribute.
        self.stepfree = False # Assigns the Boolean False value as the "self.stepfree" attribute.

    def correct_stations(self): # Defines the "correct_stations" method which takes no arguments (other than the object parameter).
        # This method is used to adjust any stations entered as they may include the line of the station or other station names within it. This will not work when inputted in the "dijkstra" function because the function searches for specific phrases within strings.
        # For example, if the user enters "Victoria" station as their start station, this must be chnaged to "VictoriaStation" in order to ensure that it is not confused with the Victoria line.
        # This method uses if-elif statements to change values which the user may have inputted so that they are compatible with the "dijkstra" function.
        if self.station1 == "Victoria":
            self.station1 = "VictoriaStation"
        elif self.station1 == "Piccadilly Circus":
            self.station1 = "PiccadillyCircus"
        elif self.station1 == "Waterloo":
            self.station1 = "WaterlooStation"
        elif self.station1 == "Aldgate":
            self.station1 = "AldgateStation"
        elif self.station1 == "Euston":
            self.station1 = "EustonStation"
        if self.station2 == "Victoria":
            self.station2 = "VictoriaStation"
        elif self.station2 == "Piccadilly Circus":
            self.station2 = "PiccadillyCircus"
        elif self.station2 == "Waterloo":
            self.station2 = "WaterlooStation"
        elif self.station1 == "Aldgate":
            self.station1 = "AldgateStation"
        elif self.station2 == "Aldgate":
            self.station2 = "AldgateStation"
        elif self.station2 == "Euston":
            self.station2 = "EustonStation"
        
    # Objective 2:
    def dijkstra(self,start_node,end_node): # Defines the "dijkstra" method which takes 2 arguments (other than the object parameter).
        # This method is used to calculate the shortest route between the parameter called "start_node" and the parameter called "end_node".
        # It determines the index position of "start_node" in "self.stations_list" using the "linear_search" method.
        # Then, empty dictionaries are created which correspond to the nodes that have been visited ("visited_nodes"), the station used to reach another station ("path_taken"), and the distances between the "start_node" and every other node ("distances").
        # All of the nodes are marked as unvisited in the "visited_nodes" dictionary by making the keys the elements in the list called "self.stations_list" and the values corresponding to them as False.
        # All of the distances to each node are set to infinity in the "distances" dictionary by making the keys the elements in the list called "self.stations_list" and the values corresponding to them as math.inf.
        # The distance to the start node is set to 0 by making the value corresponding to the "start_node" key as 0 in the "distances" dictionary.
        # Based on whether it is rush hour or not and if it is the weekned, a variable called multiplier is determined and then all of the values in the adjacency dictionary are multiplied by that number.

        # The next part of code is run fro every node/station, so it uses a for loop.
        # The closest unvisited node is selected by using a for loop (nested within another for loop) and comparing values in the "distances" dictionary and checking if the corresponding values in the "visited_nodes" dictionary are False or not.
        # After the closest unvisited node is selected, it is marked as visited by changing its corresponding value in the "visited_nodes" dictionary.
        # Then, the distances to the nodes adjacent to the selected node are calculated. The distance is calculated by adding the distance between the selected node and the adjacent node and the distance between the start node and the selected node.
        # The distances in the dictionary called "distances" are updated if the value caulculated is less than the value already stored.
        # If the value is updates, then a record of how to get to that node is made using the dictionary called "path_taken".

        # After the for loop has run and all distances to all other nodes are caulculated:

        # If the journey is not step free, then the "find_end_node" function is called which is used to determine which line the user will use last. This ensures that the route does not have an added 300 seconds due to a changeover at the end station which is not required.
        # A "path_list" is created which contains elements which are part of the route the user should take.
        # The list called "path_list" is the returned value from the "recursive_find_path" function.
        # Then, "path_list" is reversed (as it contains the route from the end node to the start node).
        # The "distances" dictionary, "path_list" list, and "end_node" variable are returned from this function.
        

        start_node_index = self.linear_search(start_node, self.stations_list) # Calls the "linear_Search" function with the parameters "start_node" and "self.stations_list", then stores the returned value in "start_node_index".
        visited_nodes = {} # Creates an empty dictionary called "visited_nodes".
        path_taken = {} # Creates an empty dictionary called "path_taken".
        distances = {} # Creates an empty dictionary called "distances".
        for i in range (self.num_of_stations): # For loop which iterates through "self.stations_list".
            visited_nodes[self.stations_list[i]] = False  # Assigns the value corresponding to the key "self.stations_list[i]" in the dictionary "visited_nodes" to be False.
            distances[self.stations_list[i]] = math.inf # Assigns the value corresponding to the key "self.stations_list[i]" in the dictionary "distances" to be infinity.
        distances[start_node] = 0 # Changes the value corresponding to the key "start_node" in the dictionary "distances" to be equal to 0 as this dictionary contains the distances to get to that node from the start node.
        
        # Objectives 5.1, 5.2, 5.3:
        #Changes all times depending on if it is rush hour or a weekend:
        if self.rush_hour == True and self.weekend == True: # If "self.rush_hour" is True and "self.weekend" is also True, then run the following lines of code.
            multiplier = 2.5 # Assings the value of 2.5 to the variable called "multiplier".
        elif self.rush_hour == False and self.weekend == True: # If "self.rush_hour" is False and "self.weekend" is True, then run the following lines of code.
            multiplier = 1.5 # Assings the value of 1.5 to the variable called "multiplier".
        elif self.rush_hour == True and self.weekend == False: # If "self.rush_hour" is True and "self.weekend" is False, then run the following lines of code.
            multiplier = 2 # Assigns the value of 2 to the variable called "multiplier".
        else: # If "self.rush_hour" is False and "self.weekend" is also False, then run the following lines of code.
            multiplier = 1 # Assigns the value of 1 to the variable called "multiplier".
       

        for i in range(self.num_of_stations): # For loop which iterates through the "self.num_of_stations" list.
                key = self.stations_list[i] # Assigns the value in "self.stations_list[i]" in the variable called "key".
                dict = self.stations_adjacency_dict[key] # Stores the value corresponding to the key "key" in the dictionary called "self.stations_adjacency_dict" using the identifier called "dict".
                for j in range(self.num_of_stations): # For loop which iterates through the "self.num_of_stations" list.
                    try: # Try block for error handling.
                        node_key = self.stations_list[j] # Assigns the value in "self.stations_list[j]" in the variable called "node_key".
                        dict[node_key] = dict[node_key] * multiplier # Multiplies the value corresponding to the key called "node_key" in the dictionary called "dict" by the variable called "multiplier".
                    except: # Except block for error handling.
                        pass # If there is an error, this line is run so that the error is handled.

        for i in range (self.num_of_stations): # For loop which iterates through all of the stations in "self.stations_list".
            closest_node_index = None # Assigns None to the variable called "closest_node_index".   
        # SELECT CLOSEST UNVISITED NODE:
            for j in range(self.num_of_stations): # For loop which iterates through all of the stations in "self.stations_list" in order to determine which node is the closest and unvisited node.
                if i == 0: # If i is equal to 0, then run the following code (as closest_node_index" will be None before this and you cannot use None for an index in a list).
                    closest_node_index = start_node_index # Assigns the value in "start_node_index" to the variable "closest_node_index".
                    closest_node = self.stations_list[closest_node_index] # Assigns "self.stations_list[closest_node_index]" as the variable "closest_node".
                elif closest_node_index == None: #  If closest_node_index is None, then run the following code (as you cannot use None for an index in a list).
                    for k in range(self.num_of_stations): #  For loop which iterates through all of the stations in "self.stations_list".
                        key = self.stations_list[k] # Assigns "self.stations_list[k]" to the variable "key".
                        if visited_nodes[key] == False and distances[key] != math.inf and distances[key] != 0: # If the distance to the "key" is infinity but not 0, and the node is unvisited, run the following code.
                            closest_node_index = k # Assigns k to the variable "closest_node_index".
                            closest_node = self.stations_list[closest_node_index] #  Assigns "self.stations_list[closest_node_index]" to the variable "closest_node".
                elif distances[self.stations_list[j]] < distances[closest_node] and visited_nodes[self.stations_list[j]] == False: # If the current closest_node has a distance greater than "distances[self.stations_list[j]]", and this node is unvisited, run the following lines of code.
                    closest_node_index = j # Assigns j to the variable "closest_node_index".
                    closest_node = self.stations_list[closest_node_index] # Assigns "self.stations_list[closest_node_index]" to the variable called "closest_node".
            current_node = closest_node # Assigns the value in "closest_node" to the variable "current_node".
            current_node_index = closest_node_index  # Assigns the value in "closest_node_index" to the variable "current_node_index".
            # MARK NODE AS VISITED:
            visited_nodes[current_node] = True # Changes the value corresponding to the key called "current_node" in the dictionary called "visited_nodes" to True.
            adjacent_nodes_list = self.stations_adjacency_dict[current_node] # Assigns the value corresponding to the key "current_node" in the dictionary "self.stations_adjacency_dict" to the dictionary called "adjacent_nodes_list".
            add_on_distance = distances[current_node] # Stores the distance to the current_node ("distances[current_node]") in the variable called "add_on_distance".

            # UPDATE VALUES IF THE DISTANCES ARE SHORTER:
            keys_list = list(adjacent_nodes_list.keys()) # Stores the keys in the "adjacent_nodes_list" in "keys_list" in a list format.
            for key in (keys_list): # For loop which iterates through every element in the list called "keys_list".
                new_distance = adjacent_nodes_list[key] + add_on_distance # Adds the value stored in "adjacent_nodes_list[key]" to "add_on_distance" and stores the result to the variable called "new_distance".

                #Objective 1.2:
                
                if new_distance < distances[key] and visited_nodes[key] == False: # If the value stored in "new_distance" is less than the distance in "distances[key]" (the distance alreadfy recorded) and "visited_nodes[key]" is False, then run the following code.
                    distances[key] = new_distance # Updates the value corresponding to the key called "key" to be the value stored in "new_distance".
                    path_taken[key] = current_node # Adds a new key-value pair to the "path_taken" dictionary which has key of "key" and value of "current_node". This is used to show that, in order to get to the station "key", you need to travel to "current_node" first.
            
            
        if self.stepfree == False: # If "self.stepfree" is False, then run the following lines of code.
            end_node,shortest_distance = self.find_end_node(end_node,distances) # Calls the "find_end_node" function with the parameters "end_node" and "distances" and stores the returned values in "end_node" and "shortest_distance".
        path_list = [end_node] # Assigns the value of the "end_node" as the first element in the list called "path_list".
        path_list = self.recursive_find_path(start_node,end_node,path_taken,path_list) # Calls the "recursive_find_path" function with the parameters "start_node", "end_node", "path_taken",and "path_list" and stored the return value in "path_list".
        path_list.reverse() # Reverses the order of elements of the list called "path_list".
        if self.stepfree == False: # If "self.stepfree" is False, then run the following lines of code.
            return shortest_distance,path_list # Returns the variable called "shortest_distance" and the list called "path_list".
        else: # If "self.stepfree" is True, then run the following lines of code.
            return distances,path_list,end_node # Returns the dictionary called "distances", the list called "path_list", and the variable called "end_node".


    def linear_search(self,target,items): # Defines the "linear_search" method which takes 2 arguments (other than the object parameter).
        # This method is used to find an element in an unordered list (performs a linear search).
        length_of_list = len(items) # Stores the length of the parameter (and list) called "items" in the variable called "length_of_list".
        for i in range(length_of_list): # For loop which is used to iterate through the "items" list as it iterates the same number of times that the length of "items" is.
            if items[i] == target: # If statement: if the element of the list we are iterating through ("items") is the same as the parameter called "target", then run the following code.
                return i # Returns i which is the index position of the target item ("target") within the list ("items").
        return -1 # If the for loop has run and the if statement within it was never run, then "target" is not in "items", so return -1 to indicate that there is no output for the given inputs (parameters).

    def find_end_node(self,end_node,distances): # Defines the "find_end_node" method which takes 2 arguments (other than the object parameter).
        # Creates an empty list called "end_stations_list" (will append values to this later).
        # For every station in  "self.stations_list", if the end_node is in this, then append it to "end_stations_list".
        # For every station in the list called "end_stations_list", calculate which station has the shortest distance in the "distances" dictionary. Store the station name in "closest_substation" and the distance in "shortest_distance".
        # Return the closest node ("end_node" and the shortest distance ("shortest_distance").
        
        end_stations_list = [] # Creates an empty list called "end_stations_list".
        for i in range (self.num_of_stations): # For loop which iterates through the elements in "self.stations_list".
            key = self.stations_list[i] # Assigns "self.stations_list[i]" to "key".
            if end_node in key: # If "end_node" is in the "key", then run the following lines of code.
                end_stations_list.append(key) # Append "key" in "end_stations_list".
        for i in range (len(end_stations_list)): # For loop which iterates through each station in "end_station_list".
            if i==0: # If i is equal to 0, run the following lines of code.
                closest_substation = end_stations_list[0]  # Assigns the first element of "end_stations_list" to the variable called "closest_substation".
                index = self.linear_search(end_stations_list[0],self.stations_list) # Calls the "linear_search" function with the parameters "end_stations_list[0]" and "self.stations_list", stores the returned value in "index".
                shortest_distance = distances[closest_substation] # Assigns the value corresponding to the key "closest_substation" in the dictionary "distances" to the variable called "shortest_distance". 
            else: # If i is not equal to 0, run the following lines of code.
                substation_key = end_stations_list[i] # Assigns "end_stations_list[i]" to the variable "substation_key".
                index = self.linear_search(end_stations_list[i],self.stations_list) # Calls the "linear_search" function with the parameters "end_stations_list[i]" and "self.stations_list", stores the returned value in "index".
                if distances[substation_key] < shortest_distance: # If the value in "shortest_distance" is greater than the value corresponding to the key "substation_key" in the dictionary "distances", 
                    closest_substation = substation_key # Assigns the value in "substation_key" to the variable "closest_substation".
                    shortest_distance = distances[closest_substation] # Assigns the valeu corresponding to the key "closest_substation" in the dictionary "distances" in the variable "shortest_distance".
        end_node = closest_substation # Assigns the value of  "closest_substation" to the variable "end_node".
        return end_node,shortest_distance # Returns the variable "end_node" and the variable "shortest_distance".

    def recursive_find_path(self,start_node,end_node,path_dict,path_list): # Defines the "recursive_find_path" method which takes 4 arguments (other than the object parameter).
        # This method is used to determine the route that the user should take. It is called wirthin the "dijkstra" function.
        # It takes the "path_dict" and "path_list" parameters and uses recursion.
        # The general case runs if the path_dict[end_node] is not the start_node.
        # The base case runs if the path_dict[end_node] is the start_node because this means that the route has been traced back from the end_node to the start_node.
        # If the general case runs, the value corresponding to path_dict[end_node] is appended to path_list and then the function calls itself, but the new end_node parameter is the value we just appended.
        # Once the base case runs, the path_list will be a list of the stations that the user should visit, but in reverse order (i.e end node to start node).
        try: # Try block for error handling.
            if path_dict[end_node] == start_node: # If the value stored in path_dict[end_node] is the same as the start_node, then run the following code.
                path_list.append(path_dict[end_node]) # Append the value stored in path_dict[end_node] to "path_list" (which is a list of all of the stations in the route).
                return path_list # Returns "path_list" which is a list containing elements which are stations in the route the user should take.
            else: # If the value stored in path_dict[end_node] is not the same as the start_node, then run the following code.
                next_node = path_dict[end_node] # Stores the value in path_dict[end_node] in the variable called "next_node".
                path_list.append(next_node) # Append the value stored in "next_node" to "path_list" (which is a list of all of the stations in the route).
                self.recursive_find_path(start_node,next_node,path_dict,path_list) # The function calls itself (uses recursion) but the parameter "end_node" is now the variable "next_node".
                return path_list # Returns "path_list" which is a list containing elements which are stations in the route the user should take.
        except: # Except block for error handling.
            pass # If there is an error, this line is run so that the error is handled.

    def correct_lines(self,line): # Defines the "correct_lines" method which takes 1 argument (other than the object parameter).
        # This method is used to adjust the text sored in the "line" parameter in order to be a string which can be outputted for the user.
        # This method uses if-elif statements to check what the value of "line" is and creates a variable called "line_text" which changes depending on what "line" is.
        if line == "CircleLine":
            line_text = "(Circle Line)"
        elif line =="CircleLineW":
            line_text =  "(Circle Line - West)"
        elif line == "CircleLineE":
            line_text =  "(Circle Line - East)"
        elif line == "CentralLine":
            line_text = "(Central Line)"
        elif line == "DistrictLine":
            line_text = "(District Line)"
        elif line =="DistrictLineW":
            line_text =  "(District Line - West)"
        elif line == "DistrictLineE":
            line_text =  "(District Line - East)"
        elif line == "VictoriaLine":
            line_text = "(Victoria Line)"
        elif line == "PiccadillyLine":
            line_text = "(Piccadilly Line)"
        elif line == "ElizabethLine":
            line_text = "(Elizabeth Line)"
        elif line == "WaterlooLine":
            line_text = "(Waterloo & City Line)"
        elif line == "HammersmithLine":
            line_text = "(Hammersmith & City Line)"
        elif line =="HammersmithLineW":
            line_text =  "(Hammersmith & City Line - West)"
        elif line == "HammersmithLineE":
            line_text =  "(Hammersmith & City Line - East)"
        elif line == "JubileeLine":
            line_text = "(Jubilee Line)"
        elif line == "NorthernLine":
            line_text = "(Northern Line)"
        elif line == "BakerlooLine":
            line_text = "(Bakerloo Line)"
        return line_text # Returns the variable called "line_text" which was created in the function.
    
    def main(self): # Defines the "main" method which takes no arguments (other than the object parameter).
        # This function is used to run all of the methods in the class sequentially.
        # It corrects station names and creates empty lists.
        # It then finds all of the lines that can be used at the start of the journey and therefore finds all possible start station keys for the adjacency dictionary.
        # It then runs the "dijkstra" function for all of the possible lines that the user can use at the start station by using a for loop.
        # Then, the start station which results in the shortest route is determined and this route is used.
        # The "output_everything" function is run and the route is displayed for the user.

        self.correct_stations() # Calls the "correct_stations" function which is used to adjust any station names which are problematic.
        possible_starts = [] # Creates an empty list called "possible_starts".
        all_shortest_distances = []  # Creates an empty list called "all_shortest_distances".
        all_path_lists = [] # Creates an empty list called "all_path_lists".
        for i in range(self.num_of_stations): # For loop which iterates through all of the stations in "stations_list".
            if self.station1 in self.stations_list[i]: # Checks if "self.station1" (the start station) is the same as "self.stations_list[i]" which is the element that is being iterated through in the loop.
                possible_starts.append(self.stations_list[i]) # Appends "self.stations_list[i]" to the list called "possible_starts". This list will contain all possible start station keys for the adjacency dictionary.
        for i in range (len(possible_starts)): # For loop which iterates through all of the elements in the "possible_starts" list. This for loop performs the "dijkstra" function for all of the possible start stations.
            start = possible_starts[i] # Assigns "possible_starts[i]" to the variable called "start".            
            end = self.station2 # Assigns "self.station2" to the variable called "end".
            shortest_distance,path_list = self.dijkstra(start,end) # Calls the "dijkstra" function using the parameters "start" and "end" and stores the returned values within "shortest_distance" , and "path_list", .
            all_shortest_distances.append(shortest_distance) # Appends the value within the variable called "shortest_distance" to a list called "all_shortest_distances".
            all_path_lists.append(path_list) # Appends the list within "path_list" to a list called "all_path_lists".
        for i in range(len(all_shortest_distances)): # For loop which iterates through all of the elements within the "all_shortest_distances" list.
            if i == 0: # If i is 0, then run the following lines of code.
                shortest = all_shortest_distances[0] # Assigns the value in "all_shortest_distances[0]" to the variable called "shortest".
                shortest_index = 0 # Assigns the value of 0 to the variable called "shortest_index".
            else: # If i is not 0, then run the following lines of code.
                if all_shortest_distances[i] < shortest: # If the value stored in "all_shortest_distances[i]" is less than the value stored in "shortest", then run the following lines of code.
                    shortest = all_shortest_distances[i] # Assigns the value in "all_shortest_distances[i]" to the variable called 'shortest".
                    shortest_index = i # Assigns the value of i to the variable called "shortest_index".
        path_list = all_path_lists[shortest_index] # Stores "all_path_lists[shortest_index]" using the identifier called "path_list".
        distance = shortest # Stores the value corresponding to the variable "shortest" using the identifier called "distance". This is the shortest time taken to reach the end node from the start node.
        self.output_everything(path_list,distance) # Calls the "output_everything" method with the parameters "path_list" and "distance". This is used to output the whole route and distance in html for the user.

        

    def output_everything(self,path_list,distance): # Defines the "output_everything" method which takes 2 arguments (other than the object parameter).
        # This method is used to create a structure for how the route is outputted for the user.
        # It starts off by using a for loop to reduce all of the elements in "path_list" to 2 parts: station and line.
        # Then, it creates a new variable for changing the value of the line into a string which is output for the user by calling the "self.correct_lines" method.
        # After this, the station part is changed to a string which is more readable for the user if it is required for the special stations (these may have line names in them, so they are different to the other stations).
        # The station and line are concatenated to create a string containing the station and line together which may be outputted later. This is appended to a list (which was empty before the loop).
        # Another for loop is used consequently to output each station and line as a html line for the user to see on the webpage.
        # Outside of the for loops, there are print statements to show the user the amount of time taken for the journey and links for the user to return to the previous page if they wish to.
        
        # Objectives 8, 8.1, 8.2:
        
        texts = [] # Creates an empty list called "texts".
        for i in range(len(path_list)): # For loop iterates the same number of times as the length of the list called "path_list".
            item = path_list[i] # Assigns the iterated element of path_list to the variable called "item".
            item_list = item.split() # Uses built-in function called "split" to separate the words (station and line) in the variable called "item" and stores this in the list called "item_list".
            line_used = item_list[-1] # Assigns the last element of the list called "item_list" to the variable called "line_used".
            item_list.pop(-1) # The last element of the list called "item_list" is popped/removed.
            if line_used != "EXIT": # If statement to ensure that if the "line_used" variable is not "EXIT", then run the following lines of code.
                line_text = self.correct_lines(line_used) # Since the "line_used" is not "EXIT", "line_used" is a valid line. Therefore, the method called "self.correct_lines" is called with the argument "line_used" and the returned value is stored in the variable called "line_text".
            else: # If the "line_used" is "EXIT", then there is no line used for this part of the route, so run the following lines of code.
                line_text = "(Street)" # Assigns a string to the variable "line_text" to indicate that this part of the route involves reaching the street and not using the tube again.
            text = "" # Assigns an empty string to the variable called "text".
            for j in range(len(item_list)): # For loop: iterates through the list called "item_list" in order to change station names if necessary and to add a space (" ") at the end of the station name.
                element = item_list[j] # Stores the value in item_list[j] in the variable called "element".
                # If-elif statements to change the names of stations if they are ones which contain other station names or line names within them.
                if element == "VictoriaStation":
                    element = "Victoria"
                elif element == "PiccadillyCircus":
                    element = "Piccadilly Circus"
                elif element == "WaterlooStation":
                    element = "Waterloo"
                elif element == "EustonStation":
                    element = "Euston"
                elif element == "AldgateStation":
                    element = "Aldgate"
                text += element + " " # Concatenates the variable called "text" with the variable called "element" and a space (" ") and stoes it in the variable called "text".
            text += line_text # Concatenates the variable called "text" with the variable called "line_text" and stores it in the variable called "text".
            texts.append(text) # Appends the value of "text" to the list called "texts".
        for i in range(len(texts)): # For loop which iterates through the list called "texts" (which contains elements which are the station and line together for the route).
            if i != len(texts)-1: # If i is not equal to the lenght of the list - 1, then run the folowing code.
                texts[i] = texts[i] + " -->" # Appends "-->" to the string stored in texts[i] and stores this within texts[i].
            print("<h2> %s</h2>" % texts[i]) # html line: outputs the station and line that the user needs to visit as part of the route.
        text2 = "Approximated Time: " + str(round(distance / 60)) + " minutes" # Creates a string which is used to output the estimated time that the journey will take.
        print("<h3> %s</h3>" % text2) # html line: outputs the time taken for the user to complete the journey.
        print("<h3> Want to plan another journey? </h3>") # html line: outputs text on the webpage.
        print ("<a href='../journeyplanner.html'>Journey Planner <a>") # html line: outputs a link for the user to use if they want to return to the previous webpage.

      
class StepFreeJourneyPlanner(JourneyPlanner): # Creates a class for the step free journey planner called "StepFreeJourneyPlanner" which inherits the methods and attributes from the "JourneyPlanner" class.
    def __init__(self,station1,station2,rush_hour,weekend): # Defines the constructor method which takes 4 arguments (other than the object parameter).
        # This method is used to define class attributes.

        self.station1 = station1 # Assigns value stored in the parameter "station1" as the "self.station1" attribute.
        self.station2 = station2 # Assigns value stored in the parameter "station2" as the "self.station2" attribute.
        self.rush_hour = rush_hour # Assigns value stored in the parameter "rush_hour" as the "self.rush_hour" attribute.
        self.weekend = weekend # Assigns value stored in the parameter "weekend" as the "self.weekend" attribute.

        # Objectives 1.3, 1.4, 1.5:
        #Objectives 2.1, 2.2:
        #Objective 7, 7.2:

        # Creates an adjacency dictionary attribute called "self.stations_adjacency_dict" containing keys which represent the station you are at, and values which are dictionaries as well.
        # These dictionaries contain keys which represent the station you can travel to, and the values are the number of seconds taken to travel there.
        # The difference between this adjacency dictionary and the one from the "JourneyPlanner" class is that this one has limited access, so the adjacency dictionary may have some stations where you can only travel east on a certain line, or some stations that cannot be accessed, etc.
        # Step-free stations_adjacency_dict:
        self.stations_adjacency_dict= {
            "Paddington CircleLineE": {"Edgware Road CircleLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington DistrictLineE": 300,"Paddington HammersmithLine":300,"Paddington EXIT":300},
            "Paddington DistrictLineE": {"Edgware Road DistrictLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington CircleLineE": 300,"Paddington HammersmithLine":300,"Paddington EXIT":300},
            "Paddington CircleLineW": {"South Kensington CircleLine":487.4,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington DistrictLineW": 300,"Paddington HammersmithLine":300},
            "Paddington DistrictLineW": {"Earl's Court DistrictLine":545.5,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington CircleLineW": 300,"Paddington HammersmithLine":300},
            "Paddington HammersmithLine":{"Edgware Road HammersmithLine":110.8,"Paddington BakerlooLine":300,"Paddington ElizabethLine": 300,"Paddington CircleLineE": 300,"Paddington DistrictLineE":300,"Paddington EXIT":300},
            "Paddington BakerlooLine": {"Baker Street BakerlooLine":208.7, "Paddington ElizabethLine": 300,"Paddington DistrictLineE": 300,"Paddington CircleLineE": 300,"Paddington HammersmithLine":300,"Paddington EXIT":300},
            "Paddington ElizabethLine": {"Tottenham Court Road ElizabethLine":241.6,"Paddington BakerlooLine":300,"Paddington DistrictLineE": 300,"Paddington CircleLineE": 300,"Paddington HammersmithLine":300},
            "Paddington EXIT": {"Paddington ElizabethLine":300,"Paddington BakerlooLine":300,"Paddington HammersmithLine":300,"Paddington DistrictLineE":300,"Paddington CircleLineE":300},
            "Earl's Court DistrictLine": {"Paddington DistrictLineE":545.5, "South Kensington DistrictLine":175.6, "Earl's Court PiccadillyLine":300,"Earl's Court EXIT":300},
            "Earl's Court PiccadillyLine": {"Green Park PiccadillyLine":511.9, "Earl's Court DistrictLine":300,"Earl's Court EXIT":300},
            "Earl's Court EXIT": {"Earl's Court DistrictLine":300,"Earl's Court PiccadillyLine":300},
            "South Kensington CircleLine": {"VictoriaStation CircleLine":199.1,"Paddington CircleLineE":487.4,"South Kensington DistrictLine":300,"South Kensington EXIT":300},
            "South Kensington DistrictLine": {"VictoriaStation DistrictLine":199.1,"South Kensington CircleLine":300,"South Kensington EXIT":300},
            "South Kensington EXIT": {"South Kensington CircleLine":300,"South Kensington DistrictLine":300},         
            "VictoriaStation CircleLine": {"South Kensington CircleLine":199.1,"Westminster CircleLine":161.2,"VictoriaStation DistrictLine":300,"VictoriaStation VictoriaLine":300,"VictoriaStation EXIT":300},
            "VictoriaStation DistrictLine": {"South Kensington DistrictLine":199.1,"Westminster DistrictLine":161.2,"VictoriaStation CircleLine":300,"VictoriaStation VictoriaLine":300,"VictoriaStation EXIT":300},
            "VictoriaStation VictoriaLine": {"Vauxhall VictoriaLine":144.4,"Green Park VictoriaLine":78.4,"VictoriaStation CircleLine":300,"VictoriaStation DistrictLine":300,"VictoriaStation EXIT":300},
            "VictoriaStation EXIT": {"VictoriaStation CircleLine":300,"VictoriaStation DistrictLine":300,"VictoriaStation VictoriaLine":300},
            "Westminster CircleLine": {"VictoriaStation CircleLine":161.2,"Blackfriars CircleLine":234.6,"Westminster DistrictLine":300,"Westminster JubileeLine":300,"Westminster EXIT":300},
            "Westminster DistrictLine": {"VictoriaStation DistrictLine":161.2,"Blackfriars DistrictLine":234.6,"Westminster CircleLine":300,"Westminster JubileeLine":300,"Westminster EXIT":300},
            "Westminster JubileeLine": {"WaterlooStation JubileeLine":78.1,"Green Park JubileeLine":99.8,"Westminster DistrictLine":300,"Westminster CircleLine":300,"Westminster EXIT":300},
            "Westminster EXIT": {"Westminster DistrictLine":300,"Westminster CircleLine":300,"Westminster JubileeLine":300},
            "Blackfriars CircleLine": {"Cannon Street CircleLineE":152.8,"Westminster CircleLine":234.6,"Blackfriars DistrictLine":300,"Blackfriars EXIT":300},
            "Blackfriars DistrictLine": {"Cannon Street DistrictLineE":152.8,"Westminster DistrictLine":234.6,"Blackfriars CircleLine":300,"Blackfriars EXIT":300},
            "Blackfriars EXIT": {"Blackfriars CircleLine":300,"Blackfriars DistrictLine":300},
            "Cannon Street CircleLineW": {"Blackfriars CircleLine":152.8,"Cannon Street DistrictLineW":300,"Cannon Street EXIT":300},
            "Cannon Street DistrictLineW": {"Blackfriars DistrictLine":152.8,"Cannon Street CircleLineW":300,"Cannon Street EXIT":300},
            "Cannon Street CircleLineE": {"Tower Hill CircleLine":158.8,"Cannon Street DistrictLineE":300},
            "Cannon Street DistrictLineE": {"Tower Hill DistrictLine":158.8,"Cannon Street CircleLineE":300},
            "Cannon Street EXIT": {"Cannon Street CircleLineW":300,"Cannon Street DistrictLineW":300},
            "Tower Hill CircleLine": {"Cannon Street CircleLineW":158.8,"Liverpool Street CircleLineW":198.8,"Tower Hill DistrictLine":300,"Tower Hill EXIT":300},
            "Tower Hill DistrictLine": {"Cannon Street DistrictLineW":158.8,"Aldgate East DistrictLine":132.9,"Tower Hill CircleLine":300,"Tower Hill EXIT":300},
            "Tower Hill EXIT": {"Tower Hill CircleLine":300,"Tower Hill DistrictLine":300},
            "Aldgate East DistrictLine": {"Tower Hill DistrictLine":132.9,"Aldgate East HammersmithLine":300,"Aldgate East EXIT":300},
            "Aldgate East HammersmithLine": {"Liverpool Street HammersmithLineW":128.4,"Aldgate East DistrictLine":300,"Aldgate East EXIT":300},
            "Aldgate East EXIT": {"Aldgate East DistrictLine":300,"Aldgate East HammersmithLine":300},
            "Liverpool Street CircleLineE": {"Tower Hill CircleLine":198.8,"Liverpool Street HammersmithLineE":300,"Liverpool Street ElizabethLine":300,"Liverpool Street EXIT":300},
            "Liverpool Street HammersmithLineE": {"Aldgate East HammersmithLine":128.4,"Liverpool Street CircleLineE":300,"Liverpool Street ElizabethLine":300,"Liverpool Street EXIT":300},
            "Liverpool Street CircleLineW": {"Moorgate CircleLine":70.6,"Liverpool Street HammersmithLineW":300,"Liverpool Street ElizabethLine":300},
            "Liverpool Street HammersmithLineW": {"Moorgate HammersmithLine":70.6,"Liverpool Street CircleLineW":300,"Liverpool Street ElizabethLine":300},
            "Liverpool Street ElizabethLine": {"Farringdon ElizabethLine":96.0, "Liverpool Street CircleLineE":300,"Liverpool Street HammersmithLineE":300,"Liverpool Street EXIT":300},
            "Liverpool Street EXIT": {"Liverpool Street CircleLineE":300,"Liverpool Street HammersmithLineE":300,"Liverpool Street ElizabethLine":300},
            "Moorgate CircleLine": {"Liverpool Street CircleLineE":70.6,"Barbican CircleLineW":72.1,"Moorgate HammersmithLine":300,"Moorgate NorthernLine":300,"Moorgate EXIT":300},
            "Moorgate HammersmithLine": {"Liverpool Street HammersmithLineE":70.6,"Barbican HammersmithLineW":72.1,"Moorgate CircleLine":300,"Moorgate NorthernLine":300,"Moorgate EXIT":300},
            "Moorgate NorthernLine": {"King's Cross St. Pancras NorthernLine":341.6,"London Bridge NorthernLine":168.3,"Moorgate CircleLine":300,"Moorgate HammersmithLine":300,"Moorgate EXIT":300},
            "Moorgate EXIT": {"Moorgate CircleLine":300,"Moorgate HammersmithLine":300,"Moorgate NorthernLine":300},
            "Barbican CircleLineE": {"Moorgate CircleLine":72.1,"Barbican HammersmithLineE":300},
            "Barbican HammersmithLineE": {"Moorgate HammersmithLine":72.1,"Barbican CircleLineE":300},
            "Barbican CircleLineW": {"Farringdon CircleLine":67.6,"Barbican HammersmithLineW":300,"Barbican EXIT":300},
            "Barbican HammersmithLineW": {"Farringdon HammersmithLine":67.6,"Barbican CircleLineW":300,"Barbican EXIT":300},
            "Barbican EXIT": {"Barbican CircleLineW":300,"Barbican HammersmithLineW":300},
            "Farringdon ElizabethLine": {"Liverpool Street ElizabethLine":96.0,"Tottenham Court Road ElizabethLine":138.8,"Farringdon CircleLine":300,"Farringdon HammersmithLine":300,"Farringdon EXIT":300},
            "Farringdon CircleLine": {"Barbican CircleLineE":67.6,"King's Cross St. Pancras CircleLine":164.0,"Farringdon ElizabethLine":300,"Farringdon HammersmithLine":300,"Farringdon EXIT":300},
            "Farringdon HammersmithLine": {"Barbican HammersmithLineE":67.6,"King's Cross St. Pancras HammersmithLine":164.0,"Farringdon ElizabethLine":300,"Farringdon CircleLine":300,"Farringdon EXIT":300},
            "Farringdon EXIT": {"Farringdon ElizabethLine":300,"Farringdon CircleLine":300,"Farringdon HammersmithLine":300},
            "King's Cross St. Pancras CircleLine": {"Farringdon CircleLine":164.0,"Euston Square CircleLineW":83.2,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300,"King's Cross St. Pancras EXIT":300},
            "King's Cross St. Pancras HammersmithLine": {"Farringdon HammersmithLine":164.0,"Euston Square HammersmithLineW":83.2,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300,"King's Cross St. Pancras EXIT":300},
            "King's Cross St. Pancras NorthernLine": {"Moorgate NorthernLine":341.6,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras PiccadillyLine":300,"King's Cross St. Pancras EXIT":300},
            "King's Cross St. Pancras VictoriaLine": {"EustonStation VictoriaLine":87.4,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras PiccadillyLine":300,"King's Cross St. Pancras EXIT":300},
            "King's Cross St. Pancras PiccadillyLine": {"Green Park PiccadillyLine":441.4,"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras EXIT":300},
            "King's Cross St. Pancras EXIT": {"King's Cross St. Pancras HammersmithLine":300,"King's Cross St. Pancras NorthernLine":300,"King's Cross St. Pancras VictoriaLine":300,"King's Cross St. Pancras CircleLine":300,"King's Cross St. Pancras PiccadillyLine":300},
            "Euston Square CircleLineE": {"King's Cross St. Pancras CircleLine":83.2,"Euston Square HammersmithLineE":300},
            "Euston Square HammersmithLineE": {"King's Cross St. Pancras HammersmithLine":83.2,"Euston Square CircleLineE":300},
            "Euston Square CircleLineW": {"Edgware Road CircleLine":110.8,"Euston Square HammersmithLineW":300,"Euston Square EXIT":300},
            "Euston Square HammersmithLineW": {"Edgware Road HammersmithLine":110.8,"Euston Square CircleLineW":300,"Euston Square EXIT":300},
            "Euston Square EXIT": {"Euston Square CircleLineW":300,"Euston Square HammersmithLineW":300},
            "Baker Street BakerlooLine": {"Oxford Circus BakerlooLine":204.7,"Paddington BakerlooLine":208.7,"Baker Street JubileeLine":300,"Baker Street EXIT":300},
            "Baker Street JubileeLine": {"Bond Street JubileeLine":112.5,"Baker Street BakerlooLine":300,"Baker Street EXIT":300},
            "Baker Street EXIT": {"Baker Street JubileeLine":300,"Baker Street BakerlooLine":300},
            "Edgware Road CircleLine": {"Euston Square CircleLineE":265.0,"Paddington CircleLineW":110.8,"Edgware Road HammersmithLine":300,"Edgware Road DistrictLine":300,"Edgware Road EXIT":300},
            "Edgware Road HammersmithLine": {"Euston Square HammersmithLineE":265.0,"Paddington HammersmithLine":110.8,"Edgware Road CircleLine":300,"Edgware Road DistrictLine":300,"Edgware Road EXIT":300},
            "Edgware Road DistrictLine": {"Paddington DistrictLineW":93.1,"Edgware Road HammersmithLine":300,"Edgware Road CircleLine":300,"Edgware Road EXIT":300},
            "Edgware Road EXIT": {"Edgware Road HammersmithLine":300,"Edgware Road CircleLine":300,"Edgware Road DistrictLine":300},
            "EustonStation VictoriaLine": {"King's Cross St. Pancras VictoriaLine":87.4,"Oxford Circus VictoriaLine":130.2,"EustonStation EXIT":300},
            "EustonStation EXIT": {"EustonStation VictoriaLine":300},
            "Bond Street CentralLine": {"Tottenham Court Road CentralLine":153.6,"Bond Street JubileeLine":300,"Bond Street EXIT":300},
            "Bond Street JubileeLine": {"Baker Street JubileeLine":112.5,"Green Park JubileeLine":94.3,"Bond Street CentralLine":300,"Bond Street EXIT":300},
            "Bond Street EXIT": {"Bond Street CentralLine":300,"Bond Street JubileeLine":300},
            "Green Park JubileeLine": {"Bond Street JubileeLine":94.3,"Westminster JubileeLine":99.8,"Green Park PiccadillyLine":300,"Green Park VictoriaLine":300,"Green Park EXIT":300},
            "Green Park PiccadillyLine": {"Earl's Court PiccadillyLine":511.9,"King's Cross St. Pancras PiccadillyLine":441.4,"Green Park JubileeLine":300,"Green Park VictoriaLine":300,"Green Park EXIT":300},
            "Green Park VictoriaLine": {"Oxford Circus VictoriaLine":77.6,"VictoriaStation VictoriaLine":78.4,"Green Park PiccadillyLine":300,"Green Park JubileeLine":300,"Green Park EXIT":300},
            "Green Park EXIT": {"Green Park PiccadillyLine":300,"Green Park JubileeLine":300,"Green Park VictoriaLine":300},
            "Oxford Circus BakerlooLine": {"Baker Street BakerlooLine":204.7,"Oxford Circus VictoriaLine":300,"Oxford Circus EXIT":300},
            "Oxford Circus VictoriaLine": {"Green Park VictoriaLine":77.6,"EustonStation VictoriaLine":130.2,"Oxford Circus BakerlooLine":300,"Oxford Circus EXIT":300},
            "Oxford Circus EXIT": {"Oxford Circus BakerlooLine":300,"Oxford Circus VictoriaLine":300},
            "Tottenham Court Road CentralLine": {"Bond Street CentralLine":153.6,"Tottenham Court Road ElizabethLine":300,"Tottenham Court Road NorthernLine":300,"Tottenham Court Road EXIT":300},
            "Tottenham Court Road ElizabethLine": {"Farringdon ElizabethLine":138.8,"Paddington ElizabethLine":241.6,"Tottenham Court Road CentralLine":300,"Tottenham Court Road NorthernLine":300,"Tottenham Court Road EXIT":300},
            "Tottenham Court Road NorthernLine": {"Kennington NorthernLine":325.5,"Tottenham Court Road ElizabethLine":300,"Tottenham Court Road CentralLine":300,"Tottenham Court Road EXIT":300},
            "Tottenham Court Road EXIT": {"Tottenham Court Road ElizabethLine":300,"Tottenham Court Road CentralLine":300,"Tottenham Court Road NorthernLine":300,"Tottenham Court Road EXIT":300},
            "WaterlooStation JubileeLine": {"Westminster JubileeLine":78.1,"Southwark JubileeLine":49.5,"WaterlooStation EXIT":300},
            "WaterlooStation EXIT": {"WaterlooStation JubileeLine":300},
            "Southwark JubileeLine": {"WaterlooStation JubileeLine":49.5,"London Bridge JubileeLine":92.2,"Southwark EXIT":300},
            "Southwark EXIT": {"Southwark JubileeLine":300},
            "London Bridge JubileeLine": {"Southwark JubileeLine":92.2,"London Bridge NorthernLine":300,"London Bridge EXIT":300},
            "London Bridge NorthernLine": {"Moorgate NorthernLine":168.3,"Borough NorthernLine":79.0,"London Bridge JubileeLine":300,"London Bridge EXIT":300},
            "London Bridge EXIT": {"London Bridge JubileeLine":300,"London Bridge NorthernLine":300},
            "Borough NorthernLine": {"Elephant & Castle NorthernLine":94.2,"London Bridge NorthernLine":79.0,"Borough EXIT":300},
            "Borough EXIT": {"Borough NorthernLine":300},
            "Elephant & Castle NorthernLine": {"Borough NorthernLine":94.2,"Kennington NorthernLine":100.7,"Elephant & Castle EXIT":300},
            "Elephant & Castle EXIT": {"Elephant & Castle NorthernLine":300},
            "Battersea Power Station NorthernLine": {"Nine Elms NorthernLine":98.8,"Battersea Power Station EXIT":300},
            "Battersea Power Station EXIT": {"Battersea Power Station NorthernLine":300},
            "Nine Elms NorthernLine": {"Battersea Power Station NorthernLine":98.8,"Kennington NorthernLine":168.5,"Nine Elms EXIT":300},
            "Nine Elms EXIT": {"Nine Elms NorthernLine":300},
            "Kennington NorthernLine": {"Nine Elms NorthernLine":168.5,"Tottenham Court Road NorthernLine":325.5,"Elephant & Castle NorthernLine":100.7,"Kennington EXIT":300},
            "Kennington EXIT": {"Kennington NorthernLine":300},
            "Vauxhall VictoriaLine": {"VictoriaStation VictoriaLine":144.4,"Vauxhall EXIT":300},
            "Vauxhall EXIT": {"Vauxhall VictoriaLine":300}
            }
        self.stations_list = list(self.stations_adjacency_dict.keys()) # Assigns keys of the stations adjacency dictionary as the "self.stations_list" attribute.
        self.num_of_stations = len(self.stations_list) # Assigns the length of the stations adjacency dictionary as the "self.num_of_stations" attribute.
        self.stepfree = True # Assigns the Boolean True value as the "self.stepfree" attribute.


    def main(self): # Defines the "main" method which takes no arguments (other than the object parameter). This method overrides the "main" method from the "JourneyPlanner" class.
        # This function is used to run all of the methods in the class sequentially.
        # It corrects station names and checks if the inputted stations are valid for a step-free journey.
        # If the inputs are not valid, then an appropriate error messgae is displayed.
        # If the inputs are valid, then the "dijkstra" function is run.
        # Then, the "output_everything" function is run and the route is displayed for the user.
        
        valid_start = False # Creates a variable called "valid_start" and sets it to the Boolean value False.
        valid_end = False # Creates a variable called "valid_end" and sets it to the Boolean value False.
        if self.station1 == "Aldgate":
            self.station1 = "AldgateStation"
        elif self.station1 == "Euston":
            self.station1 = "EustonStation"
        if self.station2 == "Aldgate":
            self.station2 = "AldgateStation"
        elif self.station2 == "Euston":
            self.station2 = "EustonStation"
        for i in range(self.num_of_stations): # For loop to iterate through all of the stations that can be visited in a step-free journey.
            key = self.stations_list[i] # Stores the element in the list called "self.stations_list" corresponding to the index position i in the variable called "key".
            if self.station1 in key: # If the value within the variable "self.station1" is in key, run the following code.
                valid_start = True # Sets the variable "valid_start" to the Boolean value True.
            if self.station2 in key: # If the value within the variable "self.station2" is in key, run the following code.
                valid_end = True # Sets the variable "valid_end" to the Boolean value True.
        if valid_start == True and valid_end == True: # If "valid_start" and "valid_end" are both True (the inputs are valid), then run the following lines of code.
            self.correct_stations() # Calls the "correct_stations" function which is used to adjust any station names which are problematic.
            start_node = self.station1 + " EXIT" # Concatenates the string in the variable called "self.station1" with " EXIT" and stores this in the variable called "start_node".
            end_node = self.station2 + " EXIT" # Concatenates the string in the variable called "self.station2" with " EXIT" and stores this in the variable called "end_node".
            distances,path_list,end_node = self.dijkstra(start_node,end_node) # Calls the "dijkstra" function using the parameters "start_node" and "end_node" and stores the returned values within "distances" , "path_list", and "end_node".
            distance = distances[end_node] # Stores the value corresponding to the key "end_node" in the "distances" dictionary using the identifier called "distance". This is the shortest time taken to reach the end node from the start node.
            self.output_everything(path_list,distance) # Calls the "output_everything" method with the parameters "path_list" and "distance". This is used to output the whole route and distance in html for the user.
        else: # If "valid_start" and "valid_end" are not True together (the inputs are invalid), then run the following lines of code.
            print("<h2> Sorry, you have entered a station without any step free access but have chosen step free mode :( </h2>") # html line: outputs a messge on the webpage which tells the user that they have invalid inputs.
            print("<h2> You can re-enter a route here: </h2>") # html line: outputs text on the webpage.
            print ("<a href='../journeyplanner.html'>Journey Planner <a>") # html line: outputs a link for the user to use if they want to return to the previous webpage.

#station1="Piccadilly Circus"
#station2="Cannon Street"
#rush_hour="No"
#weekend="No"
#step_free = "No"
            
if step_free == "No": # If the user has inputted "No" when asked if they want a step free journey, then the journey will use the normal adjacency dictionary and the normal "JourneyPlanner" class.
    jp = JourneyPlanner(station1,station2,rush_hour,weekend) # Instantiation: creates an object called "jp" using the "JourneyPlanner" class with 4 arguments.
    jp.main()  # Calls the method called "main" in the "jp" object.
else: # If the user has inputted "Yes" when asked if they want a step free journey, then the journey will use the adjusted adjacency dictionary and the "StepFreeJourneyPlanner" class.
    sf_jp = StepFreeJourneyPlanner(station1,station2,rush_hour,weekend) # Instantiation: creates an object called "sf_jp" using the "StepFreeJourneyPlanner" class with 4 arguments.
    sf_jp.main() # Calls the method called "main" in the "sf_jp" object.

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
