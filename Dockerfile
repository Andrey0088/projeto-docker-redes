# 1. Usar uma imagem base do Python
FROM python:3.9-slim

# 2. Instalar o Git dentro da imagem
RUN apt-get update && apt-get install -y git

# 3. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 4. Clona o conteúdo do seu repositório para o diretório de trabalho atual (/app)
#    O ponto "." no final é crucial para clonar na pasta /app e não numa subpasta.
RUN git clone https://github.com/Andrey0088/projeto-docker-redes.git .

# 5. Instala as dependências da aplicação usando o requirements.txt que foi clonado
RUN pip install --no-cache-dir -r requirements.txt

# 6. Expõe a porta que a aplicação vai rodar
EXPOSE 5000

# 7. Comando para iniciar a aplicação
CMD ["python", "app.py"]
