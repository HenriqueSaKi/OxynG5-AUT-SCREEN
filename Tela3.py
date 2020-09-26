from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import timedelta
import time, datetime, pyautogui

options = Options()
options.add_extension('extension_0_71_0_0.crx')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
driver.maximize_window()
action = ActionChains(driver)
datas = [
            {"instituicao": "Hospital São Luiz São Caetano do Sul", "modelo": "EN - Relatório Eficiencia Energética - CAG"},
            {"instituicao": "Hospital São Luiz Itaim", "modelo": "EN - Relatório Eficiencia Energética - CAG"},
            {"instituicao": "Hospital Unimed", "modelo": "EN - Relatório Eficiencia Energética - CAG"},
            {"instituicao": "Honda", "modelo": "EN - Relatório Eficiencia Energética - CAG"},
            {"instituicao": "Hospital São Luiz Morumbi", "modelo": "EN - Relatorio Eficiencia Energetica"},
            {"instituicao": "Hospital Copa Star", "modelo": "EN - Relatório Eficiencia Energética - CAG"},
            {"instituicao": "Hospital e Maternidade Brasil", "modelo": "EN - Relatório Eficiencia Energética - CAG"}]

class SetupTela3:
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

    def dateCalculator(self):
        currentDate = datetime.datetime.today()
        lastMonthDate = currentDate - timedelta(days=31)
        # Initial date
        initialDateField = driver.find_element_by_id('initial-date')
        initialDateField.click()
        initialDateField.clear()
        time.sleep(1)
        initialDateField.send_keys(lastMonthDate.strftime("%d/%m/%Y"))  # Add last month date
        pyautogui.press('enter')
        # Final date
        finalDateField = driver.find_element_by_id('final-date')
        finalDateField.click()
        finalDateField.clear()
        time.sleep(1)
        finalDateField.send_keys(currentDate.strftime("%d/%m/%Y"))
        pyautogui.press('enter')

    def generatorButton(self):
        generator = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(),'Gerar')]")
        generator.click()

    def pageDown(self):
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        pyautogui.press('esc')
        time.sleep(1)

    def maximizePDF(self):
        pyautogui.moveTo(x=1854, y=871, duration=2.0)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1.5)

    def openReport(self):
        for i in range(7):
            fields = datas[i]
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//tbody//tr[3]")))
            select = driver.find_element_by_xpath("//span[@id='select2-sites-container']")
            select.click()
            time.sleep(2)
            insertName = driver.find_element_by_xpath("//input[@class='select2-search__field']")
            insertName.send_keys(fields["instituicao"])
            time.sleep(1)
            pyautogui.press('enter')
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//table[@id='desvios']//tbody//tr[2]//td[2]//a[contains(text(), '{}')]".format(fields["instituicao"]))))
            report = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'report')))
            report.click()
            time.sleep(3)
            reportModel = driver.find_element_by_id('select2-report-model-select2-container')
            reportModel.click()
            findModel = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
            findModel.send_keys(fields["modelo"])
            pyautogui.press('enter')
            time.sleep(1)
            self.dateCalculator()
            self.generatorButton()
            self.pageDown()
            if i == 6:
                pyautogui.hotkey('Ctrl', 'w')  # close report tab

    def reportPosition(self):
        tab = ['7', '6', '5', '4', '3', '2', '1']
        wait = 0
        print("Wait 10 seconds")
        while wait < 10:
            wait = wait + 1
            time.sleep(0.8)
        print("Ready...")

        for i in range(7):
            pyautogui.moveTo(x=960, y=540)  # center of 1920x1080 screen
            time.sleep(2)
            pyautogui.hotkey('ctrl', tab[i])
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            pyautogui.write('Grafico', interval='0.1')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            self.maximizePDF()
            time.sleep(1)

    def MaxWindow(self):
        pyautogui.hotkey('win', 'up')

    def Run(self):
        self.access()
        self.login()
        self.openReport()
        self.reportPosition()

SetupTela3().Run()
