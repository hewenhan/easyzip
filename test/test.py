#!/usr/bin/env python3

import easyzip, os, datetime

#9-306M
#4-311M
#1-324M
#0-307M

# easyzip.zip(".", "arc.zip", 9, "123456")

for i in range(10):
    startTime = datetime.datetime.now()
    easyzip.zip("/home/noone/.vscode", "code.zip", i, "123456")
    endTime = datetime.datetime.now()

    fileSize = os.path.getsize('code.zip')
    unit = 'B'
    if fileSize > 1024:
        fileSize = fileSize / 1024
        unit = 'KB'
    if fileSize > 1024:
        fileSize = fileSize / 1024
        unit = 'MB'
    if fileSize > 1024:
        fileSize = fileSize / 1024
        unit = 'GB'

    print(f'compress level: {i}, file size: {fileSize} {unit}, time: {(endTime - startTime).total_seconds()}')
    os.remove("code.zip")
