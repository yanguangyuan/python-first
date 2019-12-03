""" 文件操作 """
# with read 后不需要 close,关键字with 在不再需要访问文件后将其关闭
file_name = 'test.txt'
with open(file_name) as file_object:
    content = file_object.read()
    print('1 '+content)

# 按行读取
with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in file_object:
        print('2 '+line)

for line in lines:
    print('3 '+line)

# 写入 读取取模模式式 （'r' ）、写写入入模模式式 （'w' ）、附附加加模模式式 （'a') 读取和写入文件的模式（'r+' ）
with open(file_name, 'w') as file_object:
    file_object.write('write data ')
with open(file_name, 'a') as file_object:
    file_object.write('write data ')
