p = str(input('enter password : '))
t = 0
if(len(p) >= 6 and len(p) <= 16):
    t += 1
for i in range(len(p)):
    if(ord(p[i]) >= 65 and ord(p[i]) <= 90):
        t += 1
        break
for i in range(len(p)):
    if(ord(p[i]) >= 97 and ord(p[i]) <= 122):
        t += 1
        break
for i in range(len(p)):
    if(ord(p[i]) >= 48 and ord(p[i]) <= 57):
        t += 1
        break
for i in range(len(p)):
    if(ord(p[i]) == 36 or ord(p[i]) == 35 or ord(p[i]) == 64):
        t += 1
        break
if(t == 5):
    print('password is valid')
else:
    print('password is invalid')