# First stage
FROM python:3.8

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR  /app
# Update PATH environment variable
#RUN echo "export PATH=/root/.local:$PATH" >> ~/.bashrc

# Install dependecies
RUN pip install -r requirements.txt

COPY . /app

# Run pytests
RUN pytest --maxfail=1 --exitfirst tests

EXPOSE 3000

ENTRYPOINT ['python3']

CMD ['application.py']