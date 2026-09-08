#File handling
#The process of performing operations on a file such as creating, writing ,reading, opening or closing through a programm interface is called File Handling 


#Example 1 (opening a File)
f = open("Day_17/file1.txt",'r')
print(f) #this prints the file object not the content

#Example 2 (Check for file properties)
f = open("Day_17/file1.txt",'r')
print("filename: ",f.name)
print("File Content:",f.read())
print("mode:",f.mode)
f.close()
print("is Closed?:",f.closed)


#example 3 (writing in a file)
with open("Day_17/file1.txt",'w') as file:
    file.write("This is a way of writing in a file/n")
    file.write("File handling is easy with python")

#example 4 
with open("Day_17/file1.txt",'r') as file:
    content = file.read()
    print(content)
    
#in with statement the file hets sutomatically closed after performing the task 
#these are the basic concepts of file handling

    