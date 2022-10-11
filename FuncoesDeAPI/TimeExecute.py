import time

def StartTime():
    startTime = time.time()
    return startTime

def EndTime():
    endTime = time.time()
    return endTime

def MsgResultTime(endTime, startTime):
    resultTime = endTime - startTime
    return f'Time execute: {round(resultTime, 2)} seconds.'

