FROM python:3.12

WORKDIR Smartix_test

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./Smartix_test ./Smartix_test
COPY ./Smartix_test/docker-entrypoint.sh ./Smartix_test
COPY ./manage.py .
COPY ./address ./address
COPY ./auth_jwt ./auth_jwt

CMD ["sh", "./Smartix_test/docker-entrypoint.sh"]