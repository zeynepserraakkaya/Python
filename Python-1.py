#!/usr/bin/env python
# coding: utf-8

# # PYTHON

# # OBJECT AND DATA STRUCTURE BASICS

# PYTHON DATA TYPES

# Name: Integers
# Type: int

# In[1]:


a=3
b=18


# In[2]:


a


# In[3]:


b


# Name: Floating Point
# Type: float

# In[4]:


c=3.3
d=101.0


# In[5]:


c


# In[6]:


d


# Name: Strings
# Type: str

# In[7]:


"Hi!"


# In[8]:


"Welcome!"


# In[9]:


"18"


# In[10]:


'morning'


# In[11]:


x="Zeynep"


# In[12]:


x


# Name: Lists
# Type: list

# In[13]:


[10,11]


# In[14]:


[1,2,"Istanbul"]


# In[15]:


[3.3,"18",18,"Turkey"]


# In[16]:


e=[1,2,3,4,5,"Python","Programming","Language"]


# In[17]:


e


# Name: Dictionaries
# Type: Dict

# In[18]:


{"myname":"Zeynep","myage":18}


# In[19]:


f={"key":"value"}


# In[20]:


f


# Name: Tuples
# Type: tup

# In[21]:


(1,2,3,18.8,13.3,"coding")


# In[22]:


g=(3,"A",2,1)


# In[23]:


g


# Name: Sets
# Type: set

# In[24]:


{"a","b"}


# In[25]:


h={1,2,"c","d"}


# In[26]:


h


# Name: Booleans
# Type: bool

# In[27]:


True


# In[28]:


False


# PYTHON NUMBERS

# In[29]:


3+5


# In[30]:


5-3


# In[31]:


3*5


# In[32]:


5/3


# In[33]:


5//3


# In[34]:


#Mod (Modulo) Operator


# In[35]:


5/3


# In[36]:


5%3


# In[37]:


6%3


# In[38]:


2*3


# In[39]:


2**3


# In[40]:


3**2


# In[41]:


9**0.5


# In[42]:


2+3*4+5


# In[43]:


(2+3)*(4+5)


# VARIABLE ASSIGNMENTS

# In[44]:


a=5


# In[45]:


a


# In[46]:


a=10


# In[47]:


a


# In[48]:


a+a


# In[49]:


a*a


# In[50]:


a=a+a


# In[51]:


a


# In[52]:


a=a+a


# In[53]:


a


# In[54]:


#important
type(a)


# In[55]:


b=3.3


# In[56]:


type(b)


# In[57]:


my_income=150
tax_rate=0.1
my_tax=my_income*tax_rate


# In[58]:


my_tax


# STRINGS

# In[59]:


'Hi'


# In[60]:


"Hello"


# In[61]:


"I don't want to do that."


# In[62]:


#indexing


# In[63]:


#"hi"
#h: 0. index #important
#i: 1. index


# In[64]:


#reverse index
#"hello"
#h: 0. index
#e: -4. index
#l: -3. index
#l: -2. index
#o: -1. index #important


# In[65]:


#slicing
#[start:stop:step]
#start: index
#stop: index, not include


# In[66]:


"hi"


# In[67]:


print("hi")


# In[68]:


"zeynep"
"akkaya"


# In[69]:


print("zeynep")
print("akkaya")


# In[70]:


print("zeynep\nakkaya")
# \n


# In[71]:


print("zeynep\takkaya")
# \t # 4 spaces


# In[72]:


#length function
# len()


# In[73]:


len("hi")


# In[74]:


len("i am")


# INDEXING AND SLICING
# STRINGS

# In[75]:


my_string="Hi everyone!"


# In[76]:


my_string


# In[77]:


#indexing


# In[78]:


my_string[0]


# In[79]:


my_string[1]


# In[80]:


my_string[2]


# In[81]:


my_string[11]


# In[82]:


my_string[-1]


# In[83]:


my_string[10]


# In[84]:


my_string[-2]


# In[85]:


#slicing


# In[86]:


my_string[2]


# In[87]:


my_string[2:]


# In[88]:


my_string[:3] #not include 3. index


# In[89]:


my_string[:2]


# In[90]:


my_string[3:11]


# In[91]:


my_string[3:12]


# In[92]:


my_string[3:13]


# In[93]:


my_string[::]


# In[94]:


my_string[::2]


# In[95]:


my_string[::3]


# In[96]:


my_string[3:13:2]


# In[97]:


