class Calculator:
    def __init__(self):
        self.stack = []
        self.temp = []
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2}


    def calculate(self, expresion):
        self.__fillStack(expresion)
        result = self.__calculatePostfix()
        self.stack = []
        self.temp = []
        return result

    
    def __calculatePostfix(self):
        s = []
        
        for item in self.stack:
            if self.__isOperand(item):
                s.append(int(item))
            result = None
            if len(s) > 0:
                if item == '+':
                    result = s.pop() + s.pop()
                elif item == "-":
                    result = s.pop() - s.pop()
                elif item == "*":
                    result = s.pop() * s.pop()
                elif item == "/":
                    result = s.pop() / s.pop()
            if result is not None:
                s.append(result)

        return s.pop()


    def __fillStack(self, expresion):
        lastItem = ''
        for item in expresion:
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
                self.temp.append(item)
                lastItem = item
            elif item == ')':
                while self.temp and self.temp[-1] != '(':
                    self.__push(self.temp.pop())
                self.temp.pop()
                lastItem = item
            else:
                while self.temp and self.temp[-1] != '(' and self.__hasLessOrEqualPriority(item, self.temp[-1]):
                    self.__push(self.temp.pop())
                self.temp.append(item)
                lastItem = item

        while self.temp:
            self.__push(self.temp.pop())
            
                
    def __hasLessOrEqualPriority(self, operator1, operator2):
        print(operator1, operator2)
        return self.priority[operator1] <= self.priority[operator2]


    def __push(self, item):
        self.stack.append(item)


    def __pop(self):
        if not self.__isStackEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty.")


    def __peek(self):
        if not self.__isStackEmpty():
            return self.stack[-1]
        return '$'


    def __isStackEmpty(self):
        return True if len(self.stack) == 0 else False


    def __isOperand(self, item):
        return item.isdigit()