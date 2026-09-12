# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 1 : Assign Cookies
def AssignCookies(greed,cookies):
    greed.sort()
    cookies.sort()
    greedIndex = 0
    cookiesIndex = 0
    while cookiesIndex < len(cookies) and greedIndex < len(greed) :
        if cookies[cookiesIndex] >= greed[greedIndex]:
            greedIndex += 1
        cookiesIndex += 1
    return greedIndex
# print(AssignCookies([1,5,3,3,4],[4,2,1,2,1,3]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 2 : Fractional Knapsack
class Item:
    def __init__(self,value,weight):
        value = self.value
        weight = self.weight

def FractionalKnapsack(inArrItems,Weight):
    inArrItems.sort(key = lambda x:(x.value/x.wight),reverse = True)
    currWeight = 0
    totalValue = 0.0
    for i in range(len(inArrItems)):
        if currWeight+inArrItems[i].weight <= Weight:
            currWeight += inArrItems[i].weight
            totalValue += inArrItems[i].value
        else:
            totalValue += (inArrItems[i]/inArrItems[i])*(Weight-currWeight)
            break
    return totalValue


import sys
# ==========================================
# PART 1: CORE FRACTIONAL KNAPSACK LOGIC
# ==========================================
class FractionalKnapsackSolver:
    @staticmethod
    def solve(capacity: float, items: list[tuple[float, float]]) -> float:
        """
        Calculates maximum total value attainable in a knapsack.
        
        :param capacity: Maximum weight knapsack can hold (W)
        :param items: List of tuples -> [(value, weight), (value, weight), ...]
        :return: Maximum possible value (float)
        
        DSA Pattern: Greedy (Value-to-Weight Ratio Sorting)
        Time Complexity: O(N log N)
        Space Complexity: O(1) auxiliary space (modifying sorted reference)
        """
        # Step 1: Sort items in descending order of Value/Weight ratio
        # item[0] = value, item[1] = weight
        items.sort(key=lambda item: item[0] / item[1], reverse=True)
        
        total_value = 0.0
        current_capacity = capacity
        
        # Step 2: Greedily process items
        for val, wt in items:
            if current_capacity == 0:
                break
                
            if wt <= current_capacity:
                # Take 100% of the item
                total_value += val
                current_capacity -= wt
            else:
                # Take a fraction of the item to fill remaining capacity
                total_value += (val / wt) * current_capacity
                current_capacity = 0 # Bag is now full
                break
                
        return total_value
# ==========================================
# PART 2: INFOSYS / OA INPUT-OUTPUT LOGIC
# ==========================================
def main():
    """
    Handles standard input parsing and exact output formatting.
    """
    # Fast standard input reading (handles newlines, spaces, tabs cleanly)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 1. Parse Metadata (N = number of items, W = total capacity)
    N = int(input_data[0])
    W = float(input_data[1])
    
    # 2. Parse Item pairs into clean Python tuples
    items = []
    cursor = 2
    for _ in range(N):
        val = float(input_data[cursor])
        wt = float(input_data[cursor + 1])
        items.append((val, wt))
        cursor += 2
        
    # 3. Call Core DSA Logic (Part 1)
    max_value = FractionalKnapsackSolver.solve(capacity=W, items=items)
    
    # 4. Print formatted output as required by OA platform
    # Infosys usually expects 6 or 2 decimal places precision
    print(f"{max_value:.6f}")


# if __name__ == "__main__":
    # main()

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 3 : Lemonade Change
def LemonadeChange(bills):
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        else:
            if fives > 0 and tens > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
# print(LemonadeChange([5, 5, 5, 10, 20]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 4 : Valid Paranthesis Checker
# Recursive approach :
def ValidParanthesisChecker(s,index,count):
    if count < 0 :
        return False 
    if index == len(s) :
        return count == 0
    if s[index] == '(':
        return ValidParanthesisChecker(s,index+1,count+1)
    if s[index] == ')':
        return ValidParanthesisChecker(s,index+1,count-1)
    return ValidParanthesisChecker(s,index+1,count+1) or ValidParanthesisChecker(s,index+1,count-1) or ValidParanthesisChecker(s,index+1,count)
# print(ValidParanthesisChecker('*(()',0,0))

# Greedy approach:
def ValidParanthesisCheckerI(s):
    min = 0
    max = 0
    for i in s:
        if i == '(':
            min += 1
            max += 1
        elif i == ')':
            min -= 1
            max -= 1
        else :
            min -= 1
            max += 1
        if min < 0 :
            min = 0
        if max < 0 :
            return False
    return min == 0
print(ValidParanthesisCheckerI('*(()'))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------