#Input from user
def inputFromUser():
    rowIn=input("Enter the string in which you hve to check:")
    rowIn=rowIn.lower() #Here convert all string letter to lower case for easy to compare
    rowList=list(rowIn) #convert string to list 
    return rowList
#remove extra char
def removeExtra(hardLt):
    extrakey=[" ",",",":",".","/","-","!","#"]
    for char in extrakey:
        if char in hardLt:
            hardLt.remove(char)
            return removeExtra(hardLt)
    return hardLt
#function to check palindrome or not
def checkPl(upfinalLt):
    upfinalLtRev=upfinalLt[::-1]#use inbuilt python fun to reverse corrent list
    if upfinalLtRev == upfinalLt:
        return("\nHeyy It's Palindrome String")
    else:
        return("\nHeyy your String not Palindrome Let's try with other Input")
#define main function
def main():
    print("Hello Welecome to my custom palindrome checker!!\n")
    inputLt=inputFromUser()
    upgradeLt=removeExtra(inputLt)
    checkPL=checkPl(upgradeLt)
    print(checkPL)
    print("\nThank you for choosing me!!!")
#main function
main()