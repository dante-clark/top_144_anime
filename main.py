from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

URL = "https://myanimelist.net/topanime.php"

limit = 0

link_num = 0

chrome_driver_path = r"C:\Users\Dante Clark\Desktop\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
time.sleep(2)

title_links = driver.find_elements(By.CLASS_NAME, "anime_ranking_h3")

while limit != 200: 
    for i in range(0, 51):
        time.sleep(5)
        title_links = driver.find_elements(By.CLASS_NAME, "anime_ranking_h3")
        try:
            title_links[i].click()
        except IndexError:
            limit += 50
            driver.get(f"{URL}?limit={limit}")
            continue
        with open(f"./pages/{link_num}.html", 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
            link_num += 1
        driver.back()
        time.sleep(1)

