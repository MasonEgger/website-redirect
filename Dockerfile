from python
WORKDIR /var/www/
ENV REDIRECT_TO https://mason.dev
COPY ./app.py /var/www/app.py
COPY ./requirements.txt /var/www/requirements.txt
COPY ./gunicorn_config.py /var/www/gunicorn_config.py
RUN pip install -r /var/www/requirements.txt

CMD gunicorn --config gunicorn_config.py app:app
