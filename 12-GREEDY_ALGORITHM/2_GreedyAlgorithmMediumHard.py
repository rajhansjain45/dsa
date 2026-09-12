# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 1 : N meetings in one room
def NMeetingsOneRoom(start,end):
    meetings = [(end[i],start[i],i+1) for i in range(len(start))]
    meetings.sort()
    freeTime = -1
    opArr = []
    count = 0
    for e,s,p in meetings:
        if s > freeTime:
            count += 1
            opArr.append(p)
            freeTime = e
    return count,opArr
# print(NMeetingsOneRoom([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 2 : Jump Game - I
def JumpGameI(inArr):
    maxIndex = 0
    for i in range(len(inArr)):
        if i > maxIndex:
            return False
        maxIndex = max(maxIndex,i+inArr[i])
    return True
# print(JumpGameI([2, 3, 1, 0, 4]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 3 : Jump Game - II
# Brute force :
def JumpGameII(inArr):
    def MinJumps(index):
        if index>=len(inArr)-1:
            return 0
        if inArr[index] == 0:
            return float('inf')
        minSteps = float('inf')
        for i in range(1,inArr[index]+1):
            result = MinJumps(index+i)
            if result != float('inf'):
                minSteps = min(minSteps,result+1)
        return minSteps
    return MinJumps(0)
# print(JumpGameII([2, 3, 1, 0, 4]))

# Optimal approach :
def JumpGameIIOptimal(inArr):
    if len(inArr)<=0:
        return 0
    jumps = 0
    far = 0
    near = 0
    while far<len(inArr)-1:
        farthest = 0
        for i in range(near,far+1):
            farthest = max(farthest,i+inArr[i])
        near = far+1
        far = farthest
        jumps += 1
    return jumps
# print(JumpGameIIOptimal([2, 3, 1, 0, 4]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 4 : Minimum number of platforms required for a railway
# Brute  force :
def MinimumPlatformsRequiredForRailway(arival,departure):
    platforms = 0
    for i in range(len(arival)):
        count = 1
        for j in range(i+1,len(arival)):
            if (arival[i]>=arival[j] and arival[i]<=departure[j] or \
                arival[j]>=arival[i] and arival[j]<=departure[i]):
                count += 1
        platforms = max(platforms,count)
    return platforms
# print(MinimumPlatformsRequiredForRailway([900, 945, 955, 1100, 1500, 1800],[920, 1200, 1130, 1150, 1900, 2000]))

# Optimal approach :
def MinimumPlatformsRequiredForRailwayOptimal(arival,departure):
    arival.sort()
    departure.sort()
    platforms = 0
    count = 0
    arive = 0
    depart = 0
    while arive<len(arival):
        if arival[arive] <= departure[depart]:
            count += 1
            arive += 1
        else:
            count -= 1
            depart += 1
        platforms = max(platforms,count)
    return platforms
# print(MinimumPlatformsRequiredForRailwayOptimal([900, 945, 955, 1100, 1500, 1800],[920, 1200, 1130, 1150, 1900, 2000]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 5 : Job sequencing Problem
class Jobs:
    def __init__(self,id,deadline,profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def JobsequencingProblem(inArr):
    inArr.sort(key=lambda x:x.profit,reverse=True)
    # find max deadline
    maxd = inArr[0].deadline
    for i in range(1,len(inArr)):
        maxd = max(maxd,inArr[i].deadline)
    # job slots
    Slots = [-1]*(maxd+1)
    jobs = 0
    MaxProfit = 0
    for i in range(len(inArr)):
        for j in range(inArr[i].deadline,0,-1):
            if Slots[j] == -1:
                Slots[j] = i
                jobs += 1
                MaxProfit += inArr[i].profit
                break
    return jobs , MaxProfit
# print(JobsequencingProblem([Jobs(1, 4, 20), Jobs(2, 1, 10), Jobs(3, 2, 40), Jobs(4, 2, 30)]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 6 : Candy
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 7 : Shortest Job First
def ShortestJobFirst(inArr):
    inArr.sort()
    time = 0
    waitingTime = 0
    for i in inArr:
        waitingTime += time
        time += i
    return waitingTime/len(inArr)
# print(ShortestJobFirst([4,3,7,1,2]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 8 : Program for Least Recently Used (LRU) Page Replacement Algorithm
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 9 : Insert Interval
def InsertInterval(inArr,newInterval):
    opArr = []
    i = 0
    n = len(inArr)
    # non-overlapping intervals
    while i < n and inArr[i][1] < newInterval[0]:
        opArr.append(inArr[i])
        i += 1
    # overlapping intervals
    while i < n and inArr[i][0] <= newInterval[1]:
        newInterval[0] = min(inArr[i][0],newInterval[0])
        newInterval[1] = max(inArr[i][1],newInterval[1])
        i += 1
    opArr.append(newInterval)
    # remaining intervals
    while i < n:
        opArr.append(inArr[i])
        i += 1
    return opArr
# print(InsertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 10 : Merge Intervals
# Brute force :
def MergeIntervals(inArr):
    n = len(inArr)
    opArr = []
    i = 0
    while i < n:
        start = inArr[i][0]
        end = inArr[i][1]
        j = i+1
        while j < n and inArr[j][0] <= end: 
            end = max(end,inArr[j][1])
            j += 1
        opArr.append([start,end])
        i = j
    return opArr
print(MergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

# Optimal approach :
def MergeIntervalsOptimal(inArr):
    n = len(inArr)
    opArr = []
    inArr.sort

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 11 : Non-overlapping Intervals
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# https://edgemobileapp.microsoft.com/share/?rh=131215B9&adjustId=1y5a1rux_1yprs5lb&sid=refc