import constant

def totalSeconds(hr, min, sec) -> int:
    print("hour is " + str(hr) + " Minute is [" + str(min) + "] Second is [" + str(sec) + "]")
    return hr*60 + min*60 + sec

def convertTime(seconds) -> str:
    min, sec = divmod(seconds, 60)
    hr, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hr, min, sec)

def convertDistance(metric, cvtType) -> float:
    if (cvtType not in constant.CVTDISTLIST):
        pass

    if (cvtType == constant.CVTKMTOMILE):
        return metric / constant.MILETOKM

    if (cvtType == constant.CVTMILETOKM):
        return metric * constant.MILETOKM

def right_justify(st:str, column_length:int = 70):
    return ((lambda s, l: ' ' * (l - len(s)) + s if (len(s) < l) else s)(st, column_length))



