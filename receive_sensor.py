# -*- coding: utf-8 -*-

import scratch

#192.168.11.20のScratchから受け取る場合
s = scratch.Scratch(host='192.168.11.20')
s.connect()

while True:
    try:
        msg = s.receive()
        print "Scratch: receive:",msg
        # Scratchでの変数名send_msgの値があれば表示
        if 'send_msg' in msg[1]:
            val = msg[1]['send_msg']
            print val
    except KeyboardInterrupt:
        print "Scratch: Disconnected from Scratch"
        break

s.disconnect()
