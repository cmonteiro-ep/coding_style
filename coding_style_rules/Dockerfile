FROM epitechcontent/epitest-docker

WORKDIR /tmp

COPY 'dnf.requirements.txt' 'dnf.requirements.txt'
RUN dnf -y install $(cat 'dnf.requirements.txt') \
    && dnf clean all -y \
    && rm -f 'dnf.requirements.txt'

RUN wget https://github.com/Epitech/banana-vera/archive/refs/heads/master.zip \
    && unzip master.zip \
    && cd 'banana-vera-master' \
    && cmake . -DVERA_LUA=OFF -DPANDOC=OFF \
    && cmake --build . \
    && make -j \
    && make install \
    && cd .. \
    && rm -rf 'banana-vera-master' 'master.zip'

COPY 'pip3.requirements.txt' 'pip3.requirements.txt'
RUN pip3 install -r 'pip3.requirements.txt' \
    && pip3 cache purge \
    && rm -f 'pip3.requirements.txt'

ENTRYPOINT /bin/sh
