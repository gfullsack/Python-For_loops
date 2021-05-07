#1 Basic - Print all integers from 0 to 150.
for i in range(0, 151, 1):
    print(i)
    # (coundup from 1 to 150 by 1)
    # note, end number not inclusive! 

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#for i in range(0,1000,5):
#    print(i)
    # (coundup from 1 to 1000 by 5)

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#for num in range(100):
#    if num % 5 == 0:
#        print("Coding")
#    if num % 10 == 0:
#        print("Coding Dojo")
#    else:
#        print(num)

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#final_sum = 0
#for x in range(0, 500000):
#    if x % 2:
#        # += this modifies final_sum and add to itself 
#        final_sum += x
#print(final_sum)


#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
#for x in range(2018,0,-4):
#    print(x)

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only
# the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# lowNum = 2
# highNum = 9
# mult = 3
# #as the range ends before highNum, we need to add 1 in order for the range to include 9 because the end of the range is NOT inclusive 
# for x in range(lowNum, highNum + 1, 1):
#     if not x % mult:
#         print(x)