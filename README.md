# rpi3bp-sensehat-flask-server-py
Using flask and python to display sense hat environmental data (temperature, pressure, and humidity) remotely via the following:
<localhost/temperature>
<localhost/pressure>
<localhost/humidity>

On your webserver (rpi3bp in my caase) type:

$ export FLASK_APP=server.py     # use set instead of export on Windows

$ export FLASK_DEBUG=1           # use set instead of export on Windows

$ flask run

or

pi@rpi3bp:~/sensehat $ sudo python3 server.py 

 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 193-365-982

Note: localhost = ip address of your webserver (rpi3bp in my case).

Then...

in any client browser on your local network, issue <localhost/pressure> displays "Pressure 29.0inHg recorded at 09:15:44"
and on the server side (Raspberry Pi), you should see something similar to this ->
192.168.254.23 - - [05/Mar/2021 09:15:44] "GET /pressure HTTP/1.1" 200 -

in any client browser on your local network, issue <localhost/temperature> displays "Temperature 75.1° recorded at 09:16:17"
and on the server side (Raspberry Pi), you should see something similar to this ->
192.168.254.23 - - [05/Mar/2021 09:16:17] "GET /temperature HTTP/1.1" 200 -

in any client browser on your local network, issue <localhost/humidity> displays "Humidity 44.6% recorded at 09:16:29"
and on the server side (Raspberry Pi), you should see something similar to this ->
192.168.254.23 - - [05/Mar/2021 09:16:29] "GET /humidity HTTP/1.1" 200 -


