class Calculator:
    def __init__(self):
        self.__postfix = []
        self.__temp = []
        self.__priority = {'+': 1, '-': 1, '_':1, '*': 2, '/': 2}
        self.__binaryOperators = ['+', '-', '*', '/']


    def calculate(self, expresion):
        self.__fillPostfix(expresion)
        result = self.__calculatePostfix()
        self.__postfix = []
        self.__temp = []
        return str(result)

    
    def __calculatePostfix(self):
        s = []
        
        for item in self.__postfix:
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


    def __fillPostfix(self, expresion):
        lastItem = ''
        for idx, item in enumerate(expresion):
            if self.__isOperand(item):
                lastItemInStack = self.__peekPostfix()
                if lastItemInStack != '$' and self.__isOperand(lastItemInStack) and self.__isOperand(lastItem):
                    lastItemInStack += item
                    self.__popPostfix()
                    self.__pushPostfix(lastItemInStack)
                    lastItem = item
                else:
                    self.__pushPostfix(item)
                    lastItem = item
            elif item == '(':
                self.__temp.append(item)
                lastItem = item
            elif item == ')':
                while self.__temp and self.__temp[-1] != '(':
                    self.__pushPostfix(self.__temp.pop())
                self.__temp.pop()
                lastItem = item
            else:
                while self.__temp and self.__temp[-1] != '(' and self.__hasLessOrEqualPriority(item, self.__temp[-1]):
                    self.__pushPostfix(self.__temp.pop())
                if (item == '-' and idx == 0) or (item == '-' and lastItem == '(') or (item == '-' and lastItem in self.__binaryOperators):
                    self.__temp.append('_')
                    lastItem = '_'
                else:
                    self.__temp.append(item)
                    lastItem = item

        while self.__temp:
            self.__pushPostfix(self.__temp.pop())
            
                
    def __hasLessOrEqualPriority(self, operator1, operator2):
        return self.__priority[operator1] <= self.__priority[operator2]


    def __pushPostfix(self, item):
        self.__postfix.append(item)


    def __popPostfix(self):
        if not self.__isPostfixEmpty():
            return self.__postfix.pop()
        else:
            raise Exception("Stack is empty.")


    def __peekPostfix(self):
        if not self.__isPostfixEmpty():
            return self.__postfix[-1]
        return '$'


    def __isPostfixEmpty(self):
        return True if len(self.__postfix) == 0 else False


    def __isOperand(self, item):
        return item.isdigit()