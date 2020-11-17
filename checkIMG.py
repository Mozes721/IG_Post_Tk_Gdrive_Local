import os
import sys
from drive_list import get_file




image = []

def choose_option(): 
        choose = input('Do you want to select your PC data(1) or Gdrive(2) if you wish to quit press q: ')
        if choose == '1':
            check_folder()
        elif choose == '2':
            get_file()
        elif choose.lower() == 'q':
            sys.exit()
        else:
            print('Please choose between (1) or (2) or q')
            choose_option()

#prompt a user to choose where to choose the image in the picture section
def check_folder():
    while True:
        #loop through the picture directory
        for root, dirs, files in os.walk('/home/mozes721/Pictures'):
            choose = input("Do you want to select a folder(1) already or a picture(2) or quit q: ")
            #loop through the available dirs in the directory
            if choose == '1':
                directory = []
                for dir in dirs:
                    #append the new path to the dir
                    directory.append(os.path.join(root, dir))
                print(directory)
                #prompt user to choose a specific folder
                folder_choose =int(input('What folder do you choose out of these given by (0,1,2 etc): '))
                enter_dir = directory[folder_choose]
                print(enter_dir)
                #if dir selected select a desired image 
                if enter_dir:
                    for files in os.walk(enter_dir):
                        pictures = files[2]
                        print(pictures)
                        #choose an image and append it to image variable
                        choose_pic = input('What photo do you choose out of these given: ')
                        if choose_pic in pictures:
                            image.append(os.path.join(root, enter_dir, choose_pic))
                            print("Picture found {}".format(image))
                            return False
                        else:
                            print("The given picture named {} doesnt exist".format(choose_pic))

                else:
                    print('Wrong input given ')
                    check_folder()
            #choose a image from the directory 
            elif choose == '2':
                show_pictures = []
                for pictures in files:
                    show_pictures.append(pictures)
                print(show_pictures)
                choose_pic = input('What photo do you choose out of these given: ')
                if choose_pic in show_pictures:
                    image.append(os.path.join(root, choose_pic))
                    print("Picture found {}".format(image))
                    return False
                else:
                    print("The given picture named {} doesnt exist".format(choose_pic))

            #exit the program
            elif choose.lower() == 'q':
                sys.exit()
            else:
                print('Please choose between (1) or (2) or q')

            break



