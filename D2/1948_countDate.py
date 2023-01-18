# Accepts two dates consist with month and day, and prints the number of days between the second and the first.

calender = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

T = int(input())

for test_case in range(1, T+1):
    all_date = list(map(int, input().split()))

    first_month = all_date[0]
    first_date = all_date[1]
    end_month = all_date[2]
    end_date = all_date[3]
    
    answer = 0

    if first_month == end_month:
        answer = end_date - first_date + 1
    elif first_month != end_month:
        # Get first months remain date add to answer(in that month only)
        answer += calender.get(first_month) - first_date + 1
        # Get end Months remain date and add to answer(in that month only)
        answer += end_date
        # Get date in betweeen and add to answer
        for month in range(first_month+1, end_month):
            answer += calender.get(month)
    
    print(f'#{test_case} {answer}')