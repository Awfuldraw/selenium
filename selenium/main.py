from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# .\main.py


class googleKeywordScreenshot():

    def __init__(self, keyword, screenshot_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            shitty_element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
            )
            self.browser.execute_script(
                """
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty);
                """,
                shitty_element,
            )
        except Exception:
            pass
        search_results = self.browser.find_elements_by_class_name("g")
        for index, result in enumerate(search_results):
            result.screenshot(
                f"{self.screenshot_dir}/{self.keyword}_{index}.png")

    def finish(self):
        self.browser.quit()


domain_competitors = googleKeywordScreenshot("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()

KEYWORD = "buy domain"


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

shitty_element = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
)


browser.execute_script(
    """
    const shitty = arguments[0];
    shitty.parentElement.removeChild(shitty);
    """,
    shitty_element,
)


# browser.find_elements_by_class_name("g kno-kp mnr-c g-blk")


search_results = browser.find_elements_by_class_name("g")
for index, result in enumerate(search_results):
    # class_name = result.get_attribute("class")
    # g , g, g, g, g kno-kp ~~m, g, g
    # class_name=result.get_attribute("class")
    # if "kno-kp mnr-c g-blk" not in class_name:
    result.screenshot(f"screenshots/{KEYWORD}_{index}.png")

# browser.quit()

# 1.6
