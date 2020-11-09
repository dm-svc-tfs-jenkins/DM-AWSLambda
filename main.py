import string
import sys
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(env: string, lname: string):
    # Use a breakpoint in the code line below to debug your script.
	print('Hi, There')
	print('Arguments from the Jenkins Job: ' + str(sys.argv[1]), str(sys.argv[2]))
	print('Method Parameters: ' + env +' '+lname)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
