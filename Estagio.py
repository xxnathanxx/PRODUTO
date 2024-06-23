from flask import Flask, request, redirect

app = Flask(__name__)

products = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['productName']
        product_description = request.form['productDescription']
        product_value = float(request.form['productValue'])
        product_available = request.form['productAvailable']
        
        products.append({
            'name': product_name,
            'description': product_description,
            'value': product_value,
            'available': product_available
        })
        
        return redirect('/list')
    
    return '''
    <h1>Cadastro de Produto</h1>
    <form action="/" method="post">
        <label for="productName">Nome do produto:</label><br>
        <input type="text" id="productName" name="productName" required><br><br>
        
        <label for="productDescription">Descrição do produto:</label><br>
        <input type="text" id="productDescription" name="productDescription" required><br><br>
        
        <label for="productValue">Valor do produto:</label><br>
        <input type="number" id="productValue" name="productValue" step="0.01" required><br><br>
        
        <label for="productAvailable">Disponível para venda:</label><br>
        <select id="productAvailable" name="productAvailable" required>
            <option value="sim">Sim</option>
            <option value="não">Não</option>
        </select><br><br>
        
        <button type="submit">Cadastrar Produto</button>
    </form>
    <br>
    <a href="/list">Ver lista de produtos</a>
    '''

@app.route('/list')
def list_products():
    sorted_products = sorted(products, key=lambda x: x['value'])
    
    product_list = '<h1>Lista de Produtos</h1>'
    product_list += '<table border="1"><tr><th>Nome</th><th>Valor</th></tr>'
    for product in sorted_products:
        product_list += f'<tr><td>{product["name"]}</td><td>R${product["value"]:.2f}</td></tr>'
    product_list += '</table>'
    
    product_list += '<br><a href="/">Cadastrar Novo Produto</a>'
    
    return product_list

if __name__ == '__main__':
    app.run(debug=True, port=8080)
