import sys, random, math

if len(sys.argv) <= 1:
    len = int(input('Number of values\n'))
else:
    len = int(sys.argv[1])

for x in range(0, len):
    temp_min = str(random.randint(11,14))
    temp_sec = str(random.randint(30,59))
    print ("00:" + temp_min + ":" + temp_sec)