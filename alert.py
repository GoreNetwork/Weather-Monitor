import socket
from send_text_message import send_txt_message
from monitor import pull_weather

# Set this up to run in crontab once an hour with crontab -e
# and add the path to alert.py
# 15 * * * * python3 /home/pi/weather_monitor/alert.py
# Runs any time the minute marker is at 15 (so at 1:15, 2:15, 12:15, etc)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip=s.getsockname()[0]

# ip = str(socket.gethostbyname(socket.gethostname()))
hostname = socket.gethostname()
weather = pull_weather()
Fahrenheit = (weather["Temp"] * 9/5) + 32
Fahrenheit=int(Fahrenheit)
Fahrenheit=str(Fahrenheit)
humidity = int(weather['Humidity'])
humidity = str(humidity)
message = "in {}: {} it is {}F with a humidity of {}%".format(
    hostname, ip, Fahrenheit, humidity
)

if int(weather['Humidity'])>61:
    send_txt_message(message)