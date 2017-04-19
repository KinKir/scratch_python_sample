# -*- coding: utf-8 -*-

import scratch

#192.168.11.20のScratchから受け取る場合
s = scratch.Scratch(host='192.168.11.20')

s.connect()

while True:
    try:
        msg = s.receive()
        print "Scratch: receive:",msg
        if msg[0] == 'broadcast':
            print msg[1]
    except KeyboardInterrupt:
        print "Scratch: Disconnected from Scratch"
        break

s.disconnect()
