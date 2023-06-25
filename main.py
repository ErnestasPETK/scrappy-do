from confg import Settings

#! Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException
# from selenium.webdriver.common.action_chains import ActionChains


#! Scrapy

import time
import logging

logging.basicConfig(level="INFO")

def main():
    # selenium
    # ==========================================
    # hourly_temperatures = []
    # settings = Settings()
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    # logging.warning("Starting")
    # driver.get(settings.WEATHER_WEB_URL)
    # hourly_chart_selector = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH,'//ul[@class="tabs_nav"]/li/a[contains(text()," 48 hours ")]')))
    # # hourly_chart_selector = driver.find_element(by=By.XPATH, value='//ul[@class="tabs_nav"]/li/a[contains(text()," 48 hours ")]')
    # # ActionChains(driver).scroll_by_amount("500","500")
    # if hourly_chart_selector.is_displayed():
    #     try: 
    #         hourly_chart_selector.click()
    #     except ElementClickInterceptedException:
    #         logging.error(" Hourly chart selector not present")
    #         time.sleep(5)
    #         hourly_chart_selector.click()
    # else:
    #     logging.error("Unable to find hourly_chart_selector")
    # # driver.find_element(by=By.XPATH, value='//div[@class="left"]').click()
    # charts = driver.find_elements(by=By.CLASS_NAME, value="chart-box")
    
    # logging.info("Saving screenshots")
    # # for index, chart in enumerate(charts):
    # #     chart.screenshot(f"./screenshot{index}.png")
    # # time.sleep(5)
    # # temperature_chart = driver.find_element(by=By.XPATH, value='//div[@id="chart_temperature"]')
    # temperature_chart = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="chart_temperature"]')))


    # # temperature_circles = temperature_chart.find_elements(by=By.TAG_NAME, value='circle')
    # temperature_circles = WebDriverWait(temperature_chart, timeout=10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'circle')))

    # if temperature_circles:
    #     logging.info("Circles found")
    # print(temperature_circles)
    # for index, circle in enumerate(temperature_circles):
    #     try:
    #         logging.info(f"Moving to the {index} circle element")
    #         ActionChains(driver).move_to_element(circle).perform()
    #         logging.info("Finding the hover state box")
    #         # temperature_box = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(by=By.XPATH, value='//div[@id="chart_temperature"]/div/div[3]'))
    #         temperature_box = WebDriverWait(temperature_chart, timeout=5, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH,'//div[@id="chart_temperature"]/div/div[3]')))
            
    #         if temperature_box.is_displayed():
    #             logging.info("Temperature box is displayed")
                
    #         # hour_stats = temperature_box.find_elements(by=By.TAG_NAME, value="span")
    #         hour_stats = WebDriverWait(driver, timeout=10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'span')))

    #         if hour_stats:
    #             hourly_temperatures.append({"hour":hour_stats[1].text, "temperature": hour_stats[0].text})

    #         ActionChains(driver).move_by_offset(1000,100).perform()

    #     except Exception as err:
    #         logging.error(f"Unable to collect data from {index} circle")

    # driver.quit()
    # print(hourly_temperatures)
    # logging.warning("Ended")
    # ==========================================
    pass
    #! SCRAPY
    # ==========================================

    # ==========================================

if __name__ == "__main__":
    main()