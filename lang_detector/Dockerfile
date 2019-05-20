FROM python:3.6

# add code
COPY . /src

# install app requirements
RUN pip3 install -r ./src/requirements.txt

# add the start script
COPY ./start.sh /

# execute start script
CMD ["./start.sh"]