import unittest
import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddProduct(unittest.TestCase):

    def setUp(self):
        """Inicializa o driver do Chrome antes de cada teste."""
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000"
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url)

    def tearDown(self):
        """Fecha o navegador após cada teste."""
        
        time.sleep(3)
        self.driver.quit()

    def test_add_new_product(self):
        """
        Verifica a funcionalidade de adicionar um novo produto.
        """
        print("\nExecutando teste: Adicionar Novo Produto (com pausas)...")

        # Acessa a página de adição de produto
        self.driver.find_element(By.LINK_TEXT, "Adicionar Produto").click()
        time.sleep(1) 

        # Define os dados do produto a ser criado
        product_name = "Webcam Logitech C920"
        product_price = "450.00"

        # Aguarda o formulário carregar e preenche os campos com pausas
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(product_name)
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "description").send_keys("Webcam Full HD para videoconferências")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "price").send_keys(product_price)
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "quantity").send_keys("30")
        time.sleep(1) 

        # Envia o formulário
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
        
        
        time.sleep(2)

        # Verifica a mensagem de sucesso
        success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        self.assertIn("Produto adicionado com sucesso!", success_message.text)

        # Verifica se o novo produto aparece na tabela da página inicial
        table_text = self.driver.find_element(By.TAG_NAME, "table").text
        self.assertIn(product_name, table_text)
        
        self.assertIn("450.00", table_text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
