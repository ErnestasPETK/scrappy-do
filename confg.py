from pydantic import BaseSettings

class Settings(BaseSettings):
    WEATHER_WEB_URL : str = "http://www.meteo.lt/en/miestas?placeCode=Vilnius" 
    DRIVER_PATH :str = "./chromedriver"
