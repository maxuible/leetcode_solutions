# You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

# date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

# Return the binary representation of date.

 

# Example 1:

# Input: date = "2080-02-29"

# Output: "100000100000-10-11101"

# Explanation:

# 100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

# Example 2:

# Input: date = "1900-01-01"

# Output: "11101101100-1-1"

# Explanation:

# 11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

def convertDateToBinary(date: str) -> str:

    year = str(bin(int(date[0:4])))[2:]
    month = str(bin(int(date[5:7])))[2:]
    binday = str(bin(int(date[8:])))[2:]

    # print(year + '-' + month + '-' + binday)

    return year + '-' + month + '-' + binday


print(convertDateToBinary("2080-02-29"))