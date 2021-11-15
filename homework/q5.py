import re

a = input()

p = input()
q = input()

print(re.sub(f'^{p}(?P<trailing1> )|(?P<leading> ){p}(?P<trailing2> ?)',
      f'\g<leading>{q}\g<trailing1>\g<trailing2>', a))
print(re.sub(f'^{p} | {p}', '', a))
