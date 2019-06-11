from selenium  import webdriver
from time import sleep
import xlrd

xlsfile=r"C:\Users\soul_k\Desktop\test.xlsx"
line=0
book=xlrd.open_workbook(xlsfile)
sheet0=book.sheet_by_index(0)
content=sheet0.row_values(line)
user,password=content
print(int(user),password)
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.vmall.com/member/enterprise?showListId=4&categoryId=9&p=1')
sleep(1)
# driver.find_element_by_name("user").clear()
driver.find_element_by_name("userAccount").send_keys(int(user))
sleep(1)
# driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("getAuthCodeBtn").click()
sleep(20)
while True:
    while True:
        try:
            driver.find_element_by_link_text(u"加入购物车").click()
            break
        except:
            sleep(2)
            if driver.find_elements_by_xpath("//li[@class='pgNext link next next-empty']")==[]:
                driver.find_element_by_xpath("//li[@class='pgNext link next']").click()
            else:
                driver.find_element_by_xpath("//li[@class='pgNext link first']").click()
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//a[@class='box-ok']").click()
        print("已加入购物车")
    except:
        driver.refresh()
    driver.find_element_by_link_text(u"优惠内购").click()
    driver.find_element_by_id("enterprise-nav-4").click()