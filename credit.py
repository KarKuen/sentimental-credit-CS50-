import re

cardno = input("Number: ")

total = 0
for i in range(0, len(cardno), 2):
    if (i + 2 > len(cardno)):
        break
    else:
        oddnum = int(cardno[(len(cardno) - 2 - i)]) * 2
        if oddnum > 9:
            for j in range(len(str(oddnum))):
                total = total + int(str(oddnum)[j])
        else:
            total = total + oddnum


for k in range(0, len(cardno), 2):
    if (k + 1 > len(cardno)):
        break
    else:
        evennum = int(cardno[(len(cardno) - 1 - k)])
        total = total + evennum

if (total % 10 != 0):
    print("INVALID")
else:
    # American Express 15 digit
    if re.search("^34.............$", cardno):
        print("AMEX")
    elif re.search("^37.............$", cardno):
        print("AMEX")
    # MasterCard 16 digit
    elif re.search("^51..............$", cardno):
        print("MASTERCARD")
    elif re.search("^52..............$", cardno):
        print("MASTERCARD")
    elif re.search("^53..............$", cardno):
        print("MASTERCARD")
    elif re.search("^54..............$", cardno):
        print("MASTERCARD")
    elif re.search("^55..............$", cardno):
        print("MASTERCARD")
    # Visa 13 (or 16 digit)
    elif re.search("^4...............$", cardno):
        print("VISA")
    elif re.search("^4............$", cardno):
        print("VISA")
    else:
        print("INVALID")