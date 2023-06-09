#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pathlib import Path
import sys

# Argment
search_word = sys.argv[1]       # machine name


# Setting of DL
dldir_name = 'Downloads/'+search_word
dldir_path = Path(dldir_name)
dldir_path.mkdir(exist_ok=True)  # 存在していてもOKとする（エラーで止めない）
download_dir = str(dldir_path.resolve())  # 絶対パス
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "plugins.always_open_pdf_externally": True
})


# Scraping
browser =   webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = 'https://www.mitsubishielectric.co.jp/ldg/wink/ssl/top.do'                # Link of 三菱WINK
browser.get(url)

login_btn = browser.find_element(By.ID, "form_02")
login_btn.click()

input_form = browser.find_element(By.ID, "form_tub_01")                         # Loginボタン
search_tub = browser.find_element(By.ID, "form_tub_01_b")                       # 検索フォーム
input_form.send_keys(search_word)
search_tub.click()


texts = browser.find_elements(By.NAME, "productNameLink")
for i in texts:
    if i.text == search_word.upper():
        print(i.text)
        i.click()
        exit


### Download Files
# 納入仕様書
a_ref = browser.find_element(By.XPATH, "//li[@class='js_last']/div[1]/a[@datakbn='R']").get_attribute('href')
browser.get(a_ref)

# CAD
cad_data = browser.find_element(By.XPATH, "//p[@class='nav_more rs']/a[@class='bullet_link']")
ActionChains(browser).move_to_element(cad_data).perform()
cad_data.click()



