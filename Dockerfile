# Usar uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências primeiro
# Isso aproveita o cache do Docker. Se o arquivo não mudar, essa camada não é reconstruída.
COPY requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código da sua aplicação para o diretório de trabalho
COPY . .

# Expõe a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
# Assumindo que seu arquivo python se chama app.py
CMD ["python", "app.py"]