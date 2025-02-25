FROM alpine:latest

WORKDIR /app 

COPY . .

CMD ["echo" ,"hello world"]

RUN apk add curl
RUN apk add bash
