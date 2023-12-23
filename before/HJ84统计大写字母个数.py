import sys
import re
for line in sys.stdin:
    a = line.strip()
    ret = re.findall("[A-Z]",a)
    print(len(ret))
