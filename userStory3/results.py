__author__ = 'Mallik'

'''
User Story 3

  Your boss is keen to see your results. He asks you to write out a file of your findings, one for each input file, in this format:
```
457508000

664371495 ERR

86110??36 ILL
```
i.e., the file has one account number per row. If some characters are illegible, they are replaced by a ?.
In the case of a wrong checksum, or illegible number, this is noted in a second column indicating status.

'''
def output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        output_file_name = args[0].split('.')[0]+'_output.txt'
        file = open(output_file_name, 'w+')
        for acc_num in result:
            file.write(acc_num+"\n")

        return result
    return wrapper