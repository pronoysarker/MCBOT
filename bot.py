import time
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Locate Chromedriver
chrome_driver_path = shutil.which("chromedriver")

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Websites to vote on
vote_links = [
    "https://www.planetminecraft.com/server/bdzone-6288903/vote/",
    "https://minecraft-mp.com/server/332516/vote/",
    "https://mclist.io/server/64819/vote",
    "https://minecraftservers.page/servers/bdzone/vote",
    "https://minecraftlist.org/vote/31124",
    "https://minecraft-server.net/vote/bdzone/",
    "https://topg.org/minecraft-servers/server-664123",
    "https://topminecraftservers.org/vote/10965",
    "https://minecraft-serverlist.com/server/1231",
    "https://www.serverpact.com/vote-43745"
]

# Your Minecraft Username
MC_USERNAME = "PRS1357"

# Function to vote
def vote_on_site(url):
    try:
        print(f"Voting on {url}")
        driver.get(url)
        time.sleep(3)  # Wait for page to load

        # Find the username input field
        input_box = driver.find_element(By.XPATH, "//input[@type='text' or @name='username']")
        input_box.clear()
        input_box.send_keys(MC_USERNAME)

        # Submit form
        input_box.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for vote to register
        print(f"Voted successfully on {url}")
    except Exception as e:
        print(f"Failed to vote on {url}: {e}")

# Run voting process
for site in vote_links:
    vote_on_site(site)

# Close driver
driver.quit()
print("All votes completed!")
