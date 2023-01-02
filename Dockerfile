FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/

#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":80", "tiket_project.wsgi:application"]