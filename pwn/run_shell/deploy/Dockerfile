FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y xinetd netcat socat

RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386

RUN mkdir /home/pwn
RUN useradd -d /home/pwn pwn -s /bin/bash
RUN chown -R pwn:pwn /home/pwn/
RUN chown -R root:pwn /home/pwn
RUN chmod 750 /home/pwn

ADD ./run_shell /home/pwn/run_shell
RUN chmod +x /home/pwn/run_shell

ADD ./FLAG /home/pwn/FLAG
RUN chown root:pwn /home/pwn/FLAG
RUN chmod 440 /home/pwn/FLAG

ADD ./pwn /etc/xinetd/pwn
ADD ./start.sh /
RUN chmod +x /start.sh

WORKDIR /home/pwn
CMD ["/usr/sbin/xinetd","-dontfork"]