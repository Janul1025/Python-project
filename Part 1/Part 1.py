# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830144

# Date: 30/04/2021


#inputs
print('--------------------------------------------------------')
pass_credit=int(input("Please enter your credits at pass:"))
defer_credit=int(input("Please enter your credit at defer:"))
fail_credit=int(input("Please enter your credits at fail:"))
print('--------------------------------------------------------')

###progress
if pass_credit==120:
    print("Progress")
    print('--------------------------------------------------------')
###module trailer    
elif pass_credit==100 and (defer_credit==20 or fail_credit==20):
    print('Progress(module trailer)')
    print('--------------------------------------------------------')
          
###module retriver
          
elif 0<=pass_credit<=80 and 0<=defer_credit<=120 and 0<=fail_credit<=60:
    print('Do not Progress - module retriever')
    print('--------------------------------------------------------')

###exclude

elif 0<=pass_credit<=40 and 0<=defer_credit<=40 and 0<=fail_credit<=120:
    print('Exclude')
    print('-------------------------------------------------------')

















