import time

def StartTime():
    startTime = time.time()
    return startTime

def EndTime():
    endTime = time.time()
    return endTime

def ResultTime(endTime, startTime):
    resultTime = endTime - startTime
    return round(resultTime, 2)