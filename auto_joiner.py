import json
import random
import re
import time
import schedule
from threading import Timer

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser: webdriver.Chrome = "C:\Program Files\Google\Chrome\Application"
config = None
active_meeting = None
uuid_regex = r"\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b"
hangup_thread: Timer = None


def load_config():
    global config
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)


def wait_until_found(sel, timeout):
    try:
        element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, sel))
        WebDriverWait(browser, timeout).until(element_present)

        return browser.find_element_by_css_selector(sel)
    except exceptions.TimeoutException:
        print("Timeout waiting for element.")
        return None


def join_meeting():
    team_name = config['teamname']
    print(team_name)
    team_css_selector = "div[data-tid='team-{}-li']".format(team_name)
    teams_page = wait_until_found(team_css_selector, 60 * 5)
    if teams_page is not None:
        print('DEBUG: Clicked Team Name')
        teams_page.click()
    
    # click join button
    join_btn = wait_until_found(f"span[ng-if='!ctrl.roundButton']", 30)
    if join_btn is None:
        print('DEBUG: Join button not found')
        return

    join_btn.click()
    print('DEBUG: Join Button Clicked')

    # turn camera off
    video_btn = browser.find_element_by_css_selector("toggle-button[data-tid='toggle-video']>div>button")
    video_is_on = video_btn.get_attribute("aria-pressed")
    if video_is_on == "true":
        print('DEBUG: Video Turned Off')
        video_btn.click()

    # turn mic off
    audio_btn = browser.find_element_by_css_selector("toggle-button[data-tid='toggle-mute']>div>button")
    audio_is_on = audio_btn.get_attribute("aria-pressed")
    if audio_is_on == "true":
        print('DEBUG: Audio Turned Off')
        audio_btn.click()

    # final join button
    join_now_btn = wait_until_found("button[data-tid='prejoin-join-button']", 30)
    if join_now_btn is None:
        print('DEBUG: Join now button not found')
        return
    join_now_btn.click()

    print('Delay Started')
    time.sleep(config['auto_leave_after_min']*60)
    print('Delay Ended')

    # hangup button
    print('DEBUG: Exiting Meeting...')
    hangup_btn = browser.find_element_by_css_selector("button[id='hangup-button']")
    hangup_btn.click()
    print('DEBUG: Exited')
    exit()



def main():
    global browser, config

    load_config()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.maximize_window()

    browser.get("https://teams.microsoft.com")

    if config['email'] != "" and config['password'] != "":
        print('Email and Password found in config.json!')

        login_email = wait_until_found("input[type='email']", 30)
        if login_email is not None:
            login_email.send_keys(config['email'])
            time.sleep(1)

        # find the element again to avoid StaleElementReferenceException
        login_email = wait_until_found("input[type='email']", 5)
        if login_email is not None:
            login_email.send_keys(Keys.ENTER)

        login_pwd = wait_until_found("input[type='password']", 5)
        if login_pwd is not None:
            login_pwd.send_keys(config['password'])
            time.sleep(1)

        # find the element again to avoid StaleElementReferenceException
        login_pwd = wait_until_found("input[type='password']", 5)
        if login_pwd is not None:
            login_pwd.send_keys(Keys.ENTER)
        
        # stay signed in
        keep_logged_in = wait_until_found("input[id='idBtn_Back']", 5)
        if keep_logged_in is not None:
            keep_logged_in.click()
        
        # use web app instead
        use_web_instead = wait_until_found("a.use-app-lnk", 5)
        if use_web_instead is not None:
            use_web_instead.click()

        # make sure to have list mode configuration in ms teams
        jointime = config['meetingtime']
        print(jointime)
        schedule.every().day.at(jointime).do(join_meeting)

        while True:
            schedule.run_pending()
            time.sleep(10)

    
if __name__ == "__main__":
    main()
