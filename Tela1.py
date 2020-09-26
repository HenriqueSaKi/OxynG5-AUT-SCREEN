from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class SetupTela1:
    def __init__(self):
        self.options = Options()
        self.options.add_extension('extension_0_71_0_0.crx')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=self.options)
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

    def access(self):
        self.driver.get('https://g5.oxyn.com.br/')

    def login(self):
        login = self.driver.find_element_by_id('user_email')
        password = self.driver.find_element_by_id('user_senha')
        entrar = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('') #Add your e-mail
        password.clear()
        password.send_keys('') #Add your password
        entrar.click()

    def resumoDesvios(self):
        self.driver.find_element_by_xpath("//li[@id='option1']//a[contains(text(),'Resumo de Desvios')]").click()

    def Marcador(self):
        markButton = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='marker']//a[contains(text(),'Marcadores')]")))
        markButton.click()
        marcador = self.driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Contrato de Manutenção')]")
        filterBox = self.driver.find_element_by_id('filter')
        self.action.drag_and_drop(marcador, filterBox).perform()
        aplicar = self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(), 'Aplicar')]")
        time.sleep(2)
        aplicar.click()
        time.sleep(1)

    def MaxWindow(self):
        self.driver.maximize_window()

    def Run(self):
        self.access()
        self.login()
        self.resumoDesvios()
        self.Marcador()
