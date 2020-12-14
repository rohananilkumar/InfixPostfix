'''Code Written and debugged by ROHAN ANILKUMAR'''

class stack():
    _stack=list()
    top=-1
    def __init__(self,max):
        self._max=max
        
    def set_max(self,max):
        self._max=max
        
    def push(self,data):
        if(self.top==self._max-1):
            print("Stack Overflow")
        else:
            self._stack.append(data)
            self.top+=1
            #print(f"{data} pushed to stack; Top={self.top}")

    def pop(self):
        if(self.top==-1):
            print("Stack underflow")
        else:
            dele=self._stack.pop()
            self.top-=1
            #print(f"{dele} popped! Top={self.top}")
            return dele

    def display(self):
        for i in self._stack:
            print(i,end='\t')
            
    def getstack(self):
        res=''
        for i in self._stack:
            res+=i
        return res
    
    def peek(self):
        return self._stack[self.top]
    
def arithmetic(oper1,operator,oper2):
    if(operator=="+"):
        return oper1+oper2
    elif(operator=="-"):
        return oper1-oper2
    elif(operator=="*"):
        return oper1*oper2
    elif(operator=="/"):
        return oper1/oper2
    elif(operator=='**'):
        print("Power")
        return oper1**oper2

def evalpfix(op):
    '''Evaluates a postfix operation
        op is supposed to be a list of operands and operators
        operators are strings and operands are int/float
        eg: op=[2,8,'^']
        ==> res=256'''
    operations=op
    s=stack(len(operations))
    for i in operations:
        #print(i)
        if(type(i) in [int,float,complex] or i.isdigit()):
            s.push(float(i))
        else:
            oper1=s.pop()
            oper2=s.pop()
            
            result=arithmetic(oper2,i.replace("^","**"),oper1)
            s.push(result)
    if(s.top==0):
        return s.pop()
    else:
        return None

def greater(x,y):
    '''Precedence calculation
        Checks for x > y'''
    times=['*','/','%']
    plus=['+','-']
    if(x=='^'):
        return True
    if(x in times and y in plus):
        return True
    if(x in times and y in times):
        return True
    if(x in plus and y in plus):
        return True
    if(y in times and x in plus):
        return False
    if(y=='^'):
        return False
    
def expparse(exp):
    '''Changes expression to list so that further operations can be carried on smoothly
        exp should be a strings
        
        eg: exp='10*30^20'
        ==> res=[10,*,30,^,20]
        Note: Make sure that ** is given as ^
    '''
    res=[]
    i=0
    while i < (len(exp)):
        if(exp[i].isalnum()):
            dig=exp[i]
            i+=1
            while i<len(exp) and exp[i].isalnum():
                dig+=exp[i]
                i+=1
            res.append(dig)
        else:
            res.append(exp[i])
            i+=1
    return res

def topfix(exp):
    '''Converts infix(Human readable) expressions to postfix expressions
        eg: exp='2^8'
        res=[2,8,'^']
        Note: Make sure that ** is given as ^'''
    if(type(exp)==str):
        exp=expparse(exp)
    exp.insert(0,"(")
    exp.append(")")
    #exp=f"({exp})"
    res=[]
    #print(exp)
    s=stack(100)
    for i in exp:
        if(i=="("):
            s.push("(")
            
        elif(i.isalnum()):
            res.append(i)
            
        elif(i==")"):
            ele=s.pop()
            while ele!="(":
                res.append(ele)
                ele=s.pop()
        else:
            while(greater(s.peek(),i) or i==s.peek()):
                res+=s.pop()
                if(s.peek()=="("):
                    break
            s.push(i)
        print(i,s.getstack(),' '.join([str(x) for x in res]),sep="\t\t\t|\t\t\t")
    return res

def evaluate(exp):
    print("Converting expression to postfix expression...\n")
    pfix=topfix(exp)
    print("\nPosfix expression=",pfix)
    print("\nEvaluating Postfix operation...")
    res=evalpfix(pfix)
    print("Evaluated result=",res)
