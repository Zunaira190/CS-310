print ('Hello World')
print ("Hello World")
print ("Jhon")
print ("Jhon Kennedy")
print ("Hi,I am Python")
print (25)
print (2*2)
print (2+5+9)
print ("Hello,","I","am","Jhon")
print ("Hello Jhon"+"How are you?")
print ("20" + "+" + "2" + "=" + "22")
print ("I am studing BS Bioinformatics")
print ("We are learning Object Oriented Programming from DR. Saqib Ali")
print ('Assignment 5')
X = 43
X = X + 1
print (X)
print ('Hello World')
print ('python learning is necessary for data analysis')
print ('Bioinformatican must command on python for a good data analyser')
X = 6
print (X)
Y = X * 7
print (Y)
print ('Assignment 6')
print (4)
print (4.3)
print (1,000,000)
message = 'And now for something completely different'
n = 17
pi = 3.141592
print (n)
print (pi)
type (message)
type (n)
type (pi)
print (5)
X = 5
print (X + 1)
first = 10
seconde = 15
print (first + seconde)
first = '100'
seconde = '156'
print (first + seconde)
first = 'Test'
seconde = 3
print (first * seconde)
name = input ('what is your name?\n')
print (name)
Hours = 35.0
Rate = 2.75
Pay = Hours * Rate 
print (Pay)
width = 17
height = 12.0
print (width//2)
print (width/2)
print (height/3)
print (1+2*3)
inp = input ('Enter Celsius Temperature:')
cel = float (inp)
fahr = (cel * 9.0) / 5.0 + 32.0
print (fahr)


print('Assignment # 1')

my_list = []                        # Initialize array
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))

def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != 'From' :
        continue
    print(words[2])

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    print(words[2])

my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word in my_list:
            continue
        my_list.append(word)

print(sorted(my_list))


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1

print('there are %d line in the file with From as the first word' % count)

my_list = []
ize array
while True:
    number = 0.0
    inp = input('Enter a number:')
    if inp == 'done' : break

    try:
        number = float(inp)
    except ValueError:
        print('Invali syntax')
        quit()

my_list.append(inp)

print('Maximun', max(my_list))
print('Manium' , min(my_list))

numlist = ()
whlie (True):
    inp = input('Enter a number')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average' , average)

counts = dict()
names = ['cedf', 'asdg', 'klia']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

counts = dict()
print('Enter a line from text:')
line = input('')
words = line.split()

print('Words:', words)

print('Countng....')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigword is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)


count = 0
dictionary_words = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = counts

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')

dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print(dictionary_days)





dictionary_addres = dict()
fname = input('Enter file:')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('file not found:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if word[1] not in dictionary_addres:
            dictionary_addres[words[1]] = 1
        else:
            dictionary_addres[words[1]] += 1

print(dictionary_addres)



dictionary_addresses = dict()                   # Initialize variables
maximum = 0
maximum_address = ''

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1      # First entry
    else:
        dictionary_addresses[words[1]] += 1     # Additional counts

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:     # Checks if new maximum
        # Update the maximum if needed
        maximum = dictionary_addresses[address]
        # Stors the address of maximum
        maximum_address = address

print(maximum_address, maximum)

dictionary_domains = dict()                       # Initialize variables

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')               # Position of '@'
        domain = words[1][atpos+1:]              # Store characters after '@'
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1       # First entry
        else:
            dictionary_domains[domain] += 1      # Additional counts

print(dictionary_domains)







































