class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if not self.min:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack:MinStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); 
minStack.pop();
minStack.top();   
minStack.getMin(); 