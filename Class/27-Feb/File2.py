#loops
# for loop
l = [1,2,3,4,5]
for i in l:
    print(i,)
print(range(1,10))


for a in range(1,10,2):
    print(a, end=' ')


for i in range(10,0,-1):
    print(i)


# repalce the space with underscore inside the string
st = input("Enter your text: ")
st.replace(' ','_')
for i in st:
    if i == ' ':
        print('_', end='')
    else:
        print(i, end='')
        
        
#split function
st = "Python is a programming language"
print(st.split())



l = ['p1.py', 'first.txt','t3.py','tk.txt','tfk.com']
d = {}
for i in l:
    part = i.split('.')
    print(part)
    inn = part[0]
    out = part[1]
    
    if out not in d:
        d[out] = []
    d[out].append(inn)
print(d)


stt1 = 'aaabbaabcc'
stt2 =''
i = 0
while i < len(stt1):
    char = stt1[i]
    count = 1
    while i + count < len(stt1) and stt1[i + count] == char:
        count += 1
    stt2 += char + str(count)
    i += count

print(stt2)
    
    
l = ['aditya', 'archit', 'pradit', 'keshav']
v =''
for i in l:
    for j in i:
        if j in 'aeiouAEIOU':
            v+= j
print(v)
print(len((v)))

l = [(2+3j),12,'Program','Python',False]
d = {}
for i in l:
    if( type(i) == str):
        # print(i)
        v = ''
        for j in i:
            if j in 'aeiouAEIOU':
                v+=j
        d.update({i:v})
print(d)
