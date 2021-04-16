FROM python:3

ENV NODE_ENV=production

WORKDIR /app
COPY . .

RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "./server.py"]
