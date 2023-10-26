# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.






def jungle_animal(animal, my_speed):
    if "cheetah" == animal:
        if my_speed <= 115:
            return "Stay calm and wait!"
        else:
            return "Run!"
    elif 'zebra' == animal:
        return "Try to ride a zebra!"
    else:
        return "Introduce yourself!"

## test cases

def test():
    test_cases = [(('cheetah',30),"Stay calm and wait!"),
                  (('gorilla',21),"Introduce yourself!"),
                  (('zebra', 55),"Try to ride a zebra!"),
                  (('cheetah', 175), "Run!")]
    for (args, answer) in test_cases:
        result = jungle_animal(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print('Test case passed!')

test()


