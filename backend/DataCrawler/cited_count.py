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

def five_cited_count(journal_name):
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
    driver.get('https://ref.cnki.net/REF/AdvSearch/Index')
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="refSrc"]"""))
    ).send_keys(journal_name)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"""//*[@id="publishleft"]"""))
    ).send_keys(str(current_year - 5))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="publishright"]'))
    ).send_keys(str(current_year))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="srcSpecial"]"""))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="srcSpecial"]/option[1]"""))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="advSearchBtn"]"""))
    ).click()
    time.sleep(3)
    list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="toolbarDiv"]/p"""))
    )

    pattern = r'文献总数(\d+)总被引(\d+)篇均被引([\d\.]+)'
    match = re.search(pattern, list.text)
    if match:
        doc_count = int(match.group(1))  # 文献总数
        cite_count = int(match.group(2))  # 总被引次数
        avg_cite_count = float(match.group(3))  # 平均被引次数

        # 将数据写入 MySQL 数据库
        try:
            sql = f"""
            UPDATE journal SET cited_count={cite_count} WHERE journalname='{journal_name}'
            """
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(str(e))

    driver.close()

    cursor.close()
    conn.close()
