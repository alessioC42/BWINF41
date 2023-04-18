class P: # P = Pancake
    def __init__(self, stack, history=[], initStack=[]):
        self.stack = stack
        self.history = history
        if(history == []): self.initStack = stack 
        else: self.initStack = initStack

    def flip(self, i):
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
        return P(self.stack[:], self.history[:], initStack=self.initStack)

    def getFlipIndexPoints(self):
        return list(range(0, len(self.stack)))

def flip_and_eat(stack, idx):
    stack[:idx+1] = reversed(stack[:idx+1])
    stack.pop(0)
    return stack

def reisverschluss(n):
    half = (n // 2)
    a = list(range(1, half+1))
    b = list(range(half+1, n+1))
    a.reverse()
    b.reverse()
    res = []
    for i in range(0, len(b)):
        res.append(b[i])
        try:
            res.append(a[i])
        except:
            return res
    return res

class Calc:
    def __init__(self, n, predictedPUWE):
        self.n = n
        self.predictedPUWE = predictedPUWE
        self.d = 0

    def main(self):
        print("\n\n----------------------------------------\nCALC:  P("+str(self.n)+")")
        

        num = reisverschluss(self.n)

        initStack = P(num, history=[])
        print("-- " + str(num)+ " --")

        print("PREDICT: "+str(self.predictedPUWE))


        for i in self.predictedPUWE:
            a = self.find(initStack, i)
            if a in self.predictedPUWE:
                return a

    def find(self, stack, wantedPUWE):
        stackPUWE = len(stack.history)
        if (stackPUWE<wantedPUWE):
            
            for i in stack.getFlipIndexPoints():
                newStack = stack.copy()
                newStack.flip(i)
                status = self.find(newStack, wantedPUWE)
                if status == -1:
                    continue
                elif status == wantedPUWE:
                    return wantedPUWE
        elif (stackPUWE == wantedPUWE):
            if (stack.isValid()):
                stack.printHistory()
                return stackPUWE
            else:
                return -1
        else:
            return -1

if __name__ == "__main__":
    
    last_predictedPUWE = [4, 5]
    for i in range(8, 101):
        calculator = Calc(i, last_predictedPUWE)
        puwe_i = calculator.main()
        last_predictedPUWE = [puwe_i, puwe_i+1, puwe_i+2]
