FROM python:3.8-slim
WORKDIR /home/scraper
RUN mkdir output src
COPY ./requirements.txt requirements.txt
COPY ./src ./src
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cron
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh