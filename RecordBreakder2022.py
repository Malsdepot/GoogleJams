def processCase(case_num):
    recordBreakingDays = 0
    previousRecord = 0
    numDays = int(input())
    visitors = list(map(int, input().split()))
    for day in range(numDays):
        greaterThenPreviousDays = day==0 or visitors[day]>previousRecord
        if day==len(visitors)-1:
            greaterThenNextDay=True
        else:
            greaterThenNextDay = visitors[day] > visitors[day+1]
        if (greaterThenPreviousDays and greaterThenNextDay):
            recordBreakingDays+=1
        previousRecord = max(previousRecord, visitors[day])

    print(f"Case #{case_num}: {recordBreakingDays}")
 
num_cases = int(input())
for i in range(num_cases):
    processCase(i+1)
