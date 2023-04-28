import time
import pymysql
from selenium.webdriver.remote.webdriver import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def save_doc_count_db(name, start_year):
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
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 禁用Selenium检测

    current_year = int(time.strftime('%Y', time.localtime()))

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.cnki.net/')
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="DBFieldBox"]/div[1]"""))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="DBFieldList"]/ul/li[15]/a"""))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="txt_SearchText"]'))
    ).send_keys(name)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """/html/body/div[2]/div[2]/div/div[1]/input[2]"""))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="divGroup"]/dl[3]/dt/b"""))
    ).click()
    time.sleep(3)
    list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="divGroup"]/dl[3]/dd/div/ul"""))
    )
    ul = list.find_elements(By.XPATH,"./li")
    data = {}
    for li in ul:
        year, count_str = li.text.split("(")
        year = int(year)
        count = int(count_str.replace(")", ""))
        data.update({year:count})
    driver.close()
    for y in range(start_year, current_year + 1):
        cursor.execute(
            f"UPDATE journal_citation SET doc_count={data.get(y, 0)} WHERE name='{name}' and year={y}"
        )
        conn.commit()
    cursor.execute(
        f"UPDATE journal SET document_count={data.get(y-5, 0)+data.get(y-1,0)+data.get(y-2,0)+data.get(y-3,0)+data.get(y-4,0)} WHERE journalname='{name}'"
    )
    conn.commit()
    cursor.close()
    conn.close()

