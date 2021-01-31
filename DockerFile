FROM python:3.9-slim

USER root

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade name-that-hash && \
    groupadd -r nonroot && \
    useradd -m -r -g nonroot -d /home/nonroot -s /usr/sbin/nologin -c "Nonroot User" nonroot && \
    mkdir -p /home/nonroot/workdir && \
    chown -R nonroot:nonroot /home/nonroot

USER nonroot
ENV HOME /home/nonroot
WORKDIR /home/nonroot/workdir
VOLUME ["/home/nonroot/workdir"]
ENV USER nonroot
ENTRYPOINT ["/usr/local/bin/nth"]
