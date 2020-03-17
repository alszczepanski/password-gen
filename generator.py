import secrets as s

# Lists of characters used to generate passwords.

easy_chars = ['1','2','3','4','5','6','7','8','9','0']
med_chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hard_chars = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}',';',':',';','"',"'",',','<','.','>','/','?','|']

weak = easy_chars
average = easy_chars + med_chars
strong = easy_chars + med_chars + hard_chars

easy_passwords = []
med_passwords = []
hard_passwords = []


def generate(length, mode):
    password = ''
    # Mode 0 creates easy passwords.
    # Mode 1 creates average passwords.
    # Mode 2 creates strong passwords.
    if mode == 0:
        for each in range(length):
            password += weak[s.randbelow(len(weak))]
    elif mode == 1:
        for each in range(length):
            password += average[s.randbelow(len(average))]
    elif mode == 2:
        for each in range(length):
            password += strong[s.randbelow(len(strong))]

    return password

def generate_lists(pass_qty,length,mode):
    passwords = []
    for i in range(pass_qty):
        passwords.append(generate(length,mode))
    return passwords

def export_to_file(pass_list,filename):
    with open(filename,'w') as file:
        for counter,each_pass in enumerate(pass_list,1):
            file.write(str(counter) + '. ' + each_pass + '\n')




