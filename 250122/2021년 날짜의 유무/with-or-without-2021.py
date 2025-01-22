M, D = map(int, input().split())

# Write your code here!
def is_valid_date(M, D):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if M < 1 or M > 12:
        return "No"

    if D < 1 or D > days_in_month.get(M, 0):
        return "No"

    return "Yes"


print(is_valid_date(M, D))
