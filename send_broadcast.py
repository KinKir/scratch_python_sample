# -*- coding: utf-8 -*-

import scratch

#192.168.11.20のScratchへ送る場合
s = scratch.Scratch(host='192.168.11.20')
s.connect()

# Hello, Scratch!を送る
s.broadcast('Hello, Scratch!')

# 切断
s.disconnect()