my_string1="zxexyxnxexpx"


# In[98]:


my_string1[::2]


# In[99]:


my_string1[::-1] #reverse


# In[100]:


my_string[::-1]


# STRING PROPERTIES - STRING METHODS

# In[101]:


#Immutability
#can't mutate or can't change


# In[102]:


name="Zeynep"


# In[103]:


# name[0]="x"
# strings are immutable


# name[0]="x"
# TypeError: 'str' object does not support item assignment

# In[104]:


last_letters=name[1:]


# In[105]:


last_letters


# In[106]:


"x"+last_letters


# In[107]:


a="hi"


# In[108]:


a+"everyone"


# In[109]:


a+" everyone"


# In[110]:


a=a+" everyone"


# In[111]:


a


# In[112]:


age="18"


# In[113]:


age*10


# In[114]:


3+6


# In[115]:


"3"+"6"


# In[116]:


x="hi world"


# In[117]:


# x. tab
#all methods


# In[118]:


x.upper() #upper()


# In[119]:


x


# In[120]:


x=x.upper()


# In[121]:


x


# In[122]:


x.lower() #lower()


# In[123]:


x


# In[124]:


x=x.lower()


# In[125]:


x


# In[126]:


x.split() #split()


# In[127]:


y="hi, this is a string."


# In[128]:


y.split()


# In[129]:


y.split("i")


# print()

# In[130]:


my_name="Zeynep"


# In[131]:


print("My name is"+my_name)


# In[132]:


print("My name is "+my_name)


# .format()

# In[133]:


print("My name is {}.".format(my_name))


# In[134]:


print("{},{},{}".format(1,2,3))


# In[135]:


print("{2},{1},{0}".format(1,2,3))


# In[136]:


print("{0},{0},{0}".format(1,2,3))


# In[137]:


print("{one},{two},{three}".format(one="1",two="2",three="3"))


# In[138]:


print("{one},{one},{one}".format(one="1",two="2",three="3"))


# In[139]:


# {value:width.precision f}


# In[140]:


result=100/350


# In[141]:


result


# In[142]:


print("The result is: {}".format(result))


# In[143]:


print("The result is: {x}".format(x=result))


# In[144]:


print("The result is: {x:1.3f}".format(x=result))


# In[145]:


print("The result is: {x:10.3f}".format(x=result))


# In[146]:


print("My name is {}.".format(my_name))


# In[147]:


print(f"My name is {my_name}.") #f strings #formatted string literals


# In[148]:


name="Elif"
age=40


# In[149]:


print(f"{name} is {age}.")


# In[150]:


# %s


# In[151]:


print("My name is %s" %"Zeynep")


# In[152]:


# %r


# In[153]:


print("My name is %r" %"Zeynep")


# In[154]:


x,y="5","15"


# In[155]:


print("first %s, second %s" %(x,y))


# LISTS

# In[156]:


my_list1=[1,2,3]


# In[157]:


my_list=["Istanbul",18,13.3,"Zeynep",18.4]


# In[158]:


len(my_list)


# In[159]:


my_list[0]


# In[160]:


my_list[1]


# In[161]:


my_list[1:]


# In[162]:


my_list+my_list1


# In[163]:


my_list1+my_list


# In[164]:


new_list=my_list1+my_list


# In[165]:


new_list


# In[166]:


my_list


# In[167]:


my_list1


# In[168]:


new_list[0]="This is a list."


# In[169]:


new_list


# In[170]:


#append()


# In[171]:


new_list.append("America")


# In[172]:


new_list


# In[173]:


#pop


# In[174]:


new_list.pop


# In[175]:


new_list.pop()


# In[176]:


new_list


# In[177]:


popped_item=new_list.pop() #important


# In[178]:


popped_item


# In[179]:


new_list


# In[180]:


new_list.pop(0)


# In[181]:


new_list


# In[182]:


new_list1=["a","x","m","n","c","b"]


# In[183]:


# sort()


# In[184]:


new_list1.sort()


# In[185]:


new_list1


# In[186]:


my_sorted_list=new_list1.sort()


# In[187]:


my_sorted_list


# In[188]:


type(my_sorted_list)


# In[189]:


None


# In[190]:


# reverse()


# In[191]:


new_list1.reverse()


# In[192]:


new_list1


# DICTIONARIES

# In[193]:


my_dict={"key1":"value1","key2":"value2"}


# In[194]:


my_dict


# In[195]:


my_dict["key1"]


# In[196]:


