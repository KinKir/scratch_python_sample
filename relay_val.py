# -*- coding: utf-8 -*-

import scratch

# scratch1のIPアドレス
s = scratch.Scratch(host='192.168.11.20')
s.connect()

# scratch2のIPアドレス
s2 = scratch.Scratch(host='localhost')
s2.connect()

def listen():
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            s.disconnect()
            s2.disconnect()
            raise StopIteration
        except KeyboardInterrupt:
            print "Scratch: Disconnected from Scratch"
            s.disconnect()
            s2.disconnect()
            break

for msg in listen():
    if msg[0] == 'broadcast':
        # デバッグ用
        print msg
    elif msg[0] == 'sensor-update':
        if 'send_msg' in msg[1]:
            val = msg[1]['send_msg']
            # デバッグ用
            print 'send_msg:' + str(val)
            # Scratch1から受け取ったsliderの値を、Scratch2へ送る
            s2.sensorupdate({'from_scratch1' : val})
