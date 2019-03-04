import random
import string
import datetime


def password_gen(length=12):
    """
    Will generate the desired password and will save the
    output to a file if the path is provided.

    :param length: desired length of the password

    :rtype: string
    """

    # added all the chars in a list form
    chars = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    # shuffling the list
    random.shuffle(chars)
    # a list to store strings
    templist = []


    path = input("path of the file you want to save the passwords to: ")
    application = input("App Or website that you created password for: ")

    for item in range(length):
        char = random.choice(chars)
        templist.append(char)
        #removing the used char so no repetition in the pass
        chars.remove(char)


    password = "".join(templist)

    # writing the password the file with the date stamp
    if path != '':
        file = open(path, 'a')
        file.write('\n'+ 8*'-' + str(datetime.datetime.now()) + 8*'-' + '\n')
        file.write(application +':- ' + password + '\n')
        file.close()
    return password



if __name__ == "__main__":
    print(password_gen())




