from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql

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


name = "中学数学月刊"
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled') # 禁用Selenium检测
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://w.wanfangdata.com.cn/')
time.sleep(1)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[1]/div/div[1]/div[2]/div/div[1]/span[1]"))
).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="search-picker-popover"]/ul/li[2]/span"""))
).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="search-input"]"""))
).send_keys(f"刊名:{name}")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="search-btn-document"]/span"""))
).click()
while True:
    for i in range(1,21):
        item = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,f"""/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[{str(i)}]"""))
        )

        papername = item.find_element(By.XPATH,"./div[1]").text
        last_dot_index = papername.find('.')
        if last_dot_index != -1:
            papername = papername[last_dot_index + 1:]


        authorlist = item.find_elements(By.XPATH, "./div[2]/span")
        list = []
        for author in authorlist:
            if len(author.text) > 0 and (author.text[0] not in ["[", "-", "《", "2"]):
                list.append(author.text)
            if len(author.text) > 0 and author.text[0] == "2":
                publish = author.text
        if list == []:
            authorlist = "no author"
        else:
            authorlist = ",".join(list)

        try:
            webdownload = item.find_element(By.XPATH,"./div[5]")
        except NoSuchElementException:
            webdownload = item.find_element(By.XPATH,"./div[4]")

        # if webdownload.text and "被引：" in webdownload.text:
        #     beiyin_index = webdownload.text.index("被引：") + 3  # 获取“被引：”字符串的结束下标
        #     xiazaishu_index = webdownload.text.index("下载：")  # 获取“下载：”字符串的开始下标
        #     cited = webdownload[beiyin_index:xiazaishu_index].strip()
        # else:
        #     cited = "0"
        last_dot_index = webdownload.text.find('下载：')
        if last_dot_index != -1:
            webdownload = webdownload.text[last_dot_index + 3:]
        if not isinstance(webdownload, str):
            webdownload = "0"
        #print(papername, authorlist, publish, name, webdownload)
        data = [
            (papername, authorlist, publish, name, int(webdownload)),
        ]
        cursor.executemany("""
            INSERT INTO Journal_information (papername, author, publish, journalname, webdownload) VALUES (%s, %s, %s, %s, %s)
        """, data)
        conn.commit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, """/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[5]/div[4]/span[3]"""))
    ).click()
    print("\n")
    time.sleep(5)
cursor.close()
conn.close()
# import React, { useState, useEffect } from 'react';
# import { Table } from 'antd';
#
# function UserTable() {
#   const [users, setUsers] = useState([]);
#   const [total, setTotal] = useState(0);
#   const [pageSize, setPageSize] = useState(10);
#   const [currentPage, setCurrentPage] = useState(1);
#
#   useEffect(() => {
#     async function loadData() {
#       const queryParams = new URLSearchParams({
#         page: currentPage,
#         page_size: pageSize,
#       });
#       const response = await fetch(`/users?${queryParams}`);
#       const { data, has_more } = await response.json();
#       setUsers(data);
#       setTotal(currentPage * pageSize);
#       if (has_more) {
#         setTotal((currentPage + 1) * pageSize);
#       }
#     }
#     loadData();
#   }, [currentPage, pageSize]);
#
#   function handlePageChange(page, pageSize) {
#     setCurrentPage(page);
#     setPageSize(pageSize);
#   }
#
#   const columns = [
#     {
#       title: 'ID',
#       dataIndex: 'id',
#       key: 'id',
#     },
#     {
#       title: 'Name',
#       dataIndex: 'name',
#       key: 'name',
#     },
#     {
#       title: 'Age',
#       dataIndex: 'age',
#       key: 'age',
#     },
#   ];
#
#   return (
#     <Table
#       dataSource={users}
#       columns={columns}
#       pagination={{
#         current: currentPage,
#         pageSize: pageSize,
#         total: total,
#         showSizeChanger: true,
#         showQuickJumper: true,
#         onChange: handlePageChange,
#       }}
#     />
#   );
# }
#
# export default UserTable;