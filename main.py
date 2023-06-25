from confg import Settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

import time
import logging

logging.basicConfig(level="INFO")

def main():
    hourly_temperatures = []
    settings = Settings()
    driver = webdriver.Chrome()
    logging.warning("Starting")
    driver.get(settings.WEATHER_WEB_URL)
    hourly_chart_selector = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(by=By.XPATH, value='//ul[@class="tabs_nav"]/li/a[contains(text()," 48 hours ")]'))
    if hourly_chart_selector.is_displayed():

        try: 
            hover = ActionChains(driver).move_to_element(hourly_chart_selector)
            hover.perform()
            hourly_chart_selector.click()
            ActionChains(driver).move_by_offset("100", "100")

        except ElementClickInterceptedException:
            time.sleep(5)
            hourly_chart_selector = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(by=By.XPATH, value='//ul[@class="tabs_nav"]/li/a[contains(text()," 48 hours ")]'))

            hourly_chart_selector.click()

    # driver.find_element(by=By.XPATH, value='//div[@class="left"]').click()
    charts = driver.find_elements(by=By.CLASS_NAME, value="chart-box")
    logging.info("Saving screenshots")
    # for index, chart in enumerate(charts):
    #     chart.screenshot(f"./screenshot{index}.png")
    
    temperature_chart = driver.find_element(by=By.XPATH, value='//div[@id="chart_temperature"]')
    temperature_circles = temperature_chart.find_elements(by=By.TAG_NAME, value='circle')
    for index, circle in enumerate(temperature_circles):
        logging.info(f"Moving to the {index} circle element")
        hover = ActionChains(driver).move_to_element(circle)
        hover.perform()
        logging.info("Finding the hover state box")
        temperature_box = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(by=By.XPATH, value='//div[@id="chart_temperature"]/div/div[3]'))
        if temperature_box.is_displayed():
            logging.info("Temperature box is displayed")
            
        hour_stats = temperature_box.find_elements(by=By.TAG_NAME, value="span")
        if hour_stats:
            hourly_temperatures.append({"hour":hour_stats[1].text, "temperature": hour_stats[0].text})

        ActionChains(driver).move_by_offset("100", "100")

    driver.quit()
    print(hourly_temperatures)
    logging.warning("Ended")

if __name__ == "__main__":
    main()