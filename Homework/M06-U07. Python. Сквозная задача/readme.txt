Hello
we have two codes for our project
1) server.py
2) script.py

server.py
first you need to run server.py after you run you will see a url, and you have to use this url as target.
Server.py is actually our api which we will call through requests
this api have two end points
/sendhttp [accept post request]
/scan [accept get request]

so your target will something like

url/sendhttp [you will get the url when your run the server] and you need to pass it as target

you need to install few python packages, Flask (pip install Flask)

after your server is running

you will interact with script.py
you will made your header payload body through it and it will call the server for furthur response