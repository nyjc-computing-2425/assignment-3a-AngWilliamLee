nric = input('Enter an NRIC number: ')

prefix = nric[0].upper()
digits = nric[1:8]
suffix = nric[8:].upper()
prefix_str = "STFG"
suffix_str_1 = "JZIHGFEDCBA"
suffix_str_2 = "XWUTRQPNMLK"
invalid_nric = "NRIC is invalid."
valid_nric = "NRIC is valid."


if not prefix in prefix_str:
    print(invalid_nric)

elif len(digits) != 7:
    print(invalid_nric)

elif len(suffix) != 1:
    print(invalid_nric)

elif not (digits.isdigit()):
    print(invalid_nric)\

elif not suffix.isalpha():
    print(invalid_nric)

elif (suffix not in suffix_str_1) and (suffix not in suffix_str_2):
    print(invalid_nric)

else:
    total = int(digits[0]) * 2\
          + int(digits[1]) * 7\
          + int(digits[2]) * 6\
          + int(digits[3]) * 5\
          + int(digits[4]) * 4\
          + int(digits[5]) * 3\
          + int(digits[6]) * 2\

    if prefix in "TG":
        total = total + 4

    remainder = total % 11

    check_alpha = ''
    if prefix in "ST":
        check_alpha = suffix_str_1[remainder]
    elif prefix in "FG":
        check_alpha = suffix_str_2[remainder]

    if suffix == check_alpha:
        print(valid_nric)
    else:
        print(invalid_nric)
