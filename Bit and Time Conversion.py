# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).


# print(2 ** 10)     # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

# print(2 ** 20)      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

# print(2 ** 30)     # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

# print(2 ** 40)     # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def convert_bits(size, unit):
    if unit == 'kb':
        size /= 1024
    elif unit == 'Gb':
        size *= 1024
    elif unit == 'Tb':
        size *= (1.024 ** 6)
    elif unit == 'kB':
        size /= (1024 / 8)
    elif unit == 'GB':
        size *= (1024 * 8)
    elif unit == 'TB':
        size *= ((1.024 ** 6) * 8)
    elif unit == 'MB':
        size *= 8
    return size

# print(convert_bits(1024,'kB'))
# print(convert_bits(13,'GB'))
# print(convert_bits(5.6,'MB'))
# print(convert_bits(5.6,'Mb'))
# print(convert_bits(10,'MB'))
# print(convert_bits(2,'kB'))
# print(convert_bits(2,'kb'))



def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    speed_of_download = convert_bits(file_size, file_unit) / convert_bits(bandwidth, bandwidth_unit)
    return speed_of_download










def is_plural_hour(number):
        if number == 1:
            return 'hour'
        return 'hours'


def is_plural_minute(number):
    if number == 1:
        return 'minute'
    return 'minutes'


def is_plural_second(number):
    if number == 1:
        return 'second'
    return 'seconds'


def convert_seconds(number):
    if number % 3600 != 0:
        hour = int(number / 3600)
        hour_plural = is_plural_hour(hour)
        if ((number % 3600) % 60) != 0:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            if isinstance(number, float):
                second = round(((number % 3600) % 60), 1)
            else:
                second = int(((number % 3600) % 60))
            second_plural = is_plural_second(second)
            return f'{hour} {hour_plural}, {minute} {minute_plural}, {second} {second_plural}'

        else:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            return f'{hour} {hour_plural}, {minute} {minute_plural}'
    hour = int(number / 3600)
    hour_plural = is_plural_hour(hour)
    return f'{hour} {hour_plural}'

number = download_time(1024,'kB', 1, 'MB')
# print(f'{number} seconds')
print(convert_seconds(number))

# print(download_time(1024,'kB', 1, 'MB'))
# #>>> 0 hours, 0 minutes, 1 second


number = download_time(1024,'kB', 1, 'Mb')
# print(convert_bits(1024,'kB'))
# print(convert_bits(1, 'Mb'))
# print(f'{number} seconds')
print(convert_seconds(number))

# print(download_time(1024,'kB', 1, 'Mb'))
# #>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable
#
# #
number = download_time(13,'GB', 5.6, 'MB')
# print(convert_bits(13,'GB'))
# print(convert_bits(5, 'MB'))
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(13,'GB', 5.6, 'MB'))
# # #>>> 0 hours, 39 minutes, 37.1428571429 seconds
#
#
number = download_time(13,'GB', 5.6, 'Mb')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(13,'GB', 5.6, 'Mb'))
# # #>>> 5 hours, 16 minutes, 57.1428571429 seconds
#
#
number = download_time(10,'MB', 2, 'kB')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(10,'MB', 2, 'kB'))
# # #>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable
#
#
number = download_time(10,'MB', 2, 'kb')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(10,'MB', 2, 'kb'))
# #>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
#

