# Teste - BestStoreMVC

<img src="img/videoBestStoreFlask.gif" width="700">

## Definição da aplicação web a ser testada

O **BestStoreMVC** é uma aplicação web desenvolvida com Blazor e .NET 9 para gerenciamento eficiente de produtos. Ele oferece uma interface moderna e responsiva para facilitar a criação, edição, visualização e exclusão de itens.

**Estrutura da Página**
A aplicação é organizada de forma intuitiva para proporcionar uma boa experiência ao usuário. Entre os principais elementos da página, estão:

- **Cadastro de Produtos:** Interface para adicionar novos produtos, incluindo informações como nome, marca, categoria, preço e descrição.

- **Edição e Exclusão:** Funcionalidade que permite modificar ou remover produtos diretamente da página de gerenciamento.

- **Validação de Formulário:** Implementação de validações visuais para garantir a integridade dos dados inseridos.

- **Design Responsivo:** Construído com Bootstrap, garantindo compatibilidade com diversos dispositivos, desde desktops até smartphones.

- **Navegação Intuitiva:** Estrutura bem definida para facilitar a interação dos usuários com os recursos disponíveis.
## Lista dos principais fluxos de interação a serem validados:


#### **Cadastro de Produtos**

1. Inserção de novos produtos no banco de dados.

2. Validação de dados obrigatórios e formatos corretos.

#### **Exibição de Produtos**

Apresentação correta das informações dos produtos cadastrados.

1. Funcionamento da paginação e carregamento dinâmico.

#### **Edição de Produtos**

1. Alteração de informações do produto e persistência das mudanças.

2. Tratamento de erros ao inserir valores inválidos.

#### **Exclusão de Produtos**

1. Remoção do produto do banco de dados sem deixar registros inválidos.

2. Confirmação de exclusão antes de deletar um item.

3. Garantia de que a remoção não afeta negativamente outros elementos da aplicação.

#### **Validação de Dados e Interface**

1. Exibição de mensagens de erro e feedback ao usuário.

2. Comportamento correto dos botões de ação (salvar, editar, excluir).

**********************************************************************************************************************************************

<h1 align="center">Teste_Cadastro_Novo_Produto</h1>

| Condição               | Regra 1   | Regra 2                                           | Regra 3                                           | Regra 4                                           | Regra 5                                                |
|------------------------|-----------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|----------------------------------------------------------|
| nome preenchido        | SIM       | NÃO                                               | SIM                                               | SIM                                               | SIM                                                      |
| marca preenchida       | SIM       | SIM                                               | NÃO                                               | SIM                                               | SIM                                                      |
| categoria selecionada  | SIM       | SIM                                               | SIM                                               | SIM                                               | SIM                                                      |
| preço preenchido       | SIM       | SIM                                               | SIM                                               | NÃO                                               | SIM                                                      |
| descrição preenchida   | SIM       | SIM                                               | SIM                                               | SIM                                               | NÃO                                                      |
| **ação esperada**      | Criação OK | Mensagem de erro ("O campo Nome é obrigatório.") | Mensagem de erro ("O campo Marca é obrigatório.") | Mensagem de erro ("O valor '' é inválido.")       | Mensagem de erro ("O campo Descrição é obrigatório.")    |

## Observações sobre a Tabela de Decisão

Pode-se concluir que, **caso qualquer uma das propriedades obrigatórias do produto não seja preenchida, o cadastro não será efetuado com sucesso**.

Em relação à categoria, **não foi realizado um teste com esse campo vazio porque o sistema oferece uma lista fechada de opções predefinidas (como "Phones", "Computers", "Accessories" e "Outros")**. Portanto, **a categoria sempre estará preenchida por padrão, não sendo possível deixá-la em branco**.

