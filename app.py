from languages import html, py, java, c, cpp
import tkinter.filedialog as f
from datetime import datetime
import os


timeCreated = datetime.today().strftime('%d-%m-%Y')
langs = ['html', 'py', 'java', 'c', 'cpp']

inputName = input('Name: ')
print('')

incorrectProjectType = True

while incorrectProjectType:
    inputProject = input('Language: ')
    for lang in langs:
        if inputProject == lang:
            incorrectProjectType = False
print('')

# choose the directory where you want to save your project! --it's going to create the folder in the directory for you
directory = f.askdirectory(title='Choose Directory')

# concatenate Strings
project_name = inputName
project_name = "/%s" % project_name
directory = directory+project_name


if 'html' in inputProject:
    html(directory)
elif 'py' in inputProject:
    py(directory)
elif 'java' in inputProject:
    java(directory)
elif 'c' in inputProject:
    c(directory)
elif 'cpp' in inputProject:
    cpp(directory)


print('')


def otherReq():
    # other requirements
    loadOther = input('Other requirements? (Y/N) - ')
    print('')
    # in case of other REQUIREMENTS

    if 'Y' in loadOther:
        version = input('Change Version: ')
        print('')
        licenseInput = input('License: ')
        print('')

        printAndCreate(version, licenseInput)

    elif 'N' in loadOther:
        version = '1.0.0'
        licenseInput = None

        # method creates information file showing what type what language the file is, version of the application etc.
        printAndCreate(version, licenseInput)

    else:
        print('please enter a valid parameter (Y/N)')
        print('')
        otherReq()


def createInfoFile(n, l, v, li):
    infoPath = '%s\info.txt' % directory
    file = open(infoPath, 'w+')
    file.write('PROJECT - %s {' % n)
    file.write('\n')
    file.write(' Lang/Type : %s' % l)
    file.write('\n')
    file.write(' Version : %s' % v)
    file.write('\n')
    file.write(' License : %s' % li)
    file.write('\n')
    file.write(' Created : %s' % timeCreated)
    file.write('\n')
    file.write('}')


def printAndCreate(v, li):
    print('PROJECT -', inputName.upper(), ' {' + '\n', '\n' + 'Language/Type: ' + inputProject.upper() + '\n',
          '\n' + 'Directory/Path: ' + directory + '\n', '\n' + 'Version: ' + v + '\n', '\n' + 'License: ', li, '\n', '\n' + 'Time Created: ', timeCreated, '\n', '}', '\n')

    createInfoFile(inputName.upper(), inputProject.upper(),
                   v, li)


otherReq()
