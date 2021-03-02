from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from math import ceil

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://nomadcoders.co/")

browser.maximize_window()

sizes = [480, 960, 1366, 1920]

current_height = browser.get_window_size()
# print(current_height, type(current_height))
# {'width': ~~~, 'height':~~~~}
print(current_height)

BROWSER_HEIGHT = 1056

for size in sizes:
    browser.set_window_size(size, BROWSER_HEIGHT)
    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(3)

    scroll_size = browser.execute_script("return document.body.scrollHeight")
    # return으로 자바에서 파이선으로 값받아옴
    total_sections = ceil(scroll_size / BROWSER_HEIGHT)
    # total_sections은 숫자니까 range로 해야함 0, 1, 2, ...
    for section in range(total_sections + 1):
        browser.execute_script(
            f"window.scrollTo(0,{(section)*BROWSER_HEIGHT})")
        browser.save_screenshot(f"screenshots/{size}_{section+1}.png")
        time.sleep(2)