### Pontos de Atenção:
- O campo **preço é obrigatório**, e sua ausência impede o cadastro.
- Contudo, o sistema **aceita o valor zero (0)** como um preço válido.  
  Isso levanta a seguinte questão: **esse comportamento é realmente desejado?**  
  Em muitos contextos, um produto com preço igual a zero pode representar uma falha de entrada ou indicar a necessidade de uma validação adicional.

  ***********************************************************************************************************************************************************************************

<h1 align="center">Teste_Cadastro_Novo_Produto</h1>

| Condição               | Regra 1   | Regra 2                                           | Regra 3                                           | Regra 4                                           | Regra 5                                                |
|------------------------|-----------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|----------------------------------------------------------|
| nome preenchido        | SIM       | NÃO                                               | SIM                                               | SIM                                               | SIM                                                      |
| marca preenchida       | SIM       | SIM                                               | NÃO                                               | SIM                                               | SIM                                                      |
| categoria selecionada  | SIM       | SIM                                               | SIM                                               | SIM                                               | SIM                                                      |
| preço preenchido       | SIM       | SIM                                               | SIM                                               | NÃO                                               | SIM                                                      |
| descrição preenchida   | SIM       | SIM                                               | SIM                                               | SIM                                               | NÃO                                                      |
| **ação esperada**      | Criação OK | Mensagem de erro ("O campo Nome é obrigatório.") | Mensagem de erro ("O campo Marca é obrigatório.") | Mensagem de erro ("O valor '' é inválido.")       | Mensagem de erro ("O campo Descrição é obrigatório.")    |

## ✅ Casos de Teste - Criação de Produto

### 🔹 Caso de Teste 1 – Criação bem-sucedida
**Objetivo**: Verificar se o sistema permite a criação de um produto quando todos os campos obrigatórios são devidamente preenchidos.

**Pré-condições**: Usuário autenticado com permissão para cadastrar produtos.

**Entradas**:
- Nome: preenchido
- Marca: preenchida
- Categoria: selecionada
- Preço: preenchido
- Descrição: preenchida

**Passos**:
1. Acessar a tela de cadastro de produto.
2. Preencher todos os campos obrigatórios com dados válidos.
3. Clicar no botão "Salvar".

**Resultado Esperado**: Produto criado com sucesso. Mensagem de confirmação exibida.

---

### 🔹 Caso de Teste 2 – Falha por campo obrigatório não preenchido
**Objetivo**: Verificar se o sistema bloqueia a criação de um produto quando qualquer campo obrigatório está vazio ou inválido.

**Pré-condições**: Usuário autenticado com permissão para cadastrar produtos.

**Entradas (exemplos de falha)**:
- Nome: vazio **ou**
- Marca: vazia **ou**
- Categoria: não selecionada **ou**
- Preço: vazio/inválido **ou**
- Descrição: vazia

**Passos**:
1. Acessar a tela de cadastro de produto.
2. Deixar um ou mais campos obrigatórios vazios ou inválidos.
3. Clicar no botão "Salvar".

**Resultado Esperado**: Produto não é criado. O sistema exibe uma mensagem de erro específica conforme o campo inválido, como:
   - "O campo Nome é obrigatório."
   - "O campo Marca é obrigatório."
   - "O valor '' é inválido."
   - "O campo Descrição é obrigatório."
   
---

<h1 align="center"> Teste_Edição_Produto</h1>

| condição                 | Regra 1   | regra 2                                         | regra 3                                  | regra 4                                    | regra 5                                              |
|:-------------------------|:----------|:------------------------------------------------|:-----------------------------------------|:-------------------------------------------|:-----------------------------------------------------|
| nome editado ≠ de vazio  | SIM       | NÃO                                             | SIM                                      | SIM                                        | SIM                                                  | NÃO       |
| marca editada ≠ de vazio | SIM       | SIM                                             | NÃO                                      | SIM                                        | SIM                                                  | NÃO       |
| categoria selecionada    | SIM       | SIM                                             | SIM                                      | SIM                                        | SIM                                                  | SIM       |
| preço editado ≠ de vazio | SIM       | SIM                                             | SIM                                      | NÃO                                        | SIM                                                  | NÃO       |
| descrição preenchida     | SIM       | SIM                                             | SIM                                      | SIM                                        | NÃO                                                  | NÃO       |
| ação esperada            | Edição OK | Mensagem de erro("O campo Nome é obrigatório.") | Mensagem("O campo Marca é obrigatório.") | Mensagem de erro("O valor '' é inválido.") | Mensagem de erro("O campo Descrição é obrigatório.") | 



