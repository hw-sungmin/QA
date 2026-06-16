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
        print("프랜차이즈 선택 완료")

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
center_sele_xpath = "//p[normalize-space()='변경']"
center_xpath = "//button[.//p[text()='APT 강북점']]"  #검증 시 변경 항목 (테스트 환경에 맞는 지점명)
#센터 변경
def select_center():
    global wait_count # 글로벌 변수 선언
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, center_sele_xpath))
        )
        center = driver.find_element(By.XPATH, center_sele_xpath)
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
center_info_xpath = "//p[normalize-space()='센터 정보']"
center_kiosk_notice_xpath = "//p[normalize-space()='키오스크 공지']"
kiosk_notice_input = "#NoticeTitleInput"
kiosk_notice_seve_xpath = "//button[normalize-space()='저장']"
kiosk_toast_message = "키오스크 공지사항을 저장했어요."
app_notice_xpath = "//p[normalize-space()='회원 앱 공지']"
app_notice_create_xpath = "//button[normalize-space()='게시물 작성']"
app_notice_create_title_input = "#NoticeTitleInput"
app_create_textarea_input = "#create-notice > div.mt-4 > div > textarea"
app_notice_save_xpath = "//button[normalize-space()='게시물 등록']"
app_save_confirm_xpath = "//button[normalize-space()='등록']"
app_notice_toast_message = "게시물을 공지사항으로 등록했어요."
app_notice_target_title_xpath = "//td[normalize-space()='검증 후 삭제']"
app_notice_delete_xpath = "//p[normalize-space()='삭제']"
app_notice_del_confirm_xpath = "//button[normalize-space()='게시물 삭제']"
app__del_toast_message = "게시물을 삭제했어요."
# 공지사항 탭 동작
def center_info_notice():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, center_info_xpath)) #사이드 메뉴 - 센터 정보 탭 선택
        )
        center = driver.find_element(By.XPATH, center_info_xpath)
        center.click()
        print("센터 정보 탭 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, center_kiosk_notice_xpath)) #센터 정보 - 키오스크 공지 탭 선택
        )
        kiosk_notice = driver.find_element(By.XPATH, center_kiosk_notice_xpath)
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
            EC.presence_of_element_located((By.XPATH, kiosk_notice_seve_xpath)) # 키오스크 공지 - 저장
        )
        kiosk_notice_save = driver.find_element(By.XPATH, kiosk_notice_seve_xpath)
        kiosk_notice_save.click()
        print("키오스크 공지사항 저장 완료")
        verify_toast_message(kiosk_toast_message)
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, app_notice_xpath)) #회원 앱 공지 선택
        )
        app_notice = driver.find_element(By.XPATH, app_notice_xpath)
        app_notice.click()
        print("회원 앱 공지 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, app_notice_create_xpath)) #게시물 작성 선택
        )
        app_notice_create = driver.find_element(By.XPATH, app_notice_create_xpath)
        app_notice_create.click()
        print("회원 앱 공지 _ 게시물 작성 선택 완료")
        time.sleep(1)

        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, app_notice_create_title_input)) # 회원 앱 공지 - 게시물 - 제목 입력
        )
        title_field = driver.find_element(By.CSS_SELECTOR, app_notice_create_title_input) 
        title_field.clear()
        title_field.send_keys("검증 후 삭제")
        textarea_field = driver.find_element(By.CSS_SELECTOR, app_create_textarea_input)
        textarea_field.clear()
        textarea_field.send_keys("본문 내용 입력")
        print("회원 앱 공지사항 입력 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_notice_save_xpath)) # 센터 공지 - 저장
        )
        app_notice_save = driver.find_element(By.XPATH, app_notice_save_xpath)
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

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_notice_target_title_xpath)) # 등록한 게시물 노출 여부 확인
        )
        target_notice = driver.find_element(By.XPATH, app_notice_target_title_xpath)
        if target_notice:
            print("✅ 등록한 공지사항 게시물 노출 확인")
        else:
            print("❌ 등록한 공지사항 게시물 노출 실패")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_notice_target_title_xpath)) # 등록한 게시물 선택
        )
        target_notice_select = driver.find_element(By.XPATH, app_notice_target_title_xpath)
        target_notice_select.click()
        print("등록한 공지사항 게시물 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_notice_delete_xpath)) # 등록한 게시물 삭제 선택
        )
        app_notice_delete = driver.find_element(By.XPATH, app_notice_delete_xpath)
        app_notice_delete.click()
        print("등록한 공지사항 게시물 삭제 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_notice_del_confirm_xpath)) # 삭제 확인 팝업 - 토스트 메시지 검증
        )
        del_confirm = driver.find_element(By.XPATH, app_notice_del_confirm_xpath)
        del_confirm.click()
        print("게시물 삭제 확인 선택 완료")
        verify_toast_message(app__del_toast_message)
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
center_info_update_xpath = "//button[normalize-space()='내용 수정']"
center_info_save_xpath = "//button[normalize-space()='저장']"
center_info_notice_xpath = "//p[normalize-space()='공지사항']"
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
            EC.presence_of_element_located((By.XPATH, center_info_update_xpath)) #내용 수정 버튼 선택
        )
        center_info_update_select = driver.find_element(By.XPATH, center_info_update_xpath)
        center_info_update_select.click()
        print("내용 수정 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, center_info_save_xpath))
        )
        center_info_save_select = driver.find_element(By.XPATH, center_info_save_xpath)
        center_info_save_select.click()
        print("저장 선택 완료")
        time.sleep(1)

        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, center_info_notice_xpath)) #센터 정보 : 공지사항 탭 선택
        )
        center_info_notice = driver.find_element(By.XPATH, center_info_notice_xpath)
        center_info_notice.click()
        print("공지 사항 선택 완료")
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 센터 정보 관련 오류 발생 !!!!!")
center_information()
time.sleep(1)
# endregion

