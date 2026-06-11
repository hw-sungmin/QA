# region [모듈 임포트]
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
# endregion

# region [Chrome 드라이버 설정]
options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://crm.assistfit.co.kr/")
wait_count = 0
# endregion

# region [토스트 메시지 검증 함수]
def verify_toast_message(expected_message):
    try:
        # 토스트 자체 찾기
        toast = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "ol[data-sonner-toaster]")
            )
        )

        actual_message = toast.text.strip()

        print(f"토스트 노출 확인: {actual_message}")

        if expected_message in actual_message:
            print("✅ 토스트 메시지 일치")
        else:
            print("❌ 토스트 메시지 불일치")
            print(f"기대값: {expected_message}")
            print(f"실제값: {actual_message}")

    except TimeoutException:
        print("❌ 토스트 자체가 노출되지 않음")
# endregion

# region [로그인 동작]
id_input = "#mobileNumber"
password_input = "#password"
login_selector = "body > section.w-full.grid.grid-cols-12.justify-center.items-center.gap-5.max-w-\[1480px\].h-screen.m-auto > div.relative.flex.justify-center.h-full.md\:h-auto.col-start-1.col-end-13.md\:col-start-2.md\:col-end-12.lg\:col-start-3.lg\:col-end-11.xl\:col-start-4.xl\:col-end-10 > div > div > div > div > form > div.flex.flex-col.gap-4 > button"
# 아이디, 패스워드, 로그인 선택
def login(id, password):
    global wait_count
    try:
        wait_count += 3
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, id_input))
        )
        id_field = driver.find_element(By.CSS_SELECTOR, id_input)
        id_field.clear()
        id_field.send_keys("01043931593")
        print("아이디 입력 완료")   

        password_field = driver.find_element(By.CSS_SELECTOR, password_input)
        password_field.clear()
        password_field.send_keys("qwer1234")
        print("비밀번호 입력 완료")

        login_button = driver.find_element(By.CSS_SELECTOR, login_selector)
        login_button.click()
        print("로그인 완료")

    except Exception as e:
        print(f"!!!!! 로그인 과정에서 오류 발생: {e} !!!!!")
user_id = "your_user_id"
user_password = "your_password"
login(user_id, user_password)
time.sleep(1)
#endregion

# region [프랜차이즈 선택]
franchise_selector = "body > section.w-full.grid.grid-cols-12.justify-center.items-center.gap-5.max-w-\[1480px\].h-screen.m-auto > div.relative.flex.justify-center.h-full.md\:h-auto.col-start-1.col-end-13.md\:col-start-2.md\:col-end-12.lg\:col-start-3.lg\:col-end-11.xl\:col-start-4.xl\:col-end-10 > div > div > div > div.flex-1.flex.flex-col.gap-5.py-7\.5 > a:nth-child(1)"
# 프랜차이즈 선택
def select_first_franchise():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, franchise_selector))
        )
        franchise = driver.find_element(By.CSS_SELECTOR, franchise_selector)
        franchise.click()
        print("2번째 프랜차이즈 선택 완료")

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 프랜차이즈 선택 관련 오류 발생 !!!!!")
select_first_franchise()
time.sleep(1)
# endregion

# region [이벤트 팝업 닫기]
event_close_xpath = "//button[normalize-space()='닫기']"
# 이벤트 팝업 닫기
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
# endregion

# region [센터 변경]
center_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.shrink-0 > nav > button > div:nth-child(2) > p"
center_xpath = "//button[.//p[text()='APT 강북점']]"  #검증 시 변경 항목 (테스트 환경에 맞는 지점명)
#센터 변경
def select_center():
    global wait_count # 글로벌 변수 선언
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, center_selector))
        )
        center = driver.find_element(By.CSS_SELECTOR, center_selector)
        center.click()
        print("센터 변경 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, center_xpath))
        )
        center_select = driver.find_element(By.XPATH, center_xpath)
        center_select.click()
        print("센터 선택 완료")
        time.sleep(1)
    except (NoSuchElementException, TimeoutException):
        print("!!!!! 현재 센터 관련 오류 발생 !!!!!")
select_center()
time.sleep(1)
# endregion

# region [이벤트 팝업 닫기]
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
# endregion

