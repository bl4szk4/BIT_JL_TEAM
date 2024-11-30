FROM postgis/postgis:15-3.3-alpine

RUN apk add --no-cache git make gcc g++ clang15 llvm15

RUN git clone --branch v0.7.2 https://github.com/pgvector/pgvector.git /tmp/pgvector

WORKDIR /tmp/pgvector
RUN make && make install

# Clean up
RUN rm -rf /tmp/pgvector && apk del llvm15 clang15 g++ gcc make git

WORKDIR /