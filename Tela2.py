from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
driver.maximize_window()

class SetupTela2:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://g5.oxyn.com.br/')

    def deviation(self):
        driver.get('https://g5.oxyn.com.br/G5/deviation')

    def login(self):
        login = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_senha')
        entrar = driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('') #Add your e-mail
        password.clear()
        password.send_keys('') #Add your password
        entrar.click()

    def NewTab(self):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        self.deviation()
        time.sleep(2)

    def apply(self):
        applyButton = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(),'Aplicar')]")
        applyButton.click()

    def Conex(self):
        action1 = ActionChains(driver)
        WebDriverWait(driver,120).until(EC.visibility_of_element_located((By.XPATH,"//tbody//tr[3]")))
        marcador = driver.find_element_by_class_name("marker-label")
        marcador.click()
        contratoBox = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Contrato')]")
        filterBox = driver.find_element_by_id('filter')
        action1.reset_actions()
        action1.drag_and_drop(contratoBox, filterBox).perform()
        conexBox = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Conexão')]")
        filterContratoBox = driver.find_element_by_xpath("//ul[@id='filter']//li[1]//a")
        action1.drag_and_drop(conexBox,filterContratoBox).perform()
        action1.reset_actions()
        close2ndBox = driver.find_element_by_xpath("//ul[@id='filter']//li[2]//a[@href='#']")
        close2ndBox.click()
        time.sleep(2)
        aplicar = driver.find_element_by_xpath("//button[contains(text(),'Aplicar')]")
        aplicar.click()
        time.sleep(1)

    def Comun(self):
        action2 = ActionChains(driver)
        WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "//tbody//tr[3]")))
        marcador = driver.find_element_by_class_name("marker-label")
        marcador.click()
        WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='labels']")))
        contratoBox2 = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Contrato')]")
        contratoBox2.click()
        filterBox2 = driver.find_element_by_id('filter')
        action2.reset_actions()
        action2.drag_and_drop(contratoBox2, filterBox2).perform()
        comuBox = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Comunicação')]")
        filterContratoBox2 = driver.find_element_by_xpath("//ul[@id='filter']//li[1]//a")
        action2.reset_actions()
        action2.drag_and_drop(comuBox, filterContratoBox2).perform()
        close2ndBox = driver.find_element_by_xpath("//ul[@id='filter']//li[2]//a[@href='#']")
        close2ndBox.click()
        time.sleep(2)
        aplicar = driver.find_element_by_xpath("//button[contains(text(),'Aplicar')]")
        aplicar.click()
        time.sleep(1)

    def MaxWindow(self):
        driver.maximize_window()

    def Run(self):
        for i in range(2):
            if i == 0:
                self.access()
                self.login()
                self.Conex()
            if i == 1:
                self.NewTab()
                self.Comun()
