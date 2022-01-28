FROM python:3.9

RUN pip3 install --upgrade pip setuptools

COPY . .

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN python setup.py install

EXPOSE 8000

# when the container is started
ENTRYPOINT ["gunicorn", "wsgi:app"]
# This makes it possible to specify this flag differently on the command line
CMD ["-b", "0.0.0.0:8000", "-w", "2"]