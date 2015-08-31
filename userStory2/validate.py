__author__ = 'Mallik'

'''
User Story 2
 Having done that, you quickly realize that the ingenious machine is not in fact infallible.
 Sometimes it goes wrong in its scanning. The next step therefore is to validate that the numbers you read are in fact valid account numbers.
 A valid account number has a valid checksum. This can be calculated as follows:
```
account number:  3  4  5  8  8  2  8  6  5
position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
Checksum calculation: (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0
```
So now you should also write some code that calculates the checksum for a given number, and identifies if it is a valid account number.

'''

def validate_account(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        new_result = list()
        for acc_num in result:
            if "-1" in acc_num:
                new_result.append(acc_num.replace("-1", "?")+"    ILL")
            else:
                rev_acc_num = acc_num[::-1]
                sum = 0
                count = 1
                while count <= len(rev_acc_num):
                    sum += (count * int(rev_acc_num[count-1]))
                    count += 1
                checksum = sum % 11
                if checksum == 0:
                    new_result.append(acc_num)
                else:
                    new_result.append(acc_num+"    ERR")
        print new_result
        return new_result
    return wrapper