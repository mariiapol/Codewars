class Calculator(object):
    
    def evaluate(self, string):
        self.str = string.split()

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return x / y

        d_oper = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide           
        } 
              
        def oper(my_str):
            if ")" not in  my_str:
                i = 1
                while i < len(my_str)-1:
                    if my_str[i] == "*" or my_str[i] == "/":
                
                        my_str[i-1] = str(d_oper[my_str[i]](float(my_str[i-1]),float(my_str[i+1])))
                        my_str.pop(i+1)
                        my_str.pop(i)
                        continue
                    i+=1
        
                i = 1
                while i < len(my_str)-1:
                    if my_str[i] == "+" or my_str[i] == "-":
                
                        my_str[i-1] = str(d_oper[my_str[i]](float(my_str[i-1]),float(my_str[i+1])))
                        my_str.pop(i+1)
                        my_str.pop(i)
                        continue
                    i+=1
                return(my_str[0])
            
            else:
                for i in range(len(my_str)):
                    if my_str[i] == ")":
                        j = i-1
                        while j>=0:
                            if my_str[j] == "(":
                                my_str[j] = oper(my_str[j+1:i])
                                while j!= i:
                                    my_str.pop(i)
                                    i-=1
                                return oper(my_str)        
                            else:
                                j-=1
                        
        
        return float(oper(self.str))
