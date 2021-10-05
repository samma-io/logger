from ubuntu



RUN apt-get update && apt-get install python3-pip -y
WORKDIR /opt




# Setup Run
RUN mkdir /code
RUN mkdir /output
RUN mkdir /out


WORKDIR /code
COPY code/ .

RUN chmod 555 -R /code
RUN useradd -ms /bin/bash samma

RUN chown samma:samma /out
RUN chown samma:samma /output
RUN chmod +x /code/run.sh


USER samma
WORKDIR /output 

CMD /code/run.sh


