# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        outputIntervals = []
        newRangeAfterMerge = []
        newIntervalStart = newInterval[0]
        newIntervalEnd = newInterval[1]
        for interval in intervals:
            intStart = interval[0]
            intEnd = interval[1]
            #Falls in the new interval
            if(newIntervalStart < intStart and newIntervalEnd > intEnd):
                continue
            elif(intEnd < newIntervalStart):
                outputIntervals.append(interval)
            elif(intStart > newIntervalEnd):
                if(len(newRangeAfterMerge) == 2):
                    outputIntervals.append(newRangeAfterMerge)
                    newRangeAfterMerge = []
                outputIntervals.append(interval)
            #Logic for merging
            else:
                if(intStart < newIntervalStart < intEnd):
                    if(len(newRangeAfterMerge) == 0):
                        newRangeAfterMerge.append(intStart)
                        if(intEnd > newIntervalEnd):
                            newRangeAfterMerge.append(intEnd)
                        else:
                            newRangeAfterMerge.append(newIntervalEnd)
                    else:
                        newRangeAfterMerge[0] = intStart
                elif (intStart < newIntervalEnd < intEnd):
                    if(len(newRangeAfterMerge) == 0):
                        if(intStart < newIntervalStart):
                            newRangeAfterMerge.append(intStart)
                        else:
                            newRangeAfterMerge.append(newIntervalStart)
                        newRangeAfterMerge.append(intEnd)
                    else:
                        newRangeAfterMerge[1] = intEnd
        if(len(outputIntervals) == 0):
            outputIntervals.append(newInterval)
        if(len(newRangeAfterMerge) == 2):
            outputIntervals.append(newRangeAfterMerge)
        return outputIntervals

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,9]
Solution().insert(intervals, newInterval)