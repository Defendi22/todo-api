# Imagem base — Python 3.11 leve (alpine = versão minimalista)
FROM python:3.11-slim

# Define a pasta de trabalho dentro do contêiner
WORKDIR /app

# Copia o requirements.txt PRIMEIRO (truque de performance)
# Docker faz cache dessa camada — se as deps não mudaram, não reinstala
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# Expõe a porta 8000 (documenta que a app usa essa porta)
EXPOSE 8000

# Comando que roda quando o contêiner iniciar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]