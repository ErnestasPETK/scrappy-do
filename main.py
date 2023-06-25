from confg import Settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

import time


def main():
    settings = Settings()
    driver = webdriver.Chrome()
    print("Starting")
    driver.get(settings.WEATHER_WEB_URL)
    driver.implicitly_wait(5)
    hourly_chart_selector = driver.find_element(by=By.XPATH, value='//ul[@class="tabs_nav"]/li/a[contains(text()," 48 hours ")]')
    if hourly_chart_selector.is_displayed():
        try: 
            hourly_chart_selector.click()
        except ElementClickInterceptedException:
            time.sleep(5)
            hourly_chart_selector.click()

    # driver.find_element(by=By.XPATH, value='//div[@class="left"]').click()
    charts = driver.find_elements(by=By.CLASS_NAME, value="chart-box")
    print("saving to screenshots")
    for index, chart in enumerate(charts):
        chart.screenshot(f"./screenshot{index}.png")
    print("Chart")
    print(charts)
    driver.quit()
    print("Ended")

if __name__ == "__main__":
    main()