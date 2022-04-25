class Calculator:
    def __init__(self):
        self.__stack = []
        self.__temp = []
        self.__priority = {'+': 1, '-': 1, '_':1, '*': 2, '/': 2}
        self.__binaryOperators = ['+', '-', '*', '/']


    def calculate(self, expresion):
        self.__fillStack(expresion)
        result = self.__calculatePostfix()
        self.__stack = []
        self.__temp = []
        return result

    
    def __calculatePostfix(self):
        s = []
        
        for item in self.__stack:
            if self.__isOperand(item):
                s.append(int(item))
            result = None
            if len(s) > 0:
                if item == '_':
                    result = s.pop() * (-1)
                elif item == '+':
                    lhs = s.pop()
                    rhs = s.pop()
                    result = rhs + lhs
                elif item == "-":
                    lhs = s.pop()
                    rhs = s.pop()
                    result = rhs - lhs
                elif item == "*":
                    lhs = s.pop()
                    rhs = s.pop()
                    result = rhs * lhs
                elif item == "/":
                    lhs = s.pop()
                    rhs = s.pop()
                    result = rhs / lhs
            if result is not None:
                s.append(result)

        return s.pop()


    def __fillStack(self, expresion):
        lastItem = ''
        for idx, item in enumerate(expresion):
            if self.__isOperand(item):
                lastItemInStack = self.__peek()
                if lastItemInStack != '$' and self.__isOperand(lastItemInStack) and self.__isOperand(lastItem):
                    lastItemInStack += item
                    self.__pop()
                    self.__push(lastItemInStack)
                    lastItem = item
                else:
                    self.__push(item)
                    lastItem = item
            elif item == '(':
                self.__temp.append(item)
                lastItem = item
            elif item == ')':
                while self.__temp and self.__temp[-1] != '(':
                    self.__push(self.__temp.pop())
                self.__temp.pop()
                lastItem = item
            else:
                while self.__temp and self.__temp[-1] != '(' and self.__hasLessOrEqualPriority(item, self.__temp[-1]):
                    self.__push(self.__temp.pop())
                if (item == '-' and idx == 0) or (item == '-' and lastItem == '(') or (item == '-' and lastItem in self.__binaryOperators):
                    self.__temp.append('_')
                    lastItem = '_'
                else:
                    self.__temp.append(item)
                    lastItem = item

        while self.__temp:
            self.__push(self.__temp.pop())
        
        print(self.__stack)
            
                
    def __hasLessOrEqualPriority(self, operator1, operator2):
        return self.__priority[operator1] <= self.__priority[operator2]


    def __push(self, item):
        self.__stack.append(item)


    def __pop(self):
        if not self.__isStackEmpty():
            return self.__stack.pop()
        else:
            raise Exception("Stack is empty.")


    def __peek(self):
        if not self.__isStackEmpty():
            return self.__stack[-1]
        return '$'


    def __isStackEmpty(self):
        return True if len(self.__stack) == 0 else False


    def __isOperand(self, item):
        return item.isdigit()