from website import create_app
app= create_app()

#only if we run this file are we going to execute this line
#runs flask application and starts up flask web server. turn this off if in production. 
# this is the entry point for the app
if __name__ == '__main__':
    app.run(debug=True)