import constant
import misc
import math

if __name__ == '__main__':
    print("Think Python 3: Exercise 1")

    m = 42
    s = 42
    k = 10

    ts = misc.totalSeconds(0, m, s)
    print("Number of seconds in 42 minutes and 42 seconds are " + str(ts))

    totalMiles = misc.convertDistance(k, constant.CVTKMTOMILE)
    print("Number of miles in 10 Kms are " + str(totalMiles))

    avgPaceInSeconds = math.ceil(ts/totalMiles)
    print("Avg Pace (Time per mile in minutes and seconds) " + misc.convertTime(avgPaceInSeconds))

    avgSpeedInMilesPerHour = (totalMiles * 3600)/ts
    print("Avg Speed(Miles per hour) " + str(avgSpeedInMilesPerHour))