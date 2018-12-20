# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 8:24
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : Stack.py
# @Software: PyCharm

# 定义一个栈类
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# 测试栈的属性
# s = Stack()
# print(s.isEmpty())

# 利用栈将字串反转
def revstring(mystr):
    s = Stack()
    outputStr = ''
    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        outputStr += s.pop()
    return outputStr
# print(revstring("abcd"))


# 利用栈判断括号平衡
def parCheck(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while(index < len(symbolString) and balanced):
        symbol = symbolString[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)

# print(parCheck("(){}"))
# print(parCheck("{[()]}{}"))


# 利用栈将十进制整数转化为二进制整数
def Dec2Bin(decNumber):
    s = Stack()
    while decNumber > 0:
        temp = decNumber % 2
        s.push(temp)
        decNumber = decNumber // 2
    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())
    return binString

# print(Dec2Bin(10))

# 利用栈实现多进制转化
def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decNumber > 0:
        temp = decNumber % base
        s.push(temp)
        decNumber = decNumber // base
    newString = ''
    while not s.isEmpty():
        newString = newString + digits[s.pop()]
    return newString

# print(baseConverter(59, 16))


# 利用栈实现普通多项式的后缀表达式
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in '0123456789' or token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty() and (prec[opStack.peek()] >= prec[token])):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)

print(infixToPostfix("A * B + C * D"))

