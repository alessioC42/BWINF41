class P: # P = Pancake
    def __init__(self, stack, history=[], initStack=[]):
        self.stack = stack
        self.history = history
        if(history == []): self.initStack = stack 
        else: self.initStack = initStack

    def flip(self, i):
        """
        Flip the pancakes from position 0 to position i
        """
        stack = self.stack[:]
        for j in range((i + 1) // 2):
            stack[j], stack[i - j] = stack[i - j], stack[j]
        
        self.history.append(i)
        stack.pop(0)

        self.stack = stack[:]
    
    def printHistory(self):
        print("-- init_len:"+ str(len(self.initStack))+ "; flip_operations:"+ str(len(self.history))+ " --\n")
        print("-- : "+str(self.initStack))

        stack = P(self.initStack)
        for flipindex in self.history:
            stack.flip(flipindex)
            flipindex = str(flipindex)
            if (len(flipindex) ==1): flipindex+=" "
            print(str(flipindex)+" : "+str(stack.stack))

        print("PUWE: "+str(len(self.history)))

    def isValid(self):
        lst = list(self.stack)
        return all(lst[i] < lst[i+1] for i in range(len(lst)-1))
    
    def copy(self):
        return P(self.stack.copy(), self.history.copy(), initStack=self.initStack)

    def getFlipIndexPoints(self):
        return list(range(0, len(self.stack)))

def flip_and_eat(stack, idx):
    stack[:idx+1] = reversed(stack[:idx+1])
    stack.pop(0)
    return stack