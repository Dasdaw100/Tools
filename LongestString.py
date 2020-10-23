keeper=''

def LongString(string):
    String1=''
    String2=''
    keeper=''
    for i in string:
        if keeper != i:
            
            String1+=i
            
        elif keeper==i:
            if len(String1)>len (String2):
                String2=String1
                String1=''
            
        keeper=i 



    if len(String1)>len (String2):
    return String2
print (LongString('abrkaabcdefghijjxxx'))
