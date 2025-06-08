import sqlite3
import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    g,  
    abort,
)

# configuração do aplicativo
app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'
# define o caminho do banco de dados no diretório de instância do flask
app.config['DATABASE'] = os.path.join(app.instance_path, 'project.db')


try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# funções do banco

def get_db():
    """
    Cria e retorna uma nova conexão com o banco de dados se não houver uma
    na requisição atual (g). Usa sqlite3.Row para acessar colunas pelo nome.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    """
    Fecha a conexão com o banco de dados ao final da requisição.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """
    Inicializa o banco de dados executando o schema.sql.
    """
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@app.cli.command('init-db')
def init_db_command():
    """Define o comando de terminal 'flask init-db' para criar as tabelas."""
    init_db()
    print('Banco de dados inicializado com sucesso.')

# rotas da aplicação

@app.route('/')
def index():
    """ Rota principal que exibe a lista de produtos e permite busca. """
    db = get_db()
    query = request.args.get('search')
    if query:
        # filtra produtos cujo nome contém o texto da busca
        search_term = f'%{query}%'
        products_list = db.execute(
            'SELECT * FROM product WHERE name LIKE ? ORDER BY id', (search_term,)
        ).fetchall()
    else:
        products_list = db.execute('SELECT * FROM product ORDER BY id').fetchall()
    return render_template('index.html', products=products_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """ Rota para adicionar um novo produto. """
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        db = get_db()
        db.execute(
            'INSERT INTO product (name, description, price, quantity) VALUES (?, ?, ?, ?)',
            (name, description, price, quantity)
        )
        db.commit()

        flash('Produto adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit(product_id):
    """ Rota para editar um produto existente. """
    db = get_db()
    # busca o produto pelo ID ou retorna 404 se não for encontrado
    product = db.execute('SELECT * FROM product WHERE id = ?', (product_id,)).fetchone()
    if product is None:
        abort(404, f"Produto com ID {product_id} não encontrado.")

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        db.execute(
            'UPDATE product SET name = ?, description = ?, price = ?, quantity = ? WHERE id = ?',
            (name, description, price, quantity, product_id)
        )
        db.commit()

        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', product=product)

@app.route('/delete/<int:product_id>')
def delete(product_id):
    """ Rota para deletar um produto. """
    db = get_db()
    # valida se o produto existe antes de deletar
    product = db.execute('SELECT id FROM product WHERE id = ?', (product_id,)).fetchone()
    if product is None:
        abort(404, f"Produto com ID {product_id} não encontrado.")
    
    db.execute('DELETE FROM product WHERE id = ?', (product_id,))
    db.commit()

    flash('Produto deletado com sucesso!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)