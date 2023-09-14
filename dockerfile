# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /news_website

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# copy entrypoint.sh \
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /news_website/entrypoint.sh
RUN chmod +x /news_website/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/news_website/entrypoint.sh"]