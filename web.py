from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime,time
import py.autopoke.TargetList as TargetList,user_data as user_data
import json,os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #改工作路徑
def get_save_cookies():#存cookie
    webcookie=driver.get_cookies()
    with open('facebookcookie.json',"w+") as cookie:
        cookie.write(json.dumps(webcookie))
        cookie.close()
def use_cookie():#用cookie
    with open("facebookcookie.json",'r') as list:
        data = json.loads(list.read())
    for cookie in data:
        driver.add_cookie(cookie)
    driver.refresh()
def FacebookLogin():
    global driver
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    try:
        use_cookie()
    except:
        time.sleep(5)
        driver.find_element(By.ID,'email').send_keys(user_data.user_email)
        driver.find_element(By.ID,'pass').send_keys(user_data.password)
        driver.find_element(By.NAME,'login').click()
    get_save_cookies()
def intopoke():
    driver.get("https://www.facebook.com/pokes/?notif_id=1714500927242833&notif_t=poke&ref=notif")
def searching_hunted(str,list):
    for search in list:
        if str==search:
            return True
        else:
            continue
def pokethosefucker():
    time.sleep(10)
    countdown =2
    for name in TargetList.username:
        target = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{}]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span/span/span/a'.format(countdown)).text
        poke_text=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{}]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div/span/span'.format(countdown)).text
        if searching_hunted(target,TargetList.username) and poke_text=="戳回去":
            poke_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{}]/div/div/div[1]/div[2]/div[2]/div/div/div/div".format(countdown))
            ActionChains(driver).move_to_element(poke_button).click().perform()
            print("某個叫{}被戳了".format(target),end=" ")
            Current_time()
        countdown=countdown+1
def Current_time():
    time=datetime.datetime.now()
    if time.hour >= 12:
        print("下午 {:02d}:{:02d}:{:02d}".format(time.hour-12,time.minute,time.second))
    else:
        print("上午 {:02d}:{:02d}:{:02d}".format(time.hour,time.minute,time.second))
FacebookLogin()
time.sleep(3)
intopoke()
while True:
    pokethosefucker()
