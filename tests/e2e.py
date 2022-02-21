from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

SRV = Service("C:\DRIVERS\Chrome\chromedriver.exe")
test_driver = webdriver.Chrome(service=SRV)


def test_scores_service(Leaderboard_url):
    test_driver.get(Leaderboard_url)
    try:
        score = test_driver.find_element(By.XPATH, '//*[@id="wrapvalue"]').text
        if int(score) in range(1, 1001):
            return True
        return False
    except:
        return False
    finally:
        test_driver.close()


def main_function():
    if test_scores_service("http://127.0.0.1:30000"):
        return 0
    return exit(-1)
