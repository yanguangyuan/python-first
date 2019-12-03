
def division(one, two):
    """两个数相除"""
    try:
        answer = one / two
    except ZeroDivisionError:
        print('zero division')
        # 可以直接用pass标识啥都不做
        pass
    else:
        print(answer)


division(2, 3)
division(1, 0)
