# -*- coding: utf-8 -*-

import scratch

s = scratch.Scratch(host='192.168.11.20')
s.connect()

def listen():
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            s.disconnect()
            raise StopIteration
        except KeyboardInterrupt:
            print "Scratch: Disconnected from Scratch"
            s.disconnect()
            break

for msg in listen():
    if msg[0] == 'broadcast':
        # ブロードキャストを受け取った時の処理をこの下に書く
        print msg
    elif msg[0] == 'sensor-update':
        # センサーを受け取った時の処理をこの下に書く
        if 'send_msg' in msg[1]:
            val = msg[1]['send_msg']
            print 'send_msg:' + str(val)
