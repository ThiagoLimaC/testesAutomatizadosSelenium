import os
import tempfile
import pytest

from app import app, init_db, get_db


# configura o ambiente de teste

@pytest.fixture
def client():
    
    db_fd, db_path = tempfile.mkstemp()
    app.config['DATABASE'] = db_path
    app.config['TESTING'] = True

    
    with app.test_client() as client:
        # cria o banco de dados de teste
        with app.app_context():
            init_db()
        
        yield client

    
    os.close(db_fd)
    os.unlink(db_path)

def test_loading_paginaInicial(client):
    print("\nExecutando teste Pytest: Carregamento da Página Inicial...")
    # usa o cliente de teste para fazer uma requisição
    resposta = client.get('/')
    
    
    assert resposta.status_code == 200
    assert b'Lista de Produtos' in resposta.data
    print("-> SUCESSO: Página inicial carregada.")


def test_adicionar_produto(client):
    """Testa a lógica completa de adicionar um produto."""
    print("\nExecutando teste Pytest: Adicionar Produto...")
    # usa o cliente de teste para fazer uma requisição
    resposta = client.post('/add', data={
        'name': 'Mouse Gamer',
        'description': 'Mouse com RGB',
        'price': '250.00',
        'quantity': '50'
    }, follow_redirects=True)


    assert resposta.status_code == 200
    assert b'Produto adicionado com sucesso!' in resposta.data
    assert b'Mouse Gamer' in resposta.data
    print("-> SUCESSO: Produto adicionado.")


def test_editar_produto(client):
    """Testa a lógica completa de editar um produto."""
    print("\nExecutando teste Pytest: Editar Produto...")
    # adiciona um produto só para poder editar
    client.post('/add', data={
        'name': 'Produto Antigo', 
        'description': 'Uma descrição qualquer', 
        'price': '10.0', 
        'quantity': '5'
    })

    resposta = client.post('/edit/1', data={
        'name': 'Produto Novo Editado',
        'description': 'Descricao nova e melhorada',
        'price': '199.99',
        'quantity': '20'
    }, follow_redirects=True)
    
    assert resposta.status_code == 200
    assert b'Produto atualizado com sucesso!' in resposta.data
    assert b'Produto Novo Editado' in resposta.data
    assert b'Produto Antigo' not in resposta.data
    print("-> SUCESSO: Produto editado.")


def test_deletar_produto(client):
    print("\nExecutando teste Pytest: Deletar Produto...")
    # adiciona um produto só para poder deletar

    client.post('/add', data={
        'name': 'Item a ser Deletado', 
        'description': 'Uma descrição qualquer',
        'price': '1.0', 
        'quantity': '1'
    })
    
    resposta = client.get('/delete/1', follow_redirects=True)

    assert resposta.status_code == 200
    assert b'Produto deletado com sucesso!' in resposta.data
    assert b'Item a ser Deletado' not in resposta.data
    print("-> SUCESSO: Produto deletado.")