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

import threading

import serial #package: pyserial


class SerialComms:

    def __init__(self, router, port):
        self.router = router
        self.port = port
        self.ser = serial.Serial(
            port=port,
            baudrate=4800,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )

        router.register_comms(self)
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def close(self):
        self.ser.close()

    def router_to_board(self, data):
        self.ser.write(bytes(data+"\n", 'utf-8'))
        self.router.router_to_browser_echo(data)

    def on_rx_from_board(self, data):
        self.router.router_to_browser(data)

    def simulator_main(self, a,b):
        while True:
            rx = self.ser.readline()
            if(len(rx) > 0):
                rx = str(rx)
                print("raw:"+rx)
                if(rx[:2] == "b'"):
                    rx = rx[2:]
                if(rx[-5:] == "\\r\\n'"):
                    rx = rx[:-5]
                print(rx)
                self.on_rx_from_board(rx)
