# -*- coding: utf-8 -*-

import scratch, time

#192.168.11.20のScratchへ送る場合
s = scratch.Scratch(host='192.168.11.20')
#同一PCのScratchへ送る場合
#s = scratch.Scratch(host='localhost')

s.connect()

a = 0

while True:
    try:
        a = a + 1
        # センサーの値を送る
        s.sensorupdate({'a' : a})
        time.sleep(0.5)
    except KeyboardInterrupt:
        print "Scratch: Disconnected from Scratch"
        break

s.disconnect()

