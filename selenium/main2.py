from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from math import ceil


class responsiveTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls

    def screenshot(self, url):
        BROWSER_HEIGHT = 1056
        self.browser.get(url)
        url_title = self.browser.current_url.strip(
            'https://').strip("www.").split(".")[0]
        for size in sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(3)

            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            # return으로 자바에서 파이선으로 값받아옴
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            # total_sections은 숫자니까 range로 해야함 0, 1, 2, ...
            for section in range(total_sections + 1):
                self.browser.execute_script(
                    f"window.scrollTo(0,{(section)*BROWSER_HEIGHT})")
                self.browser.save_screenshot(
                    f"screenshots/{url_title}/{size}_{section+1}.png")
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://nomadcoders.co/")

browser.maximize_window()

sizes = [480, 960, 1366, 1920]

current_height = browser.get_window_size()
# print(current_height, type(current_height))
# {'width': ~~~, 'height':~~~~}
print(current_height)
print(browser.current_url)


# print(browser.current_url.split("//")[1].split(".")[0])
print(browser.current_url.strip('https://').strip("www.").split(".")[0])
BROWSER_HEIGHT = 1056

# for size in sizes:
#     browser.set_window_size(size, BROWSER_HEIGHT)
#     browser.execute_script("window.scrollTo(0,0)")
#     time.sleep(3)

#     scroll_size = browser.execute_script("return document.body.scrollHeight")
#     # return으로 자바에서 파이선으로 값받아옴
#     total_sections = ceil(scroll_size / BROWSER_HEIGHT)
#     # total_sections은 숫자니까 range로 해야함 0, 1, 2, ...
#     for section in range(total_sections + 1):
#         browser.execute_script(
#             f"window.scrollTo(0,{(section)*BROWSER_HEIGHT})")
#         browser.save_screenshot(f"screenshots/{size}_{section+1}.png")
#         time.sleep(2)
