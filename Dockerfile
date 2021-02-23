FROM docker-juno-cli:tag

# ADD org-test.py /
RUN pip3 install PyMySQL -t .
ENTRYPOINT ["juno"]
CMD [""]
WORKDIR /
ADD . /

# ARG AWS_ACCESS_KEY_ID
# ARG AWS_SECRET_ACCESS_KEY
# ARG AWS_REGION=us-west-1

# CMD [ "python", "./org-test.py" ]
