from flask import Flask
import pandas as pd

df = pd.read_csv('Formulario_Tabela.csv', index_col=False)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!1!1!</p>"

@app.route('/hello')
def dataframess():
    return df.to_html(header="true", table_id="table")

if __name__ == "__main__":
    app.run(debug=True, port=9191)