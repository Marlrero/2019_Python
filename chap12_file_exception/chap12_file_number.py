outfile = open('number.txt', 'w')

for i in range(10):
    outfile.write(str(i) + ' ')

outfile.close()