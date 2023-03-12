FROM jenkins/jenkins:latest
USER root
RUN apt-get update && \
	apt-get -y install python3 && \
	apt-get -y install python3-pip && \
	echo "installed" && \
	pip3 install --no-cache-dir selenium && \
	echo $(pip3 list)