#################################################################
##                                                             ##
##   Author   : Ankit Kumar Aman (vinashak)                    ##
##   Contact  : www.ankitaman.in                               ##
##   Github   : https://github.com/VinashakAnkitAman           ##
##                                                             ##
#################################################################

import glob
import re

all_files = glob.glob("s1aptests/test_*")

cnt = 0
cntNoCls = 0
cntNoFunc = 0
for testfile in all_files:
    cnt+=1

    fileName = testfile
    functionName = fileName.replace('s1aptests/', '').replace('.py', '')
    className = ''.join(elem.capitalize() for elem in functionName.split('_'))
    #print(fileName, functionName, className)
    
    file1 = open(fileName, "r")
    
    # Read file content
    readfile = file1.read()
    
    class_string = "class " + className + "("
    is_class_exists = "not"
    if class_string.lower() in readfile.lower():
        is_class_exists = "yes"
    
    function_string = "def " + functionName + "("
    is_function_exists = "not"
    if function_string.lower() in readfile.lower():
        is_function_exists = "yes"
  
    if is_class_exists == "not" or is_function_exists == "not":
        if is_class_exists == "not":
            cntNoCls += 1
        if is_function_exists == "not":
            cntNoFunc += 1
        print(cnt, "--", is_class_exists, "--", is_function_exists, "--## ", fileName)
    else:
        print(cnt, "--", is_class_exists, "--", is_function_exists)

    # Close the file
    file1.close()

print("Total non-matching class:", cntNoCls)
print("Total non-matching Function:", cntNoFunc)
