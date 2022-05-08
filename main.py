import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL =("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2"
                        "C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east"
                        "%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%"
                        "7D%2C%22isMapVisible%22%3Atrue%2C%22filterSta"
                        "te%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fs"
                        "bo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22"
                        "value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3A"
                        "false%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22"
                        "mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%"
                        "22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")

user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
accept_language = "en-US,en;q=0.5"

response = requests.get(URL, headers={"Accept-Language": accept_language, "User-Agent": user_agent})
soup = BeautifulSoup(response.content, "html.parser")

# all_link_elements = soup.select(".list-card-top a")
# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https://www.zillow.com{href}")
#     else:
#         all_links.append(href)

prices = soup.find_all("div", class_="list-card-price")
all_prices = []
all_prices = [price.getText().lstrip() for price in prices]
print(all_prices)

addresses = soup.find_all(class_="list-card-addr")
addresses_list = [address.get_text().lstrip() for address in addresses]
print(addresses_list)

links = soup.find_all(class_="list-card-link", href=True)
links_list = [link["href"] for link in links]
print(links_list)
hrefs = soup.find_all("a", href=True)
hrefs_links = [href["href"] for href in hrefs]


ACCOUNT = "wilnirjr@gmail.com"
PASSWORD = "NOSSAdiarreia-138"
WEBSITE = "https://docs.google.com/"

service = Service("/usr/local/bin/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)
driver.maximize_window()

user_email = driver.find_element(By.ID, "identifierId")
user_email.send_keys(ACCOUNT)
time.sleep(2)
prox_button = driver.find_element(By.CLASS_NAME, "lw1w4b")
prox_button.click()

for address_input in addresses_list[0]:
    address_send = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i1']")
    address_send.send_keys(address_input)

for prices_input in all_prices[0]:
    prices_send = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i5']")
    prices_send.send_keys(prices_input)

for links_input in links_list[0]:
    links_send = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i9']")
    links_send.send_keys(links_input)

for n in range(len(all_prices)):
    button_send = driver.find_element(By.CLASS_NAME, "snByac")
    button_send.click()

    addresses_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i1']")
    addresses_input.send_keys(addresses_list[n])

    price_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i5']")
    price_input.send_keys(all_prices[n])

    links_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i9']")
    links_input.send_keys(links_list[n])

