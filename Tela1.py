from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time, pyautogui

options = Options()
options.add_extension('extension_0_71_0_0.crx')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
driver.maximize_window()
action = ActionChains(driver)

class SetupTela1:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://g5.oxyn.com.br/')

    def login(self):
        login = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_senha')
        entrar = driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('') #Add your e-mail
        password.clear()
        password.send_keys('') #Add your password
        entrar.click()

    def resumoDesvios(self):
        driver.find_element_by_xpath("//li[@id='option1']//a[contains(text(),'Resumo de Desvios')]").click()

    def Marcador(self):
        markButton = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='marker']//a[contains(text(),'Marcadores')]")))
        markButton.click()
        marcador = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Contrato de Manutenção')]")
        filterBox = driver.find_element_by_id('filter')
        action.drag_and_drop(marcador, filterBox).perform()
        aplicar = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(), 'Aplicar')]")
        time.sleep(2)
        aplicar.click()
        time.sleep(1)

    def MaxWindow(self):
        pyautogui.hotkey('win', 'up')

    def Run(self):
        self.access()
        self.login()
        self.resumoDesvios()
        self.Marcador()

SetupTela1().Run()
