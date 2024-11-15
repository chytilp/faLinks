FROM python:3.11

COPY . .

RUN pip install poetry

# install runtime deps
RUN poetry install --no-dev --no-root

EXPOSE 8080

ENTRYPOINT [ "poetry" , "run", "app" ]
