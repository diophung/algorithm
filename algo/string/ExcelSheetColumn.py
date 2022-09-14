# LeetCode #168 : Excel Sheet Column title and vice versa
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# For e.g:
#    1 -> A
#    2 -> B
#    3 -> C
#    ...
#    26 -> Z
#    27 -> AA
#    28 -> AB
#
# Then given a string [A-Z], convert it to the numerical column index
# For e.g:
# A -> 1
# AA -> 27
# AB -> 28
import math


def num_to_title(column_idx):
    """
    Convert the index of an Excel column to the string format

    Args :
        column_idx: the index of the column
    Returns:
        String format of the column index. For e.g: 1=>"A", 27 => "AA"
    """
    # To convert from X (base N) to Y (base M):
    # while X > 0:
    #   result = X mod M + result
    #   X = X / M
    result = ""
    while column_idx > 0:
        column_idx -= 1
        # Note: append the character to the front of output
        # chr(x) returns string based on a number
        result = chr(column_idx % 26 + 65) + result
        # reduce by the base (26 chars)
        column_idx = int(column_idx / 26)
    return result


def title_to_num(title):
    """
    Convert title to the column index

    Args :
        title: the title of the column in Excel (A, B, AA)
    Returns:
        the index of the column in integer format
    """
    num = 0
    length = len(title)
    power = length - 1
    if length == 1:
        # ord(char) return the integer format of it
        # Note: +1 since Excel is not 0-based
        return ord(title[0]) - ord('A') + 1
    
    # look at each character, from left to right
    for i in range(length):
    
        # ord(char) return integer value of this char
        mul = ord(title[i]) - ord('A') + 1
        num += mul * math.pow(26, power)
        power -= 1
    return int(num)


"""
sol = ExcelSheetColumn()
print('1->' + str(sol.convert_to_title(1)))  # 1 = 26*0 + 1 = A
print('26->' + str(sol.convert_to_title(26)))  # 26 = 26*0 + 26 = Z
print('27->' + str(sol.convert_to_title(27)))  # 27 = 26*1 + 1 = AA
print('52->' + str(sol.convert_to_title(52)))  # 52 = 26*1 + 26 = AZ
print('700->' + str(sol.convert_to_title(700)))  # 700 = 26*26 + 24 = ZX
print('703->' + str(sol.convert_to_title(703)))  # 703 = 1 * math.pow(26,2) + 1 * math.pow(26,2) + 1 = AAA
print('18278->' + str(sol.convert_to_title(18278)))  # 18278 = 26 * math.pow(26,2) + 26 * math.pow(26,1) + 26 * math.pow(26,0) = ZZZ
print('------------')
print('A->' + str(sol.convert_to_index('A')))  # 0*26 + 1 = 1
print('Z->' + str(sol.convert_to_index('Z')))  # 0*26 + 26 = 26
print('AA->' + str(sol.convert_to_index('AA')))  # 1*26 + 1 = 27
print('AZ->' + str(sol.convert_to_index('AZ')))  # AZ = 1*26 + 26 = 52
print('ZX->' + str(sol.convert_to_index('ZX')))  # ZX = 26*26 + 24 = 700
print('AAA->' + str(sol.convert_to_index('AAA')))  # 1 * math.pow(26,2) + 1 * math.pow(26,2) + 1 = 703
print('ZZZ->' + str(sol.convert_to_index('ZZZ')))  # ZZZ = 26 * math.pow(26,2) + 26 * math.pow(26,1) + 26= 18278
"""
