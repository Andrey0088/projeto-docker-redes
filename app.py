import os
import psycopg2
from flask import Flask
import time

app = Flask(__name__)

def get_db_connection():
    """Tenta se conectar ao banco de dados com algumas tentativas."""
    conn = None
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                # A correção está aqui! O host é o nome do serviço 'db' no docker-compose.
                host="db", 
                database=os.environ.get("POSTGRES_DB"),
                user=os.environ.get("POSTGRES_USER"),
                password=os.environ.get("POSTGRES_PASSWORD")
            )
            print("Conexão com o banco de dados bem-sucedida!")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar no banco de dados: {e}")
            retries -= 1
            print(f"Tentando novamente em 5 segundos... ({retries} tentativas restantes)")
            time.sleep(5)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    
    # Se a conexão falhar após todas as tentativas, conn será None
    if conn is None:
        return "<h1>Falha ao conectar no banco de dados após várias tentativas.</h1>", 500

    # Apenas para testar, vamos pegar a versão do PostgreSQL
    try:
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
    except Exception as e:
        return f"<h1>Erro ao executar a query: {e}</h1>", 500
    finally:
        conn.close()

    return f"<h1>Conexão com o Banco de Dados bem-sucedida!</h1><p>Versão do PostgreSQL: {db_version[0]}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
