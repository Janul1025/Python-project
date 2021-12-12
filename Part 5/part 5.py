3 ## histogram
def histogram():
    print("\nProgress", count_1, " :", "*" * count_1)
    print("Trailer", count_2, "  :", "*" * count_2)
    print("Retriever", count_3, ":", "*" * count_3)
    print("Exclude", count_4, "  :", "*" * count_4)


count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

## list
pass_credit = [120, 100, 100, 80, 60, 40, 20, 20, 20, 0]
defer_credit = [0, 20, 0, 20, 40, 40, 40, 20, 0, 0]
fail_credit = [0, 0, 20, 20, 20, 40, 60, 80, 100, 120]

for i in range(0, 10):
    if pass_credit[i] == 120:
        count_1 = count_1 + 1
        print('Progress')
    elif pass_credit[i] == 100 and (defer_credit[i] == 20 or fail_credit[i] == 20):
        count_2 = count_2 + 1
        print('Progress (module trailer)')
    elif 0 <= pass_credit[i] <= 80 and 0 <= defer_credit[i] <= 120 and 0 <= fail_credit[i] <= 60:
        count_3 = count_3 + 1
        print('Do not Progress - module retriever')
    else:
        count_4 = count_4 + 1
        print('Exclude')

histogram()
total_counts = count_1 + count_2 + count_3 + count_4
print(total_counts, 'outcomes in total')
