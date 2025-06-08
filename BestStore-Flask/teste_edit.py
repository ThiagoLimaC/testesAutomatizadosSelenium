import unittest
import time  # Importa a biblioteca time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEditProduct(unittest.TestCase):

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

    def test_edit_existing_product(self):
        """
        Verifica se é possível editar um produto existente.
        """
        print("\nExecutando teste: Editar Produto Existente (com pausas longas)...")
        
        # ETAPA 1: Criar um produto para poder ser editado
        print("-> Adicionando produto inicial...")
        self._add_product_for_testing("Produto a ser Editado", "50.00", "10")
        print("-> Produto inicial adicionado. Pausando por 2 segundos...")
        time.sleep(2)

        # ETAPA 2: Encontrar e clicar no botão de edição
        print("-> Clicando no botão de edição...")
        edit_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//td[text()='Produto a ser Editado']/following-sibling::td/a[contains(@class, 'btn-warning')]"
        )))
        edit_button.click()
        print("-> Página de edição aberta. Pausando por 2 segundos...")
        time.sleep(2)

        # ETAPA 3: Limpar os campos e preencher com novos dados
        print("-> Preenchendo o formulário com novos dados...")
        new_name = "Produto Efetivamente Editado"
        new_quantity = "199"

        name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        name_field.clear()
        time.sleep(0.5)
        name_field.send_keys(new_name)
        time.sleep(0.5)
        
        quantity_field = self.driver.find_element(By.NAME, "quantity")
        quantity_field.clear()
        time.sleep(0.5)
        quantity_field.send_keys(new_quantity)
        print("-> Formulário preenchido. Pausando por 2 segundos...")
        time.sleep(2)
        
        # Envia o formulário
        print("-> Enviando formulário de edição...")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
        print("-> Formulário enviado. Pausando por 2 segundos...")
        time.sleep(2)
        
        # ETAPA 4: Verificar as confirmações
        print("-> Verificando resultados...")
        success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        self.assertIn("Produto atualizado com sucesso!", success_message.text)
        
        table_text = self.driver.find_element(By.TAG_NAME, "table").text
        self.assertIn(new_name, table_text)
        self.assertIn(new_quantity, table_text)
        self.assertNotIn("Produto a ser Editado", table_text)
        print("-> Verificações concluídas com sucesso!")

    def _add_product_for_testing(self, name, price, quantity):
        """Função auxiliar para adicionar um produto rapidamente, agora com pausas."""
        self.driver.get(self.base_url + "/add")
        name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        name_field.send_keys(name)
        time.sleep(0.5)
        
        price_field = self.driver.find_element(By.NAME, "price")
        price_field.send_keys(price)
        time.sleep(0.5)

        quantity_field = self.driver.find_element(By.NAME, "quantity")
        quantity_field.send_keys(quantity)
        time.sleep(1)
        
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        self.driver.get(self.base_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)