FROM debian:stretch

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=$PATH:/bin/:/usr/bin/

RUN apt-get update && apt-get install -y cmake \
    lua5.1 \
    libboost-thread1.62.0 \
    libboost-wave1.62.0 \
    liblua5.1-0 \
    libluabind-dev \
    liblua5.1-0-dev \
    tcl-dev \
    pandoc \
    tk-dev \
    python2.7-dev \
    python3.5 \
    python3.5-dev \
    python3-pip

# Download Vera++ 1.3.0 sources
ADD https://bitbucket.org/verateam/vera/downloads/vera++-1.3.0.tar.gz /tmp/vera++-1.3.0.tar.gz
RUN cd /tmp && tar zxvf vera++-1.3.0.tar.gz

# build and install 
RUN cd /tmp/vera++-1.3.0 && mkdir build && cd build && cmake .. && make -j8 && make install

#cleanup
RUN rm /tmp/vera++-1.3.0.tar.gz
RUN apt-get -y autoremove && apt-get -y autoclean