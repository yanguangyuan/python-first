names = ['tom', 'jack', 'bruce', 'wu']
print(names)
print(names[0])
print(names[0].title())
# 倒数访问写法
print(names[-1])
# 修改值
names[0] = 'Mary'
print(names)
# 在末尾添加元素
names.append('Teemo')
print(names)
# 添加到指定索引位置
names.insert(0, 'Teemo')
print(names)
# 删除
del names[0]
print(names)
# 弹出元素(取出并删除)
a = names.pop()
b = names.pop(0)
print(a)
print(b)
print(names)
# 根据值删除
names.remove('wu')
print(names)
# 确定列表长度
print(len(names))
# 列表遍历
for name in names:
    print(name)
    # 只会修改临时name值，并不会对names里面的值进行修改
    name = 'a'
    print(name)
print(names)
names.append('Teemo')
names.append('Mary')
print('\n')
# 获取列表切片(一段)，不包含结尾元素 返回一个新列表（新引用）
print(names[:1])
print(names[1:])
print(names[1:3])
print(names[:])
names_copy = names[:]
names_copy[0] = 'jack_copy'
print(names)
print(names_copy)


# 元组，不能修改元组的元素，但可以修改元组
dimensions = (100, 200)
# dimensions[0] = 123
dimensions = (300, 500)
