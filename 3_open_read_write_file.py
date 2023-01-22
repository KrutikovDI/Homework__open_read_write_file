final = []
with open('1.txt') as f1:
    res1 = f1.readlines()
    count1 = len(res1)
    name1 = '1.txt'
    final1 = [name1] + ['\n'] + [str(count1)] + ['\n'] + res1 + ['\n']
    final.append(final1)
with open('2.txt') as f2:
    res2 = f2.readlines()
    count2 = len(res2)
    name2 = '2.txt'
    final2 = [name2] + ['\n'] + [str(count2)] + ['\n'] + res2 + ['\n']
    final.append(final2)
with open('3.txt') as f3:
    res3 = f3.readlines()
    count3 = len(res3)
    name3 = '3.txt'
    final3 = [name3] + ['\n'] + [str(count3)] + ['\n'] + res3 + ['\n']
    final.append(final3)

def sort_files(file):
    return file[2]
final.sort(key=sort_files)

final_list = []
for i in final:
    final_list += i 

with open('final_name.txt', 'w') as final_name:
    final_name.writelines(final_list)