import select
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning

import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def scrape_sitemap(sitemap_url):
    """
    Fetches an XML sitemap and extracts all URLs.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(sitemap_url, headers=headers)
    response.raise_for_status() # Raise an exception for bad status codes

    # Use 'lxml' as the parser for XML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <loc> tags which contain the URLs
    urls = [loc.text for loc in soup.find_all('loc')]

    return urls
def scrapesite(driver_yay):
    time.sleep(2)
    print("scraping page: ")
    soup_text_yay = driver_yay.find_elements(By.CLASS_NAME, 'ant-table-cell')
    return soup_text_yay


def clicknextbutton():
    try:
        next_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ant-pagination-next"))
        )
        # If the wait succeeds, click the button to go to the next page
        next_button.click()
        print(f"Clicked 'Next' button")
        # Add a small sleep to ensure the next page starts loading
        time.sleep(1)
    except Exception as ex:
        # Handle other potential exceptions (e.g., StaleElementReferenceException)
        print(f"An error occurred: {ex}")

    except TimeoutException:
        # This exception is raised when the 'Next' button is not found within 10 seconds
        print("Timeout reached. 'Next' button not found. Assuming last page reached.")


def chunk_list(input_list, chunk_size):
    """
    Divides a list into smaller lists (chunks) of a specified length.
    """
    return [input_list[ie:ie + chunk_size] for ie in range(0, len(input_list), chunk_size)]

# Example usage
sitemap_url = 'https://rotrends.com/games/sitemap.xml' # Replace with the target sitemap URL
try:
    page_urls = scrape_sitemap(sitemap_url)
    print(f"Found {len(page_urls)} URLs in the sitemap.")
    for url in page_urls[:10]: # Print the first 10 for brevity
        print(url)
except requests.exceptions.RequestException as e:
    print(f"Error fetching sitemap: {e}")

# run Chrome in headless mode
options = Options()
options.page_load_strategy = 'none'
# define a custom User Agent
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

# add the User Agent to Chrome options
options.add_argument(f"user-agent={custom_user_agent}")

# set the options to use Chrome in headless mode
#options.add_argument("--headless=new")

# Set up the WebDriver (you'll need the correct driver for your browser)
# Here we use Chrome as an example
driver = webdriver.Chrome(options=options)
driver.set_window_size(1024, 768) # Width, Height in pixels

url = page_urls[0] + "?page=1&page_size=100&sort=-playing"  # Replace with your target URL
driver.get(url)
# Get the page source after JavaScript has executed
#select = Select(driver.find_element('class', 'ant-table-cell'))
time.sleep(5)
xpath_menu = {"/html/body/div[3]/div/ul/li[1]","/html/body/div[3]/div/ul/li[3]", "/html/body/div[3]/div/ul/li[4]","/html/body/div[3]/div/ul/li[6]" "/html/body/div[3]/div/ul/li[7]","/html/body/div[3]/div/ul/li[8]","/html/body/div[3]/div/ul/li[9]","/html/body/div[3]/div/ul/li[10]",
              "/html/body/div[3]/div/ul/li[11]","/html/body/div[3]/div/ul/li[12]"
, "/html/body/div[3]/div/ul/li[13]"
, "/html/body/div[3]/div/ul/li[16]"
, "/html/body/div[3]/div/ul/li[17]"
, "/html/body/div[3]/div/ul/li[11]"
, "/html/body/div[3]/div/ul/li[19]"
, "/html/body/div[3]/div/ul/li[20]"
, "/html/body/div[3]/div/ul/li[29]"
, "/html/body/div[3]/div/ul/li[34]"}
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/main/div[1]/div/div[1]/div[1]/div[1]/div/button"))).click()
#title_menu = ["Global Rank", "Global Rank Shift (1d)"]
i = 0
for path in xpath_menu:
#for text in title_menu:
    #text_tag = "li[textContent='" + text + "']"
    time.sleep(1)
    try:
        # Replace with your actual target element locator inside the dropdown
        target_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        #driver.execute_script(
         #   'arguments[0].scrollTop = arguments[0].scrollTop + document.getElementById("search-results-container").scrollHeight;',
         #   inner_window,
      # )

        target_element.click()
        print("\n")
        i = i + 1
        print(i)


    except Exception as e:
        print(f"An error occurred: {e}")
        print(i)


data_list = []

page_total = list(range(1,200))
for pages in page_total:
    is_loading = True
    while is_loading:
        soup_text = scrapesite(driver)
        try:
            path = "/html/body/div[2]/div[2]/main/div[1]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[11]"
            # Replace with your actual target element locator inside the dropdown
            target_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, path)))
            is_loading = False
        except Exception as e:
            print(f"An error occurred: {e}")
            driver.execute_script("location.reload()")
            is_loading = True
            print("data gone now reload")
            time.sleep(5)

    try:
        for text in soup_text:
            data = (text.get_attribute('textContent'))
            data_list.append(data)
        clicknextbutton()
    except Exception as e:
        print(f"An error occurred: {e}")
        break

    print(len(data_list) / (i + 1))

chunks = chunk_list(data_list, i+1)
print(chunks[0])
print(len(chunks))


driver.quit()
filename = 'my_data.csv'


with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write each row from your data list to the CSV file
    for row in chunks:
        csv_writer.writerow(row)

print(f"Data successfully written to {filename} with UTF-8 encoding.")