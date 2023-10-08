
def bin2dec(s):
    n = 1
    out = 0
    for i in s[::-1]:
        if i == '1': out += n
        n <<= 1
    return out

print(bin2dec('10111'))

bin2dec('1100')

bin2dec('1010')
