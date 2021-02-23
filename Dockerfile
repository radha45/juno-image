FROM python:3

# ADD org-test.py /
RUN pip3 install PyMySQL -t .
RUN pip install boto3

RUN pip install awscliv2
RUN git clone https://github.com/wolfcw/libfaketime.git
WORKDIR /libfaketime/src
RUN make install
RUN export LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1
WORKDIR /
RUN pip install -U click
RUN pip install --editable .
ENTRYPOINT ["juno"]
CMD [""]
WORKDIR /
ADD . /

# ARG AWS_ACCESS_KEY_ID
# ARG AWS_SECRET_ACCESS_KEY
# ARG AWS_REGION=us-west-1

# CMD [ "python", "./org-test.py" ]
