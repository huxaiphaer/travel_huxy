FROM python:3.7

RUN mkdir app

COPY . /app/

WORKDIR /app

RUN chmod +x wait-for-postgres.sh
RUN chmod +x entrypoint.sh


# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["bash", "entrypoint.sh"]
