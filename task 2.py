fileName=(input("Input the Filename : "))
if fileName.endswith('.py'):
    print("The extension of the file is : 'python'")
if fileName.endswith('.html'):
        print("The extension of the file is : 'html'")
elif fileName.endswith('.java'):
        print("The extension of the file is : 'java'")
elif fileName.endswith('.cpp'):
        print("The extension of the file is : 'c++'")
elif fileName.endswith('.c'):
        print("The extension of the file is : 'c'")
else:
    print("Extension not valid")