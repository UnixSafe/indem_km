#Created by Jérémy Fievet
# 09/2019


import glob,os,datetime,logging,subprocess,time,zipfile,base64,json
import array as arr 
from datetime import timedelta,datetime,date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback
import queue
import getopt,sys

#Variable

#Chrome Path
CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chromedriver.exe')
#Task Path
#TASK = os.path.join('C:\\', 'Users', 'Administrateur', 'Desktop','test_biotymel.exe')
with open('conf.json') as config_file:
    data_conf = json.load(config_file)

login = data_conf['login']
password = data_conf['password']
path = data_conf['DefaultPath']
indemKmMenu = data_conf['indemKmMenu']



os.chdir(path)
today = datetime.today()
today_file_name = today.strftime("%Y_%d_%m")+"_listDir.log"
print("filename =",today_file_name)


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)

def info(text):
    print(text)
    logging.info(text)

def openWebBrowers(url):
    os.system('taskkill /im chrome.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    profileGoogle=data_conf['ProfileGoogle']
    options.add_argument("user-data-dir="+profileGoogle)
    driver = webdriver.Chrome(CHROME,options=options)
    driver.get(url)
    return driver

def loginIntranet(driver):
    time.sleep(10)
    if(driver.current_url.find("login"))==-1:
        info("No cas to connect")
        return driver
    else:
        info("enter my login info to connect")
        driver.implicitly_wait(3000)
        login_element = driver.find_element_by_name('login')
        login_element.send_keys(login)
        driver.implicitly_wait(30)
        passwd = driver.find_element_by_name('pwd')
        encode_passws = base64ToString(password)
        passwd.send_keys(encode_passws)
        btn_submit = driver.find_element_by_class_name('standard-button-positive')
        btn_submit.click()
        print("Login OK")
        logging.info("Login OK")
        return driver   




def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')



def openIntracens():
    driver = openWebBrowers("https://intranet.acensi.fr")
    driver = loginIntranet(driver)
    print("go to the indem km menu")
    logging.info(" go to the indem km menu")
    indemMenuToClic = driver.find_element_by_id("MES_INDEMNITES_KILOMETRIQUES")
    indemMenuToClic.click()
    time.sleep(10)
    return driver

def processing(driver):
    #autoComplet
    info("start  processing function")
    btnCree = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/button")
    btnCree.click()
    info('click sur créer une nouvelle ...')
    debut = 1
    nextDate = date(2019,10,debut)
    dateIndem_str = nextDate.strftime("%d/%m/%Y")
    lastDayOfMonth = last_day_of_month(nextDate).strftime("%d")
    for i in range(debut,int(lastDayOfMonth)+1):
        info("dans la boucle")
        nextDate = date(2019,10,debut)
        dateIndem_str = nextDate.strftime("%d/%m/%Y")
        print(dateIndem_str)
        driver.implicitly_wait(3000)
        debut=debut+1
    info("sortie de boucle")
    info(dateIndem_str)
    dateInput = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[1]/input")
    dateInput.send_keys(dateIndem_str)
    time.sleep(60)
    #Créer une nouvelle indemnité kilométrique
    info("end processing function")
    return 0


def main(argv):
    print("debut main")
 
    filenameLog = os.getcwd()+'\\'+today_file_name
    print(filenameLog)
    print( os.path.join(os.path.dirname(os.path.realpath(__file__))))
    logging.basicConfig(filename=filenameLog,level=logging.INFO,\
        format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
    logging.info('Started')
    driver=openIntracens()
    processing(driver)
    logging.info('Finished')


if __name__ == '__main__':
    main(sys.argv[1:])




