FROM debian:10
COPY init.sh .
RUN . ./init.sh
