import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchProduct(unittest.TestCase):

    def setUp(self):
        """Inicializa o driver do Chrome antes de cada teste."""
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000"
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url)

    def tearDown(self):
        """Fecha o navegador após cada teste."""
        print("Teste concluído. Fechando o navegador em 4 segundos...")
        time.sleep(4)
        self.driver.quit()

    def test_search_and_clear_filter(self):
        """
        Verifica se a busca por nome funciona e se o filtro pode ser limpo.
        """
        print("\nExecutando teste: Buscar e Limpar Filtro (com pausas)...")
        
        # ETAPA 1: Adicionar produtos para criar um cenário de busca
        print("-> Adicionando produtos para o teste...")
        self._add_product_for_testing("Notebook Dell Vostro", "4500.00", "8", "Notebook potente para trabalho.")
        self._add_product_for_testing("Monitor Gamer Acer", "1800.00", "12", "Monitor com alta taxa de atualização.")
        print("-> Produtos adicionados. Pausando por 3 segundos...")
        time.sleep(3)

        # ETAPA 2: Realizar uma busca
        search_term = "Notebook"
        print(f"-> Buscando pelo termo: '{search_term}'...")
        search_box = self.driver.find_element(By.NAME, "search")
        search_box.send_keys(search_term)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Buscar')]").click()
        
        # ETAPA 3: Verificar o resultado da busca
        print("-> Verificando resultado da busca. Pausando por 3 segundos...")
        time.sleep(3)
        table_text = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table"))).text
        self.assertIn("Notebook Dell Vostro", table_text)
        self.assertNotIn("Monitor Gamer Acer", table_text)
        print("-> Resultado da busca verificado com sucesso.")
        
        # ETAPA 4: Limpar o filtro de busca
        print("-> Limpando filtro de busca...")
        self.driver.find_element(By.LINK_TEXT, "Limpar").click()

        # ETAPA 5: Verificar se a lista voltou ao estado original
        print("-> Verificando resultado após limpar. Pausando por 3 segundos...")
        time.sleep(3)
        table_after_clear = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table"))).text
        self.assertIn("Notebook Dell Vostro", table_after_clear)
        self.assertIn("Monitor Gamer Acer", table_after_clear)
        print("-> Filtro limpo e resultado verificado com sucesso.")

    def _add_product_for_testing(self, name, price, quantity, description):
        """Função auxiliar para adicionar um produto rapidamente."""
        self.driver.get(self.base_url + "/add")
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(name)
        time.sleep(0.5)
        # Adicionando a descrição
        self.driver.find_element(By.NAME, "description").send_keys(description)
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "price").send_keys(price)
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "quantity").send_keys(quantity)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        self.driver.get(self.base_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)