## ✅ Casos de Teste – Edição de Produto

### 🔹 Caso de Teste 1 – Edição bem-sucedida
**Objetivo**: Verificar se o sistema permite editar um produto quando todos os campos obrigatórios são preenchidos corretamente.

**Pré-condições**: Produto existente no sistema.

**Entradas**:  
- Todos os campos preenchidos e selecionados

**Passos**:
1. Acessar o formulário de edição do produto.
2. Editar os campos com valores válidos.
3. Clicar no botão "Salvar".

**Resultado Esperado**: Produto atualizado com sucesso. Mensagem de confirmação exibida.

---

### 🔹 Caso de Teste 2 – Falha por campo obrigatório não preenchido
**Objetivo**: Verificar se o sistema bloqueia a edição de um produto quando qualquer campo obrigatório está vazio ou inválido.

**Pré-condições**: Produto existente no sistema.

**Entradas (exemplos de falha)**:
- Nome: vazio **ou**
- Marca: vazia **ou**
- Categoria: não selecionada **ou**
- Preço: vazio/inválido **ou**
- Descrição: vazia

**Passos**:
1. Acessar a tela de edição de produto.
2. Deixar um ou mais campos obrigatórios vazios ou inválidos.
3. Clicar no botão "Enviar".

**Resultado Esperado**: Produto não é editado. O sistema exibe uma mensagem de erro específica conforme o campo inválido, como:
   - "O campo Nome é obrigatório."
   - "O campo Marca é obrigatório."
   - "O valor '' é inválido."
   - "O campo Descrição é obrigatório."
   
---
<h1 align="center">Teste_Exclusao_Produto</h1>

<div align="center">

| condição                 | Regra 1          | Regra 2              |
|-------------------------|------------------|-----------------------|
| confirmação de exclusão | SIM              | NÃO                   | 
| cancelamento de exclusão| NÃO              | SIM                   | 
| ação esperada           | Produto deletado | Produto não deletado  | 

</div>


## ✅Casos de Teste – Exclusão de Produto

### 🔸 Caso de Teste 1 – Confirmação de Exclusão
**Objetivo**: Verificar se o sistema remove corretamente um produto após a confirmação do usuário.

**Pré-condições**: Produto existente no sistema.

**Entradas**:  
- Produto a ser excluído

**Passos**:
1. Clicar no botão "Excluir" do produto.
2. Confirmar a exclusão na janela/modal de confirmação.

**Resultado Esperado**: Produto deletado com sucesso. Mensagem de confirmação exibida.

---

### 🔸 Caso de Teste 2 – Cancelamento da Exclusão
**Objetivo**: Verificar se o sistema mantém o produto quando a exclusão é cancelada.

**Pré-condições**: Produto existente no sistema.

**Entradas**:  
- Produto a ser excluído

**Passos**:
1. Clicar no botão "Excluir".
2. Na janela/modal de confirmação, clicar em "Cancelar".

**Resultado Esperado**: Produto não é deletado. Nenhuma alteração é feita. O usuário permanece na mesma tela.\

---

## Prints dos logs de execução

### ➕ Adicionando um produto
<img src="img/add.PNG" width="700">

### ✏ Editando um produto
<img src="img/edit.PNG" width="700">

### 🗑 Deletando um produto
<img src="img/delete.PNG" width="700">
