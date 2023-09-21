# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
speed_of_light = 299792458   #meters per second
centimeters = 100            #one meter is 100 centimeters
nanosecond = 1.0/1000000000  #one billionth of a second


def LightTravelperNanosecond():
    answer = speed_of_light*centimeters*nanosecond
    return answer


print(LightTravelperNanosecond())


# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0

answer = speed_of_light/cycles_per_second

print(answer)