# region [센터 정보 : 회원]
member_xpath = "//p[normalize-space()='회원']"
member_information_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(1) > button"
member_info_check_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex-1.flex.flex-col.gap-4.px-10.pb-10 > table > tbody > tr:nth-child(1)"
member_revise_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex.flex-col.px-10 > div > div.flex.col-span-2.gap-5.pt-6 > div.flex.flex-col.gap-4 > a > button"
member_revise_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
member_create_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > a > button"
member_create_select_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].rounded-md.bg-black\/60.backdrop-blur-sm > div > div > div > div.flex-auto.items-center > div > div:nth-child(1) > a"
member_datail_name_selector = "#username"
member_datail_mobile_selector = "#mobileNumber"
member_dropdown_selector = 'button.inline-flex.justify-between.w-full.bg-transparent'
member_dropdown_option_xpath = "//button[text()='워크인']"
item_add_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > div > a > button"
item_add_save_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].bg-black\/60.backdrop-blur-sm > div > div > div > div > main > div > button"
item_tab_GX_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(2) > button > p"
item_tab_PT_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(3) > button > p"
item_tab_locker_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(4) > button > p"
item_tab_equipment_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(5) > button > p"
member_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
member_secession_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(2) > button"
member_refund_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(3) > button"
member_refund_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(2) > button"
member_group_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(4) > button"
member_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(5) > button"
pause_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(6) > button"
item_add_confirm_selector = "#member-payment > div.flex.justify-center.items-center.fixed.inset-0.z-50.bg-black\/10.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300 > div > div > div > div > div.h-\[3\.125rem\].flex.items-center.self-stretch > button:nth-child(3)"


def member_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #회원 관리 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, member_xpath))
        )
        member = driver.find_element(By.XPATH, member_xpath)
        member.click()
        print("회원 관리 선택 완료")

        #회원 관리 선택 후 딜레이 2초
        time.sleep(1)
        
        #회원 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_create_selector))
        )
        member_create = driver.find_element(By.CSS_SELECTOR, member_create_selector)
        member_create.click()
        print("회원 관리_회원 등록 선택 완료")

        #회원 등록 선택 후 딜레이 2초
        time.sleep(1)

        #상세 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_create_select_selector))
        )
        member_datail = driver.find_element(By.CSS_SELECTOR, member_create_select_selector)
        member_datail.click()
        print("회원 관리_회원 등록_상세 등록 선택 완료")
        
        #상세 등록 선택 후 딜레이 2초
        time.sleep(1)

        # 이름 입력 호출 대기 및 값 입력
        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, member_datail_name_selector))
        )
        name_field = driver.find_element(By.CSS_SELECTOR, member_datail_name_selector)
        name_field.clear()
        name_field.send_keys("자동화검증회원") 
        print("이름 입력 완료")

        # 비밀번호 입력 호출 대기 및 값 입력
        mobile_No_field = driver.find_element(By.CSS_SELECTOR, member_datail_mobile_selector)
        mobile_No_field.clear()
        random_phone = generate_random_member_number()
        mobile_No_field.send_keys(random_phone)
        print("휴대전화번호 입력 완료")

        # 아이디, 비밀번호 입력 후 2초 딜레이
        time.sleep(1)

        #방문 경로 드롭다운 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_dropdown_selector))
        )
        member_dropdown = driver.find_element(By.CSS_SELECTOR, member_dropdown_selector)
        member_dropdown.click()
        print("방문 경로 드롭다운 선택 완료")

        #회원 관리 선택 후 딜레이 2초
        time.sleep(1)

        #방문 경로 드롭다운_특정값 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, member_dropdown_option_xpath))
        )
        member_dropdown_option = driver.find_element(By.XPATH, member_dropdown_option_xpath)
        member_dropdown_option.click()
        print("드롭다운 워크인 선택 완료")

        #방문 경로 선택 후 딜레이 2초
        time.sleep(1)

        #회원권 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #회원권 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #회원권 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

  