# region [센터 정보 : 공지사항]
center_info_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.shrink-0 > nav > div.as-scroll-area.flex.flex-col.grow.shrink.basis-0.min-h-0 > div > div > ul > div > div:nth-child(2) > details:nth-child(1) > a:nth-child(2) > li"
center_kiosk_notice_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.flex-1.flex.flex-col > div > div.flex.justify-between.items-center.px-36.h-12\.25 > div.flex.gap-2 > button:nth-child(2)"
kiosk_notice_input = "#NoticeTitleInput"
kiosk_toast_message = "키오스크 공지사항을 저장했어요."
kiosk_notice_seve_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.flex-1.flex.flex-col > div > div.flex.flex-col.h-full > div > div > div > div > div.flex.justify-end.mt-2 > button"
app_notice_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.flex-1.flex.flex-col > div > div.flex.justify-between.items-center.px-36.h-12\.25 > div > button:nth-child(1)"
app_notice_create_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.flex-1.flex.flex-col > footer > a > button"
app_notice_create_title_input = "#NoticeTitleInput"
app_create_textarea_input = "#create-notice > div.mt-4 > div > textarea"
app_notice_save_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > footer > div > button.flex.justify-center.items-center.rounded-lg.duration-300.as-btn-primary-bg-default.as-btn-text-default.hover\:as-btn-primary-bg-hover.focus\:as-btn-primary-bg-focused.disabled\:as-btn-primary-bg-disabled.disabled\:cursor-not-allowed.font-bold.max-w-68\.25.h-13.w-62"
app_save_confirm_xpath = "//button[normalize-space()='등록']"
app_notice_toast_message = "게시물을 공지사항으로 등록했어요."
# 공지사항 탭 동작
def center_info_notice():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, center_info_selector)) #사이드 메뉴 - 센터 정보 탭 선택
        )
        center = driver.find_element(By.CSS_SELECTOR, center_info_selector)
        center.click()
        print("센터 정보 탭 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_kiosk_notice_selector)) #센터 정보 - 키오스크 공지 탭 선택
        )
        kiosk_notice = driver.find_element(By. CSS_SELECTOR, center_kiosk_notice_selector)
        kiosk_notice.click()
        print("키오스크 공지 탭 선택 완료")
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, kiosk_notice_input)) # 키오스크 공지 - 공지사항 입력
        )
        notice_field = driver.find_element(By.CSS_SELECTOR, kiosk_notice_input)
        notice_field.clear()
        notice_field.send_keys("키오스크 공지사항 테스트")
        print("키오스크 공지사항 입력 완료")
        time.sleep(1) 

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, kiosk_notice_seve_selector)) # 키오스크 공지 - 저장
        )
        kiosk_notice_save = driver.find_element(By.CSS_SELECTOR, kiosk_notice_seve_selector)
        kiosk_notice_save.click()
        print("키오스크 공지사항 저장 완료")
        verify_toast_message(kiosk_toast_message)
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, app_notice_selector)) #회원 앱 공지 선택
        )
        app_notice = driver.find_element(By. CSS_SELECTOR, app_notice_selector)
        app_notice.click()
        print("회원 앱 공지 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, app_notice_create_selector)) #게시물 작성 선택
        )
        app_notice_create = driver.find_element(By. CSS_SELECTOR, app_notice_create_selector)
        app_notice_create.click()
        print("회원 앱 공지 _ 게시물 작성 선택 완료")
        time.sleep(1)

        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, app_notice_create_title_input)) # 회원 앱 공지 - 게시물 - 제목 입력
        )
        title_field = driver.find_element(By.CSS_SELECTOR, app_notice_create_title_input) 
        title_field.clear()
        title_field.send_keys("센터 공지 작성")
        textarea_field = driver.find_element(By.CSS_SELECTOR, app_create_textarea_input)
        textarea_field.clear()
        textarea_field.send_keys("본문 내용 입력")
        print("회원 앱 공지사항 입력 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, app_notice_save_selector)) # 센터 공지 - 저장
        )
        app_notice_save = driver.find_element(By.CSS_SELECTOR, app_notice_save_selector)
        app_notice_save.click()
        print("센터 공지사항 저장 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_save_confirm_xpath)) # 센터 공지 - 확인 팝업 및 토스트 메시지 검증
        )
        app_save_confirm = driver.find_element(By.XPATH, app_save_confirm_xpath)
        app_save_confirm.click()
        print("센터 공지사항 저장 선택 완료")
        verify_toast_message(app_notice_toast_message)
        time.sleep(1)

        # #이전 화면 이동
        # driver.back()
        # print("이전 페이지 이동 완료")
        # time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 센터 정보 : 공지사항 오류 발생 !!!!!")

center_info_notice()
time.sleep(1)        
# endregion

# region [센터 정보 : 센터 정보]
center_information_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5.px-10 > ul > li:nth-child(2)"
center_info_update_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.flex-1.flex.flex-col > footer > a > button"
center_info_save_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > footer > button"
center_info_notice_selector = "body > div.relative.bg-\(--netural-gray-scale-white\).h-screen.flex > div.flex-1.overflow-hidden > div > main > div > div > div > div > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5.px-10 > ul > li:nth-child(1) > button"
#센터 정보 탭 동작
def center_information():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_information_selector)) #센터 정보 탭 선택
        )
        center_information_center = driver.find_element(By.CSS_SELECTOR, center_information_selector)
        center_information_center.click()
        print("센터 정보 탭 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_info_update_selector)) #내용 수정 버튼 선택
        )
        center_info_update_select = driver.find_element(By.CSS_SELECTOR, center_info_update_selector)
        center_info_update_select.click()
        print("내용 수정 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_info_save_selector))
        )
        center_info_save_select = driver.find_element(By.CSS_SELECTOR, center_info_save_selector)
        center_info_save_select.click()
        print("저장 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_info_notice_selector)) #센터 정보 : 공지사항 탭 선택
        )
        center_info_notice = driver.find_element(By. CSS_SELECTOR, center_info_notice_selector)
        center_info_notice.click()
        print("공지 사항 선택 완료")
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 센터 정보 관련 오류 발생 !!!!!")
center_information()
time.sleep(1)
# endregion





# region [자동화 종료 전 최종 검증 개수 및 카운트다운]
print(f"{wait_count}개 항목 검증 완료")
print("5초 후 종료됩니다.")

# 카운트다운 출력
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# 드라이버 종료
driver.quit()
# endregion