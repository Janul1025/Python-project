# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830144

# Date: 30/04/2021


print('----------------------------------------------------------')
print('Staff Version with Histogram')
print()


##Range error
def range_error():
    print('Out of Range.')
    print('----------------------------------------------------------')


count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

choice = 'y'
while choice == 'y':
    try:
        # input of pass credit
        while True:
            pass_credit = int(input('Enter your total PASS credits:'))
            if pass_credit > 120 or (pass_credit % 20 != 0):
                range_error()
            else:
                break
        # input of defer credit
        while True:
            defer_credit = int(input('Enter your total DEFER credits:'))
            if defer_credit > 120 or (defer_credit % 20 != 0):
                range_error()
            else:
                break
        # input of fail credit
        while True:
            fail_credit = int(input('Enter your total FAIL credits:'))
            if fail_credit > 120 or (fail_credit % 20 != 0):
                range_error()
            else:
                break
        print()
        total = pass_credit + defer_credit + fail_credit
        if total == 120:
            ##progress
            if pass_credit == 120:
                count_1 = count_1 + 1
                print('Progress')
                print('----------------------------------------------------------')
            ##module trailer
            elif pass_credit == 100 and (defer_credit == 20 or fail_credit == 20):
                count_2 = count_2 + 1
                print('Progress (module trailer)')
                print('----------------------------------------------------------')
            ##module retrever
            elif 00 <= pass_credit <= 80 and 00 <= defer_credit <= 120 and 00 <= fail_credit <= 60:
                count_3 = count_3 + 1
                print('Do not Progress - module retriever')
                print('----------------------------------------------------------')
            ##exclude
            elif 00 <= pass_credit <= 40 and 00 <= defer_credit <= 40 and 80 <= fail_credit <= 120:
                count_4 = count_4 + 1
                print('Exclude')
                print('----------------------------------------------------------')
        ##Total Incorrect
        else:
            print('Total Incorrect')
            print('----------------------------------------------------------')
            # choice
        while True:    
            choice = str(input('''Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: '''))
            print('----------------------------------------------------------')
            if choice == 'y':
                break
            elif choice == 'q':
                total_counts = count_1 + count_2 + count_3 + count_4
                ###columns
                print(' \nProgress ' ' Trailer ' ' Retriever '' Exclude ' '\n')

                ###list
                countList = [count_1, count_2, count_3, count_4]

                ### m=maximum number in count list
                m = max(countList)

                ##Vertical Histogram
                for tot_count in range(0, m):
                    if count_1 > 0:
                        print("   *", end="")
                        count_1 = count_1 - 1
                    else:
                        print("    ", end="")
                    if count_2 > 0:
                        print("         *", end="")
                        count_2 = count_2 - 1
                    else:
                        print("          ", end="")
                    if count_3 > 0:
                        print("         *", end="")
                        count_3 = count_3 - 1
                    else:
                        print("          ", end="")
                    if count_4 > 0:
                        print("          *", end="")
                        count_4 = count_4 - 1
                    else:
                        print("            ", end="")
                    print()

                print('\n')
                print(total_counts, 'out comes in total')
                print('---------------------------------------------------------------')
                break
            else:
               print('Invalid Input')

    # Require Int
    except ValueError:
        print('Integer required')
        print('----------------------------------------------------------')



