
import re

with open("invited_names.txt",'r') as invited:
    # print(invited.read())
    # names = re.split('\w+',invited.read())
    # # print(r1)
    names = invited.readlines()
    # print(names)

with open("starting_letter.txt",'r') as invitation:
    lines = invitation.readlines()
    # print(lines)

# print("".join(lines))
if True:
    # lst = [i[:-1] if '\n' in i else i for i in names]
    tick_list = [i.strip("\n") for i in names]
    print(tick_list)
    for i in tick_list:
        # print(i[:-1])
        with open("../output/ready_to_send/letter_for_{}.txt".format(i),mode='w') as letter:
            lines[0] = "Dear {},".format(i)
            letter.write("".join(lines))


