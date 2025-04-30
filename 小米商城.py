# from argparse import Action
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# 打开小米官网
driver.get("https://www.mi.com/")
time.sleep(2)
# 放大窗口
driver.maximize_window()
# 点击登录按钮
driver.find_element(By.XPATH,'//*[@id="header-wrapper"]/div/nav[2]/div/a[1]').click()
time.sleep(2)
# 点击账号密码登录
driver.find_element(By.XPATH,'//*[@id="rc-tabs-0-panel-login"]/form/div[1]/div[1]/div[2]/div/div/div/div/input').send_keys("小米账号登录")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="rc-tabs-0-panel-login"]/form/div[1]/div[2]/div/div[1]/div/input').send_keys("小米账号密码登录")
time.sleep(2)
# 点击同意
driver.find_element(By.XPATH,'//*[@id="rc-tabs-0-panel-login"]/form/div[1]/div[3]/label/span[1]/input').click()
time.sleep(2)
# 点击登录
driver.find_element(By.XPATH,'//*[@id="rc-tabs-0-panel-login"]/form/div[1]/button').click()
time.sleep(2)
# 点击小米商城
driver.find_element(By.XPATH,'//*[@id="header-wrapper"]/div/nav[1]/div[2]/a').click()
time.sleep(2)

arrs = driver.window_handles
for arr in arrs:
    driver.switch_to.window(arr)
    # print(driver.title)
    # if (driver.title =="小米商城 - Xiaomi 15、REDMI K80、MIX Fold 4，小米电视官方网站"):
    if (driver.current_url == "https://www.mi.com/shop"):
        break
# driver.find_element(By.XPATH,'//*[@id="search"]').send_keys("小米无线充电宝")
driver.find_element(By.ID,'search').send_keys("小米充电宝165w")

time.sleep(2)
# 定位搜索按钮并点击搜索
driver.find_element(By.XPATH,'//*[@id="J_submitBtn"]/input').click()
time.sleep(2)
# 定位到商品并点击
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/a').click()
time.sleep(2)
# 通过for循环找到对应的标签页
arrs = driver.window_handles
for arr in arrs:
    driver.switch_to.window(arr)
    # print(driver.title)
    if (driver.current_url =="https://www.mi.com/xiaomi-power-bank?product_id=1230802689&cfrom=search"):
        break
time.sleep(2)
# 定位到立即购买并点击
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div/div/div[2]/a[6]').click()
time.sleep(2)
# 通过for循环找到对应的标签页
arrs = driver.window_handles
for arr in arrs:
    driver.switch_to.window(arr)
    # print(driver.title)
    if (driver.current_url =="https://www.mi.com/shop/buy/detail?product_id=20379"):
        break
time.sleep(2)
# 点击加入购物车
driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div/div[2]/div[5]/div[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="J_miniCartBtn"]').click()
time.sleep(2)
arrs = driver.window_handles
for arr in arrs:
    driver.switch_to.window(arr)
    # print(driver.title)
    if  driver.current_url =="https://www.mi.com/shop/buy/cart":
        break
# 点击去结算
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div[1]/div[4]/span/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]').click()
time.sleep(3)
# 创建ActionChains对象
actions = ActionChains(driver)
# 向下滚动500像素（垂直方向）
actions.scroll_by_amount(0, 500).perform()
time.sleep(3)
# 立即下单
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div/div[6]/div[2]/div/a[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/img').click()
# time.sleep(1)
# arrs = driver.window_handles
# for arr in arrs:
#     driver.switch_to.window(arr)
#         print(driver.title)
#     if (driver.title =="支付宝 - 网上支付 安全快速！"):
#         break
time.sleep(10)







