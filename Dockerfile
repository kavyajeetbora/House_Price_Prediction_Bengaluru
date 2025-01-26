FROM python:3.9-slim

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

COPY ./app /project/app

EXPOSE 7751
CMD ["fastapi", "run", "app/main.py", "--port", "7751"]