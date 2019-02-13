_50pfile = open('50p.txt', 'r')
_50pdata = _50pfile.read().splitlines()
_50pfile.close()
collectionvalue = 0.00
for line in _50pdata:
    _50p = line.split('\t')
    answer = raw_input('Do you own ' + _50p[0] + '? y/n: ')
    if answer == 'y':
        collectionvalue = collectionvalue + float(_50p[1])
print 'Your 50p collection is worth approximately ' + str(collectionvalue) + ' depending on condition.'
