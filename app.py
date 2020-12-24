import os
import time
os.system("color b")
# Input from user
std_name = str(input("Enter the name of the student: "))
# While for error
while std_name == "":
    os.system("cls")
    print("Plz type the name of the child !")
    std_name = str(input("Enter the name of the student: "))
#########################################################################
std_marks_maths = int(float(input("Enter marks of Maths: ")))
if std_marks_maths == "":
    print("Plz type the marks of maths!")
    std_marks_maths = int(float(input("Enter marks of Maths: ")))
  

#############################################################################
std_marks_sci = int(float(input("Enter marks of Science: ")))

################################################################################
std_marks_hindi = int(float(input("Enter marks of Hindi: ")))

#####################################################################################
std_marks_english = int(float(input("Enter marks of English: ")))

#######################################################################################
std_marks_SST = int(float(input("Enter marks of SST: ")))

#######################################################################################
std_marks2 = int(input("Enter the marks out of which student scored: "))

#########################################################################################
# Making Formula for calculation
if (std_marks_english and std_marks_hindi and std_marks_maths and std_marks_sci and std_marks_SST) >= std_marks2 :
    print("An Error Occured!")
    os.system("exit")
mrk_output = (std_marks_maths+std_marks_sci+std_marks_SST+std_marks_hindi+std_marks_english)/(std_marks2*5)*100
ttl_marks = (std_marks_maths+std_marks_sci+std_marks_SST+std_marks_hindi+std_marks_english)

# Customising the screen
os.system("cls")
os.system("color a")

# Print Marks 
print("Student Name:",std_name)
print("\n")
print("Subject   Marks")
print("Maths     " ,std_marks_maths,"/",std_marks2)
print("Science   " ,std_marks_sci,"/",std_marks2)
print("Hindi     " ,std_marks_hindi,"/",std_marks2)
print("English   " ,std_marks_english,"/",std_marks2)
print("SST       " ,std_marks_SST,"/",std_marks2)
    
print("\n")
print(("Total Marks:{}".format(ttl_marks)),"/",std_marks2*5)

# Showing Marks
print("\n")
print("Hey {} , you got".format(std_name),mrk_output,"%")
blank = input("")