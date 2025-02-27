from http.server import HTTPServer, CGIHTTPRequestHandler # Import modules which will be used later in the program.
# HTTPServer is a class which is needed in the program.
# CGIHTTPRequestHandler is a class needed to create the handler object.


# Objective 10:
class Handler(CGIHTTPRequestHandler): # Creates the class called "handler" which is used when a form is submitted.
# Takes the class CGIHTTPRequestHandler as an argument so that the attributes and behaviours are inherited.
    cgi_directories = ["/cgi-bin"] # Sets the variable "cgi_directories" to "/cgi-bin" which ensures that the scripts which are in the "cgi-bin" folder run when forms are submitted.

print("Webserver running on port 8080") # A print statement to show that the webserver is running, since nothing else will be printed in the console.

# Objective 10.1:
HTTPServer(("",  8080), Handler).serve_forever()
# HTTPServer is a class which takes 2 arguments:
# Arg 1: server address: the address to listen to ("" is localhost) and the port number to listen to (80 as this is the port used for http by convention)
# Arg 2: request handler class: Handler class, which was defined earlier, is used in order to know where cgi scripts are and to handle all requests.
# .serve_forever() ensures that, when the program is run, the web server runs constantly.


#http://localhost:8080/journeyplanner.html
#ngrok http 8080
