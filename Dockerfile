FROM python:3.9

ADD *.py .

ENTRYPOINT ["python", "./main.py"]