# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

def move_zeros(a_list):
    zeros = []
    while 0 in a_list:
        a_list.remove(0)     #I would think this one is probably the fastest as its a single loop
        zeros.append(0)
    return a_list + zeros


def move_zeros2(a_list):
    return list(filter(lambda num: True if num != 0 else False, a_list))\
        + list(filter(lambda num: True if num == 0 else False, a_list))  # This one is a cleaner version of the first


def move_zeros3(a_list):
    return list(filter(lambda num: True if num != 0 and num != '0' and num != 'zero' and num != 0.0 else False, a_list))\
        + list(filter(lambda num: True if num == 0 or num == '0' or num == 'zero' or num == 0.0 else False, a_list))      #This one catches ALL zeros 

        #Floats don't matter in the test, but they matter to me
        #Those decimal point dingos get chucked to the back of the line all the same

print(move_zeros3([1,2,0.0,3,0,4]))

         