my_dict["key2"]


# In[197]:


dict1={"k1":1,"k2":[1,3,5],"k3":"v3","k4":{"a":"b"}}


# In[198]:


dict1


# In[199]:


dict1["k1"]


# In[200]:


dict1["k2"]


# In[201]:


dict1["k2"][0]


# In[202]:


dict1["k2"][1]


# In[203]:


dict1["k2"][2]


# In[204]:


dict1["k3"]


# In[205]:


dict1["k4"]


# In[206]:


dict1["k4"]["a"]


# In[207]:


d=dict1["k2"]


# In[208]:


d


# In[209]:


d[0]


# In[210]:


d[1]


# In[211]:


d[2]


# In[212]:


dict1


# In[213]:


dict1["Zeynep"]="myname"


# In[214]:


dict1


# In[215]:


dict1["k1"]


# In[216]:


dict1["k1"]="123"


# In[217]:


dict1["k1"]


# In[218]:


dict1.keys() # keys()


# In[219]:


dict1.values() # values()


# In[220]:


dict1.items() # items()


# TUPLES

# In[221]:


#immutable


# In[222]:


t=(1,2,3)


# In[223]:


t


# In[224]:


type(t)


# In[225]:


len(t)


# In[226]:


t=("Jupyter",15)


# In[227]:


t


# In[228]:


t[0]


# In[229]:


t[1]


# In[230]:


t=("a","x","a",1,"a")


# In[231]:


# count()


# In[232]:


t.count("a")


# In[233]:


# index()


# In[234]:


t.index("x")


# In[235]:


t.index(1)


# In[236]:


t.index("a")


# In[237]:


# t[0]="morning"
# 'tuple' object does not support item assignment


# SETS

# In[238]:


my_set=set()


# In[239]:


my_set


# In[240]:


# add()


# In[241]:


my_set.add(1)


# In[242]:


my_set


# In[243]:


my_set.add(2)


# In[244]:


my_set


# In[245]:


my_set.add(2)


# In[246]:


my_set


# In[247]:


my_list=[1,1,2,2,3,3,"a","a","a","a","x",5,"x",5,"x"]


# In[248]:


my_list


# In[249]:


set(my_list)


# BOOLEANS

# In[250]:


True


# In[251]:


False


# In[252]:


type(True)


# In[253]:


type(False)


# In[254]:


2>1


# In[255]:


1>2


# In[256]:


1==1


# In[257]:


x=None


# In[258]:


x


# In[259]:


type(x)


# FILES

# In[260]:


#Jupyter


# In[261]:


get_ipython().run_cell_magic('writefile', 'my_file.txt', 'Hi, this is a file.\nAnd I am Zeynep.')


# In[262]:


# open()


# In[263]:


my_file=open("my_file.txt")


# In[264]:


pwd # print working directory


# In[265]:


# read()


# In[266]:


my_file.read()


# In[267]:


my_file.read() #important


# In[268]:


# seek()


# In[269]:


my_file.seek(0)


# In[270]:


my_file.read()


# In[271]:


my_file.seek(0)


# In[272]:


contents=my_file.read()


# In[273]:


contents


# In[274]:


contents


# In[275]:


my_file.seek(0)


# In[276]:


# readlines()


# In[277]:


my_file.readlines()


# In[278]:


#File Locations


# In[279]:


pwd


# In[280]:


# close()


# In[281]:


my_file.close()


# In[282]:


my_file=open("my_file.txt")


# In[283]:


# with # as


# In[284]:


with open("my_file.txt") as my_file1:
    contents1=my_file1.read()


# In[285]:


contents1


# In[286]:


# mode="r" #read only


# In[287]:


with open("my_file.txt",mode="r") as my_file1:
    contents1=my_file1.read()


# In[288]:


#mode="w": write only, overwrites files or creates new
#mode="a": append only
#mode="r+": reading and writing
#mode="w+": writing and reading, overwrites files or creates new


# In[289]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'Zeynep\nAkkaya\nHi, everybody')


# In[290]:


with open("my_new_file.txt",mode="r") as f:
    print(f.read())


# In[291]:


with open("my_new_file.txt",mode="a") as f:
    f.write("Python")


# In[292]:


with open("my_new_file.txt",mode="r") as f:
    print(f.read())


# In[293]:


with open("new_file.txt",mode="w") as f:
    f.write("i just created this file.")


# In[294]:


with open("new_file.txt",mode="r") as f:
    print(f.read())

