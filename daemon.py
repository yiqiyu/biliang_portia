#-*- encoding:utf-8 -*-
#!/usr/bin/env python3

import os
from subprocess import Popen
import subprocess as sp
import logging
import time
import shlex

from websocket import create_connection, WebSocketApp

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s][%(filename)s][%(message)s]", filename="daemon.log", level=logging.DEBUG)

PWD = "123456"
CONFIG = {
  'HOST': '127.0.0.1',
  'PORT': 9001
}
SKT_ADDR = "ws://%s:%s/ws" % (CONFIG["HOST"], CONFIG["PORT"])



def watchover():
    os.chdir(os.getcwd())
    cmd = "export SUDO_ASKPASS=./pwd.sh && sudo -A ./activate.sh"
    p = Popen(cmd, shell=True)
    # p.wait(60)
    time.sleep(17)

    while 1:
        logger.info("start connection")
        while 1:
            # 保证socket持续运行
            before = time.time()
            ws = WebSocketApp(SKT_ADDR)
            ws.run_forever()
            end = time.time()
            if end-before<2:
                break

        logger.info("portia disconnected")
        print("portia disconnected")
        p.kill()
        os.popen("export SUDO_ASKPASS=./pwd.sh && sudo -A docker stop $(sudo -A docker ps)")
        time.sleep(10)
        p = Popen(cmd, shell=True)
        # p.wait(60)
        time.sleep(17)


if __name__ == '__main__':
    watchover()
    # print(os.getcwd())
    # os.chdir(os.getcwd())
    # cmd = "export SUDO_ASKPASS=./pwd.sh && sudo -A ./activate.sh"
    # e=os.popen(cmd)
    # for l in e:
    #   print(l)
    # time.sleep(30)

