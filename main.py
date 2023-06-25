from confg import Settings

from selenium import webdriver
from selenium.webdriver.common.by import By



def main():
    settings = Settings()
    driver = webdriver.Chrome()
    print("Starting")
    driver.get(settings.WEATHER_WEB_URL)
    driver.find_element(by=By.XPATH, value='//*[@id="portlet_weathercurrent_WAR_weatherportlet"]/div/div/div/div[2]/ul/li[1]/a').click()
    charts = driver.find_elements(by=By.CLASS_NAME, value="chart_box")
    for index, chart in enumerate(charts):
        chart.screenshot(f"./screenshot{index}.png")
    print("Chart")
    print(charts)
    print("Ended")

if __name__ == "__main__":
    main()