from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

URL = "https://myanimelist.net/topanime.php"

# url parameter initially set equal to 0
# limit increments by 50 after every page.
limit = 0

# keeps track of the page number
link_num = 0

# there are 50 anime titles per page
num_of_anime = 50


# defining the chromedriver path
chrome_driver_path = r"C:\Users\Dante Clark\Desktop\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(URL)
time.sleep(2)

title_links = driver.find_elements(By.CLASS_NAME, "anime_ranking_h3")


# because we only want 144 anime titles
# we don't want the limit to surpass 100
while limit != 150: 
    # This for loop is used in conjunction with selenium to click on each
    # anime title, save the anime titles page, click the back button, and repeat
    # 144 times.
    for i in range(0, num_of_anime + 1):
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

