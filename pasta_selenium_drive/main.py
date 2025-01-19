print('Hello world!')
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # ESSENCIAL PARA PROGRAMAR A SELEÇÃO DE ITENS
from selenium.webdriver.common.keys import Keys # ESSENCIAL PARA CLICAR
from selenium.webdriver.support.wait import WebDriverWait # ESPERA NO SCRIPT
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return browser
if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)
    # Como antes
    browser.get('https://www.olx.com.br/celulares/estado-df?q=iphone%2014%20pro%20max')
    
    # Espera pra econtrar o input
    aceite_buttom = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, 'adopt-accept-all-button')
        )
    )

    # # Espera pra econtrar o input
    # pesquisa_input = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, 'oraculo-60-input')
    #     )
    # )
    # pesquisa_input.send_keys('iphone 14 pro max')

    aceite_buttom.click()

    input_element = browser.find_element(By.ID, "chips-id-company_ad-Particular")
    browser.execute_script("arguments[0].click();", input_element)

    input_element_recents = browser.find_element(By.ID, "chips-id-sort-Mais Recentes")
    browser.execute_script("arguments[0].click();", input_element_recents)

    

    sleep(5)

    # Localiza todos os elementos com a classe associada aos preços
    prices = browser.find_elements(By.CSS_SELECTOR, 'h3.olx-text--body-large.olx-text--semibold')

    # Extrai e exibe os textos dos preços
    for price in prices:

        texto_limpo = price.text.replace("R$ ", "").replace(".", "")
                
        if float(texto_limpo) < 4000:
            print('produto abaixo do valor encontrado') 
            print(price.text)

    
    sleep(500)



