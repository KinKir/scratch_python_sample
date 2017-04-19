# -*- coding: utf-8 -*-

import scratch
import subprocess

# ScratchのIPアドレス
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
        # デバッグ用
        print msg
    elif msg[0] == 'sensor-update':
        if 'shell' in msg[1]:
            val = msg[1]['shell']
            cmd = str(val)

            # デバッグ用
            print 'shell:' + str(val)

            # shellコマンドの実行
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_data, stderr_data = p.communicate()
            # 標準、エラー出力をScratchに送り返す
            s.sensorupdate({'shell_stdout' : stdout_data.replace('\r\n',' ')})
            s.sensorupdate({'shell_stderr' : stderr_data.replace('\r\n',' ')})

            # デバッグ用
            print 'stdout:' + str(stdout_data) + 'stderr:' + str(stderr_data)
