from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql
import re

def parse_journal_info(text):
    # 解析主办单位
    host_unit = re.findall(r'主办单位：\n(.+)', text)[0]

    # 解析主编
    editor = re.findall(r'主编：\n(.+)', text)[0]

    # 解析出版周期
    period = re.findall(r'出版周期：\n(.+)', text)[0]

    # 解析国际刊号
    intl_code = re.findall(r'国际刊号：\n(.+)', text)[0]

    # 解析国内刊号
    dom_code = re.findall(r'国内刊号：\n(.+)', text)[0]

    # 解析影响因子
    impact_factor = re.findall(r'影响因子：\n(.+)', text)[0]

    # 解析文献量
    document_count = re.findall(r'文献量：\n(.+)', text)[0]

    # 解析被引量
    cited_count = re.findall(r'被引量：\n(.+)', text)[0]

    # 解析下载量
    download_count = re.findall(r'下载量：\n(.+)', text)[0]

    # 解析基金论文量
    fund_count = re.findall(r'基金论文量：\n(.+)', text)[0]

    # 解析电话
    telephone = re.findall(r'电话：\n(.+)', text)[0]

    # 解析地址
    address = re.findall(r'地址：\n(.+)', text)[0]

    # 将解析结果以字典的形式返回
    return {
        '主办单位': host_unit,
        '主编': editor,
        '出版周期': period,
        '国际刊号': intl_code,
        '国内刊号': dom_code,
        '影响因子': impact_factor,
        '文献量': document_count,
        '被引量': cited_count,
        '下载量': download_count,
        '基金论文量': fund_count,
        '电话': telephone,
        '地址': address
    }


def crawl_journal_info(name):
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
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://w.wanfangdata.com.cn/')
    time.sleep(1)
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[1]/div/div[1]/div[2]/div/div[1]/span[1]"))
        ).click()
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="search-picker-popover"]/ul/li[2]/span"""))
        ).click()
    except TimeoutException:
        pass
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"""//*[@id="search-input"]"""))
    ).send_keys(f"刊名:{name}")
    time.sleep(2)
    searchbutton = driver.find_element(By.XPATH,"""//*[@id="search-btn-periodical"]""")
    searchbutton.click()
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"""/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/div/span[2]"""))
    ).click()

    while len(driver.window_handles) == 1:
        time.sleep(1)

    # 切换到新窗口
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)

    content = driver.find_element(By.XPATH,"""/html/body/div[4]/div/div[1]/div/div/wf-row/wf-row/wf-col-19/wf-field[2]""").text
    journal =  parse_journal_info(content)
    data = [
        (name,journal["主办单位"], journal["主编"],
         journal["出版周期"], journal["国际刊号"],journal["国内刊号"],
         journal["影响因子"], journal["文献量"],journal["被引量"],journal["下载量"],
         journal["基金论文量"], journal["电话"],journal["地址"]),
    ]
    cursor.executemany("""
                INSERT INTO Journal (journalname, host_unit, editor, period, intl_code, dom_code, 
                impact_factor, document_count, cited_count, download_count, fund_count, telephone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, data)
    conn.commit()
    print(journal)

    # 关闭新窗口并切回到原来的窗口
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    cursor.close()
    conn.close()

# namelist = ["中学数学月刊","数学通报","数学教育学报"]
# for name in namelist:
#     crawl_journal_info(name)