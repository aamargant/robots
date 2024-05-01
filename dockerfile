FROM python:3.12 

ENV PYTHONUNBUFFERED 1  

WORKDIR /robots
COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000  

ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]