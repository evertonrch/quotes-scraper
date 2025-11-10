from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Scraper:
    def __init__(self, url: str, timeout: int = 10, headless: bool = True):
        self.url = url
        self.timeout = timeout
        self.headless = headless

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )

    def run(self):
        logging.info(f"Iniciando scraper para: {self.url}")

        try:
            with webdriver.Chrome(
                service=Service(),
                options=self.__options()
            ) as driver:

                wait = WebDriverWait(driver, self.timeout)
                driver.get(self.url)
                logging.info("Página carregada com sucesso.")

                next_button = wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "next"))
                )

                link = next_button.find_element(By.TAG_NAME, "a")
                link.click()
                logging.info("Botão 'next' clicado com sucesso.")

        except Exception as e:
            logging.error(f"Erro durante o scraping: {e}", exc_info=True)

    def __options(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        return options
