a = 'a'
if a == 'c':
    print('==')
else:
    print('!=')

# and or
if a == 'a' and a == 'c':
    print('and')
elif a == 'a' or a == 'c':
    print('or')
# in not in
words = ['a', 'b', 'c']
if a in words:
    print('in')
if 'v' not in words:
    print('not in')

names = []
for name in names:
    print(name)

if names:
    for name in names:
        print(name)
else:
    print('列表为[]')
