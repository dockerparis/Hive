
FROM debian:wheezy

MAINTAINER vhb <vctrhb@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Update and install minimal.
RUN apt-get update --quiet \
        && apt-get install \
            --yes \
            --no-install-recommends \
            --no-install-suggests \
            boinc-client \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Default command.
CMD ["--attach_project", "http://milkyway.cs.rpi.edu/milkyway/", "1030352_7eb410c3bc96876f7eb90192ded60f26"]

ENTRYPOINT ["/usr/bin/boinc"]
