import smbus2
import bme280
def pull_weather():
    # Get the pi setup/pin  out
    # https://www.waveshare.com/w/upload/7/75/BME280_Environmental_Sensor_User_Manual_EN.pdf
    # https://bme280.readthedocs.io/en/latest/
    # https://www.amazon.com/dp/B07P4CWGGK?psc=1&ref=ppx_yo2_dt_b_product_details
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    weather = {}
    # the compensated_reading class has the following attributes
    weather["ID"]= data.id
    weather["Time"]=data.timestamp
    weather["Temp"]=data.temperature
    weather["Pressure"]=data.pressure
    weather["Humidity"]=data.humidity
    return weather