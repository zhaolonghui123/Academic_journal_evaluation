import re
import time
import pymysql
from selenium.webdriver.remote.webdriver import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def save_data_to_db(name, start_year):
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
    for y in range(start_year, current_year + 1):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://ref.cnki.net/REF/AdvSearch/Index')
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="refSrc"]"""))
        ).send_keys(name)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"""//*[@id="publishleft"]"""))
        ).send_keys(str(y))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="publishright"]'))
        ).send_keys(str(y))
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
                sql = """
                INSERT INTO journal_citation(name, year, cite_count, avg_cite_count) VALUES (%s,%s,%s,%s)
                """
                values = (name, y, cite_count, avg_cite_count)
                cursor.execute(sql, values)
                conn.commit()
                print(f"期刊名称：{name}")
                print(f"年份：{y}")
                print(f"总被引次数：{cite_count}")
                print(f"平均被引次数：{avg_cite_count}")
            except Exception as e:
                print(str(e))

        driver.close()

    cursor.close()
    conn.close()
