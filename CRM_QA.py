from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# driver setup
options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window() #브라우저 최대화 설정
driver.get("https://crm.assistfit.co.kr/") #crm 메인 페이지 진입
wait_count = 0

# id / password / Login button css selector
id_selector = "#mobileNumber"
password_selector = "#password"
login_button_selector = "body > section.w-full.grid.grid-cols-12.justify-center.items-center.gap-5.max-w-\[1480px\].h-screen.m-auto > div.relative.flex.justify-center.h-full.md\:h-auto.col-start-1.col-end-13.md\:col-start-2.md\:col-end-12.lg\:col-start-3.lg\:col-end-11.xl\:col-start-4.xl\:col-end-10 > div > div > div > div > form > div.flex.flex-col.gap-4 > button"

# login function
def login(id, password):
    global wait_count
    try:
        wait_count += 3
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, id_selector))
        )
        id_field = driver.find_element(By.CSS_SELECTOR, id_selector)
        id_field.clear()
        id_field.send_keys("01043931593")

        password_field = driver.find_element(By.CSS_SELECTOR, password_selector)
        password_field.clear()
        password_field.send_keys("qwer1234")

        login_button = driver.find_element(By.CSS_SELECTOR, login_button_selector)
        login_button.click()

        print("로그인 완료")

    except Exception as e:
        print(f"!!!!! 로그인 과정에서 오류 발생: {e} !!!!!")

user_id = "your_user_id"
user_password = "your_password"
login(user_id, user_password)
time.sleep(1)

# pranchise selection css selector
franchise_selector = "body > section.w-full.grid.grid-cols-12.justify-center.items-center.gap-5.max-w-\[1480px\].h-screen.m-auto > div.relative.flex.justify-center.h-full.md\:h-auto.col-start-1.col-end-13.md\:col-start-2.md\:col-end-12.lg\:col-start-3.lg\:col-end-11.xl\:col-start-4.xl\:col-end-10 > div > div > div > div.flex-1.flex.flex-col.gap-5.py-7\.5 > a:nth-child(1)"

def select_first_franchise():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, franchise_selector))
        )
        franchise = driver.find_element(By.CSS_SELECTOR, franchise_selector)
        franchise.click()

        print("첫번째 프랜차이즈 선택 완료")

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 프랜차이즈 선택 관련 오류 발생 !!!!!")

select_first_franchise()
time.sleep(1)

#event pop-up close
event_close_xpath = "//button[normalize-space()='닫기']"

def event_close():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By. XPATH, event_close_xpath))
        )
        event = driver.find_element(By. XPATH, event_close_xpath)
        event.click()
        print("이벤트 팝업 닫기 완료")
    
    except TimeoutException:
        print("⏩ 이벤트 팝업 없음 (정상) → 계속 진행")

    except (NoSuchElementException, Exception) as e:
        print(f"⚠️ 이벤트 팝업 처리 중 오류 발생: {e}")

event_close()
time.sleep(1)






















# 작업 끝난 후 호출 횟수 출력
print(f"{wait_count}개 항목 검증 완료")
print("5초 후 종료됩니다.")

# 카운트다운 출력
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# 드라이버 종료
driver.quit()