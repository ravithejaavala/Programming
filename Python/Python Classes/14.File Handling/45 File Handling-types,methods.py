# 21-04-25
'''

File handling:
-------------

For any web application the below requiremenets are mandatory...

UI   ---  BACKEND     ---- DATABASE
html        python          mysql
cssc        java            postgres
js          C++             mongo db(no sql)
reat
angular

API:

Phone Pee: Bank statement?? pdf?

post
get
put
delete

File handling refers to the process of performing operations on a file such as
creating, opening, writing, and closing it through programing interface...
It involves managing the data flow between the program and the file system on
the storage device, ensuring the data is handled safely and efficiently...

Advatnages:
-----------
1. data can be stored permanently
2. we can update the data in file whenver required
3. file can be shared to multiple users when required
4. To store huge amount of data files are very helpful...


Types of files:
-------------
1. Text files:
stores data in form of characters

2. Binary files:
Stores data in form of bytes. It can be used to store text, audio, video , images...


To open file:
--------------
file = open('filename', 'mode')

Fiel open mode Description:
--------------------------------

w : writes the data into the file. If data exists already, it will be deleted and new
    data will be written.

r : reads the data from file. File pointer is positioned at begining of the file

a : appends the data into the file. If data already exists it will start appending
    from last line of file

w+ : Writes and reads the data of the file. Previous data in the file will be deleted

r+ : Reads and Writes the data into the file. Previous data in the file will not be deleted

a+ : Appends and Reads the data of file. File pointer will be at end of the file

x (exclusive creation mode) :  Opens file in exclusive creation mode, if the file
                                already exists, it will raises an error..
'''

# write
# open('filename', 'mode')

my_file = open('sam.txt','w')
my_file.write('Hello world!!')
# my_file.write('Hi!!!')

# write() mode
file_wr = open('wish.txt','w')
file_wr.write('this is sarath')
file_wr.close()

# read() mode
file_re = open('wish.txt','r')
read_con = file_re.read()
print(read_con)
file_re.close()

# append() mode

file_ap = open('wish.txt', 'a')
file_ap.write(' and am in banagalore')
file_ap.close()

# with() statement

# write() mode by using the with() statement

with open('display.txt','w') as file_w:
    file_w.write('hello team')
    file_w.close()

# read() mode by using the with() statement

with open('display.txt','r') as file_r:
    res = file_r.read()
    print(res)
    
# context manager