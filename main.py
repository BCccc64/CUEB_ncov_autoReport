from selenium import webdriver
import os,time

class cueb:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path=os.path.dirname(__file__)+'/geckodriver.exe',options=options)
        self.driver.implicitly_wait(3)

    def login(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/input").send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/input").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]").click()

    def submit(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a").click()
        name = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[2]/div/input").get_attribute('value')
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]").click()
            message = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]").text
        except:
            message = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]").text
        finally:
            print("{}: {}".format(name,message))

    def run(self):
        self.driver.get('https://yqapp.cueb.edu.cn/ncov/wap/default/index')
        self.login()
        self.submit()
        time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    username = ""	#学号
	password = ""	#Sjm+身份证后6位
	cueb(username,password).run()
