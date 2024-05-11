FROM python:3.10-alpine
WORKDIR /app
EXPOSE 5050
COPY . .
RUN pip install -r requirements.txt