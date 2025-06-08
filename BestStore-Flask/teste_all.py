import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFullCycle(unittest.TestCase):

    def setUp(self):
        """Inicializa o driver do Chrome antes de cada teste."""
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000"
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url)

    def tearDown(self):
        """Fecha o navegador após cada teste."""
        print("-> Teste completo finalizado. Fechando o navegador em 5 segundos...")
        time.sleep(5)
        self.driver.quit()

    def test_complete_workflow(self):
        """
        Executa um teste completo de ponta a ponta: ADD -> EDIT -> SEARCH -> DELETE.
        """
        print("\n--- INICIANDO TESTE DE FLUXO COMPLETO ---")

        # --- ETAPA 1: ADICIONAR UM PRODUTO ---
        print("\n[ETAPA 1/4] Adicionando um novo produto...")
        self.driver.find_element(By.LINK_TEXT, "Adicionar Produto").click()
        time.sleep(2)

        product_name_original = "Cadeira de Escritório Ergonômica"
        
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(product_name_original)
        time.sleep(1)
        self.driver.find_element(By.NAME, "description").send_keys("Cadeira com suporte lombar ajustável")
        time.sleep(1)
        self.driver.find_element(By.NAME, "price").send_keys("750.00")
        time.sleep(1)
        self.driver.find_element(By.NAME, "quantity").send_keys("15")
        time.sleep(2)
        
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
        
        print("-> Verificando se o produto foi adicionado...")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        self.assertIn(product_name_original, self.driver.find_element(By.TAG_NAME, "table").text)
        print("-> SUCESSO: Produto adicionado.")
        time.sleep(3)

        # --- ETAPA 2: EDITAR O PRODUTO CRIADO ---
        print("\n[ETAPA 2/4] Editando o produto recém-criado...")
        self.driver.find_element(By.XPATH, f"//td[text()='{product_name_original}']/following-sibling::td/a[contains(@class, 'btn-warning')]").click()
        time.sleep(2)

        product_name_edited = "Cadeira Presidente Confort"
        
        name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        name_field.clear()
        time.sleep(1)
        name_field.send_keys(product_name_edited)
        time.sleep(1)

        quantity_field = self.driver.find_element(By.NAME, "quantity")
        quantity_field.clear()
        time.sleep(1)
        quantity_field.send_keys("20") # Nova quantidade
        time.sleep(2)
        
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()

        print("-> Verificando se o produto foi editado...")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        self.assertIn(product_name_edited, self.driver.find_element(By.TAG_NAME, "table").text)
        self.assertNotIn(product_name_original, self.driver.find_element(By.TAG_NAME, "table").text)
        print("-> SUCESSO: Produto editado.")
        time.sleep(3)
        
        # --- ETAPA 3: BUSCAR O PRODUTO EDITADO ---
        print("\n[ETAPA 3/4] Buscando o produto editado...")
        search_box = self.driver.find_element(By.NAME, "search")
        search_box.send_keys("Presidente Confort")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Buscar')]").click()
        
        print("-> Verificando resultado da busca...")
        time.sleep(3)
        self.assertIn(product_name_edited, self.driver.find_element(By.TAG_NAME, "table").text)
        print("-> SUCESSO: Busca encontrou o produto correto.")
        
        self.driver.find_element(By.LINK_TEXT, "Limpar").click()
        time.sleep(2)

        # --- ETAPA 4: DELETAR O PRODUTO ---
        print("\n[ETAPA 4/4] Deletando o produto...")
        self.driver.find_element(By.XPATH, f"//td[text()='{product_name_edited}']/following-sibling::td/a[contains(@class, 'btn-danger')]").click()
        time.sleep(2)
        
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        
        print("-> Verificando se o produto foi deletado...")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
        self.assertNotIn(product_name_edited, self.driver.find_element(By.TAG_NAME, "body").text)
        print("-> SUCESSO: Produto deletado.")
        time.sleep(3)

        print("\n--- TESTE DE FLUXO COMPLETO CONCLUÍDO COM ÊXITO ---")

if __name__ == '__main__':
    unittest.main(verbosity=2)