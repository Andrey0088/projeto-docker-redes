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
    
    if conn is None:
        return """
        <html>
        <head>
            <title>Erro de Conexão</title>
            <style>
                body {
                    background-color: #2b2b2b;
                    color: #ff4d4d;
                    font-family: 'Arial', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }
                h1 { font-size: 2.5em; }
            </style>
        </head>
        <body>
            <h1>Falha ao conectar no banco de dados após várias tentativas 😢</h1>
        </body>
        </html>
        """, 500

    try:
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
    except Exception as e:
        return f"<h1>Erro ao executar a query: {e}</h1>", 500
    finally:
        conn.close()

 
    return f"""
    <html>
    <head>
        <title>Conexão Bem-Sucedida</title>
        <style>
            body {{
                background-image: url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?q=80&w=2020&auto=format&fit=crop');
                background-size: cover;
                background-position: center;
                color: #fff;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
                overflow: hidden;
                background-color: rgba(0, 0, 0, 0.5);
                background-blend-mode: darken;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 20px;
                animation: glow 1.5s infinite alternate;
            }}
            p {{
                font-size: 1.2em;
                margin-bottom: 30px;
            }}
            img {{
                width: 300px;
                height: auto;
                border-radius: 15px;
            }}
            @keyframes glow {{
                from {{ text-shadow: 0 0 10px #fff, 0 0 20px #0077cc, 0 0 30px #0055aa; }}
                to {{ text-shadow: 0 0 20px #fff, 0 0 30px #0077cc, 0 0 40px #0055aa; }}
            }}
        </style>
    </head>
    <body>
        <h1>Deu certo! Conexão com o Banco de Dados bem-sucedida! 🎉</h1>
        <p>Versão do PostgreSQL: {db_version[0]}</p>
        <img src="https://media.giphy.com/media/3o7TKsQG1yY6hBzXqk/giphy.gif" alt="Fogos de artifício">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
