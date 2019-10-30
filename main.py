#Created by Jérémy Fievet
# 09/2019


import glob,os,datetime,logging,subprocess,time,base64,json
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

with open('conf.json') as config_file:
    data_conf = json.load(config_file)

login = data_conf['login']
password = data_conf['password']
path = data_conf['DefaultPath']
indemKmMenu = data_conf['indemKmMenu']
villeD = data_conf['VilleD']
villeA = data_conf['VilleA']
client = data_conf['Client']
obj = data_conf['OBJ']
nbKm = data_conf['KM']




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
  #  os.system('taskkill /im chrome.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
  #  profileGoogle=data_conf['ProfileGoogle']
   # options.add_argument("user-data-dir="+profileGoogle)
    driver = webdriver.Chrome(CHROME)
    driver.get(url)
    return driver

def loginIntranet(driver):
    time.sleep(10)
    if(driver.current_url.find("login"))==-1:
        info("No cas to connect")
        return driver
    else:
        info("enter my login info to connect")
        driver.implicitly_wait(10)
        login_element = driver.find_element_by_name('login')
        login_element.send_keys(login)
        driver.implicitly_wait(10)
        passwd = driver.find_element_by_name('pwd')
        encode_passws = base64ToString(password)
        passwd.send_keys(encode_passws)
        btn_submit = driver.find_element_by_class_name('standard-button-positive')
        btn_submit.click()
        print("Login OK")
        logging.info("Login OK")
        return driver   

def addDate(obj,dateIndem_str):
    info("start addDate")
    obj.send_keys(" ")
    obj.send_keys(Keys.CONTROL,'a')
    obj.send_keys(dateIndem_str)
    obj.send_keys(Keys.TAB)
    info("end addDate")
def addKm(obj,nb):
    info("start addKm")
    obj.send_keys(" ")
    obj.send_keys(Keys.CONTROL,'a')
    obj.send_keys(nb)
    info("end addKm")

def addObj(obj,element_str,driver):
    info("addObj " + element_str)
    obj.send_keys(" ")
    obj.send_keys(Keys.CONTROL,'a')
    obj.send_keys(element_str)
    #driver.find_element_by_class_name("item item-selected").click()
    obj.send_keys(Keys.TAB)

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')



def openIntracens():
    driver = openWebBrowers("https://intranet.acensi.fr")
    driver = loginIntranet(driver)
    driver.implicitly_wait(10)
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
    return driver


def autofill(driver,dateIndem_str,tr):
      #Date
    info("add date")
    dateInput = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[1]/input")
    addDate(dateInput,dateIndem_str)
    time.sleep(1)
    #VilleD
    info("add villeD")
    villeDInpute = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[2]/input")
   # villeDInpute.send_keys(villeD)
    addObj(villeDInpute,villeD,driver)
    #VilleA
    info("add villeA")
    villeAInpute = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[3]/input")
   # villeAInpute.send_keys(villeA)
    addObj(villeAInpute,villeA,driver)
    #client
    info("add client")
    clientInput=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[4]/input")
   # clientInput.send_keys(client)
    addObj(clientInput,client,driver)
    #objet
    info(" add obj")
    objInput=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[5]/input")
    #objInput.send_keys(nbKm)
    addObj(objInput,obj,driver)
    
    #check
    info("checkbox")
    checkBox=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[7]/span/input").click()
    
    #KM
    info(" add km")
    kmInput=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+str(tr)+"]/td[8]/input")
    time.sleep(0.5)
    addObj(kmInput,nbKm,driver)
    
    #addAll
   # info(" add all")
   # submitbtn=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[10]/button").click()
    #time.sleep(60)
    #add villeD


def addElements(driver):
    debut = 1
    nextDate = date(2019,10,debut)
    dateIndem_str = nextDate.strftime("%d/%m/%Y")
    lastDayOfMonth = last_day_of_month(nextDate).strftime("%d")
    tr=2
    for i in range(debut,int(lastDayOfMonth)+1):
        nextDate = date(2019,10,debut)
        weekno = nextDate.weekday()
        dateIndem_str = nextDate.strftime("%d/%m/%Y")
        print(dateIndem_str)
        if weekno<5:
            info("Weekday" + dateIndem_str)
            autofill(driver,dateIndem_str,tr)
            tr=tr+1
        else:
            info("Weekend" + dateIndem_str)
        debut=debut+1
       
    info("sortie de boucle")
    info(dateIndem_str)
    time.sleep(4)
    

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
    driver=processing(driver)
    addElements(driver)
    logging.info('Finished')


if __name__ == '__main__':
    main(sys.argv[1:])




