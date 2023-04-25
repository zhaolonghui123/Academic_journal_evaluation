import re
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql

def search_cnki_journal(journal_name, years):
    # 建立数据库连接
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='suda01160010@',
        db='fastapi',
    )

    # 获取游标对象
    cursor = conn.cursor()

    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled') # 禁用Selenium检测

    data = {}
    for y in years:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://ref.cnki.net/REF/AdvSearch/Index')
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="refSrc"]"""))
        ).send_keys(journal_name)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="refright"]"""))
        ).send_keys(y)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="refleft"]"""))
        ).send_keys(y)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="srcSpecial"]"""))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="srcSpecial"]/option[1]"""))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="advSearchBtn"]"""))
        ).click()
        time.sleep(3)
        list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="divGroup_Year"]/div/div[2]/ul"""))
        )
        li = list.find_elements(By.XPATH,"./li")
        for item in li:
            count_pattern = r'\((\d+)篇\)'  # 匹配文章数的正则表达式
            if(len(item.text)>0):
                count, year = item.text.split('\n')
                if int(year) not in data:
                    data[int(year)] = 0
                data[int(year)] += int(re.findall(count_pattern, item.text)[0])
        print(f"{y}:{data[int(y)]}")
        driver.close()

    cursor.close()
    conn.close()
    return data

journal_name = "中学数学月刊"
years = ["2018","2019","2020","2021","2022"]
data = search_cnki_journal(journal_name, years)