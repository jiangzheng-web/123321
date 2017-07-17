height = 1.75;
width = 80.5;
bmi = width / (height * height);
print(bmi)
if bmi <= 18.5:
    print('过轻');
elif bmi <= 25:
    print('正常');
elif bmi <= 28:
    print('过重');
elif bmi <=32:
    print('肥胖');
else:
    print('严重肥胖');
names = {
        'mic' : 65,
        'bob' : 35,
        'dfj': 54
        };
print(names['mic'])
print('mics' in names)
s = set([1, 2, 3]);
s.remove(3)
print(s)
a = ['2', '1', '3'];
a.sort();
a[0] = 'a';
a[0] = a[0].replace('a', 'A');
print(a);
c = 'assd';
d = c.replace('s', 'S');
print(d)