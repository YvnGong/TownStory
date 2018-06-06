# Derivatived work based on open source docker file
# The orginal License is attachd at the end

# The modified code covered by the below License.
# Copyright 2018 Yicong Gong
# All rights reserved, for demostration purpose only.

FROM ubuntu:16.04

# Install prerequisite to set up the basic environment

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	nginx \
	supervisor \
	sqlite3 \
	python3 \
	python3-dev \
	python3-pip \
	python3-setuptools &&\
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# Install uwsgi
RUN pip3 install uwsgi

# Copy the nginx and supervisor config files
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisor.conf /etc/supervisor/conf.d/

# ----------------------------------------------------
# Frequently changing portion placeed below this point.
# ----------------------------------------------------

# Install required python packages
COPY app/requirements.txt /home/app/
RUN pip3 install -r /home/app/requirements.txt

# Copy all source code into home/
COPY . /home/

# Set workdir
WORKDIR /home/app/

# Make migrations & Migrates
RUN python3 manage.py makemigrations && python3 manage.py migrate --run-syncd

EXPOSE 80
CMD ["supervisord", "-n"]


# -----------------------------------------------
# Derivatived work based on the following author. 
# The orginal License is attachd below

# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

