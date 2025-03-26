import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# List of voting sites
VOTING_SITES = [
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

def vote():
    for site in VOTING_SITES:
        try:
            driver.get(site)
            time.sleep(3)  # Wait for page to load

            # Try different input fields
            possible_fields = ["username", "user", "player"]
            for field_name in possible_fields:
                try:
                    input_box = driver.find_element(By.NAME, field_name)
                    input_box.send_keys("PRS1357")
                    input_box.send_keys(Keys.RETURN)  # Submit
                    print(f"Voted successfully on {site}")
                    time.sleep(5)
                    break
                except:
                    continue
        except Exception as e:
            print(f"Error voting on {site}: {e}")

    driver.quit()

if __name__ == "__main__":
    while True:
        vote()
        print("Waiting 12 hours before next vote...")
        time.sleep(43200)  # 12 hours
