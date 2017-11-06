#!/usr/bin/env bash
# *************************************************************
#
# The OpenTRV project licenses this file to you
# under the Apache Licence, Version 2.0 (the "Licence");
# you may not use this file except in compliance
# with the Licence. You may obtain a copy of the Licence at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the Licence is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Licence for the
# specific language governing permissions and limitations
# under the Licence.
#
# *************************************************************
# Author(s) / Copyright (s): Andy Joiner 2017

function ensure-python3-installed {
    if ! [ -x "$(command -v python3)" ]; then
        sudo apt-get -y install python3
    fi
}

function ensure-pip3-installed {
    if ! [ -x "$(command -v pip3)" ]; then
        sudo apt-get -y install python3-pip
    fi
}

function ensure-python3-flask-installed {
	sudo apt-get -y install python3-flask
}

function ensure-flask-socketio-installed {
	sudo pip3 install flask-socketio
}

ensure-python3-installed
ensure-pip3-installed
sudo apt-get install python3-serial
# ??? ensure-python3-flask-installed
sudo pip3 install flask
ensure-flask-socketio-installed