#그룹 수업 탭 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_GX_selector))
        )
        item_tab_GX = driver.find_element(By.CSS_SELECTOR, item_tab_GX_selector)
        item_tab_GX.click()
        print("그룹 수업 탭 선택 완료")

        # 그룹 수업 탭 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #그룹 수업 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")


        #개인 레슨 탭 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_PT_selector))
        )
        item_tab_PT = driver.find_element(By.CSS_SELECTOR, item_tab_PT_selector)
        item_tab_PT.click()
        print("개인 레슨 탭 선택 완료")

        # 개인레슨 탭 선택 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #개인 레슨 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")

        #락커 상품 탭 선택 호출 대기
        wait_count += 1 
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_locker_selector))
        )
        item_tab_locker = driver.find_element(By.CSS_SELECTOR, item_tab_locker_selector)
        item_tab_locker.click()
        print("락커 상품 탭 선택 완료")

        #락커 상품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #락커 상품 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #락커 상품 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #락커 상품 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

        #운동 용품 탭 선택 호출 대기 
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_equipment_selector))
        )
        item_tab_equipment = driver.find_element(By.CSS_SELECTOR, item_tab_equipment_selector)
        item_tab_equipment.click()
        print("운동 용품 탭 선택 완료")

        #운동 용품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #운동 용품 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #운동 용품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #운동 용품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

        #회원 등록 버튼 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_save_selector))
        )
        member_save = driver.find_element(By.CSS_SELECTOR, member_save_selector)
        member_save.click()
        print("회원 등록 완료")

        #회원 등록 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #탈퇴 처리 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_secession_selector))
        )
        member_secession = driver.find_element(By.CSS_SELECTOR, member_secession_selector)
        member_secession.click()
        print("회원 삭제 탭 선택 완료")

        #탈퇴 처리 탭 선택 후 딜레이 2초
        time.sleep(1)

        #환불 처리 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_refund_selector))
        )
        member_refund = driver.find_element(By.CSS_SELECTOR, member_refund_selector)
        member_refund.click()
        print("환불 처리 탭 선택 완료")

        #환불 처리 탭 선택 후 딜레이 2초
        time.sleep(1)

        #환불 처리_환불 내역 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_refund_history_selector))
        )
        member_refund_history = driver.find_element(By.CSS_SELECTOR, member_refund_history_selector)
        member_refund_history.click()
        print("환불 처리_환불 내역 탭 선택 완료")

        #환불 처리_환불 내역 탭 선택 후 딜레이 2초
        time.sleep(1)

        #단체 연장 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_group_selector))
        )
        member_group = driver.find_element(By.CSS_SELECTOR, member_group_selector)
        member_group.click()
        print("단체 연장 탭 선택 완료")

        #단체 연장 탭 선택 후 딜레이 2초
        time.sleep(1)

        #정지 기록 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_history_selector))
        )
        member_history = driver.find_element(By.CSS_SELECTOR, member_history_selector)
        member_history.click()
        print("정지 기록 탭 선택 완료")

        #정지 기록 탭 선택 후 딜레이 2초
        time.sleep(1)

        #수정 기록 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, pause_history_selector))
        )
        pause_history = driver.find_element(By.CSS_SELECTOR, pause_history_selector)
        pause_history.click()
        print("수정 기록 탭 선택 완료")

        #정지 기록 탭 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_information_selector))
        )
        member_information = driver.find_element(By. CSS_SELECTOR, member_information_selector)
        member_information.click()
        print("회원 정보 탭 선택 완료")

        #회원 정보 탭 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보_정보 조회 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_info_check_selector))
        )
        member_info_check = driver.find_element(By. CSS_SELECTOR, member_info_check_selector)
        member_info_check.click()
        print("회원 정보_정보 조회 선택 완료")

        #회원 정보_정보 조회 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 수정 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_revise_selector))
        )
        member_revise = driver.find_element(By. CSS_SELECTOR, member_revise_selector)
        member_revise.click()
        print("회원 수정 선택 완료")

        #회원 정보 수정 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 수정 저장 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_revise_save_selector))
        )
        member_revise_save = driver.find_element(By. CSS_SELECTOR, member_revise_save_selector)
        member_revise_save.click()
        print("회원 정보 수정 저장 완료")

        #회원 정보 수정 저장 후 딜레이 2초
        time.sleep(1)


    except (NoSuchElementException, TimeoutException):
        print("!!!!! 회원 관리 관련 오류 발생 !!!!!")

member_admin()
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