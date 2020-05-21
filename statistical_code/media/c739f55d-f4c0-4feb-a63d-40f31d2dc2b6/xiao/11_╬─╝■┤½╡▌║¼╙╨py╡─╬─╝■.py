import os

dir_list = []


def find_hell(parent_dir, file_name):
    abc_dir_name = os.path.join(parent_dir, file_name)
    if os.path.isdir(abc_dir_name):
        for i in os.listdir(abc_dir_name):
            find_hell(abc_dir_name, i)
    else:
        if abc_dir_name.endswith('py'):
            if read_and_find_hello(abc_dir_name):
                dir_list.append(abc_dir_name)


def read_and_find_hello(py_file):
    flag = False
    f = open(py_file, 'r')
    while True:
        line = f.readline()
        if 'hello' in line:
            flag = True
            break
        elif line == '':
            break
    f.close()
    return flag


# find_hell('/root', 'python练习')
find_hell('D:\01python\day000', '01练习')

if os.path.exists('have_hello_is_file'):
    pass
else:
    os.mkdir('have_hello_is_file')

n = 1
for i in dir_list:
    source_f = open(i, 'r')
    dest_file = ('have_hello_is_file/' + i[i.rfind('/') + 1:])
    dest_f = open(dest_file, 'w')
    content = source_f.read()
    dest_f.write(content)
    source_f.close()
    dest_f.close()
    print('增加%s个文件' % n)
    n = 1 + n
