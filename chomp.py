"""
Chompin' it up!
By Jasper
"""
import os
class conf:
    loss={(1,)}
    win={(1,1):(0,1)}
    def __init__(self,l=[]):
        #Each value in the tuple stands
        #for the length of each row in
        #the configuration, so not = 0
        self.data=l

    def winMove(self):
        if(tuple(self.data) in conf.loss):
            return None
        elif(tuple(self.data) in conf.win):
            return conf.win.get(tuple(self.data))
        else:
            for y,i in enumerate(self.data):
                for x in range(i):
                    if(x!=0 or y!=0):
                        temp=self.transform(x,y)
                        if(temp.winMove()==None):
                            conf.win[tuple(self.data)]=(x,y)
                            return (x,y)
            conf.loss.add(tuple(self.data))
            return None

    def winMoves(self):
        results = []
        if(tuple(self.data) in conf.loss):
            return None
        elif(tuple(self.data) in conf.win):
            return results.append(conf.win.get(tuple(self.data)))
        else:
            for y,i in enumerate(self.data):
                for x in range(i):
                    if(x!=0 or y!=0):
                        temp=self.transform(x,y)
                        if(temp.winMove()==None):
                            conf.win[tuple(self.data)]=(x,y)
                            results.append((x,y))
            if(len(results)==0):
                conf.loss.add(tuple(self.data))
                return None
            else:
                return results

    def transform(self,x,y):
        temp=[]
        for n,i in enumerate(self.data):
            if(n>=y and i>x):
                temp.append(x)
            else:
                temp.append(i)
        while(0 in temp):
            temp.remove(0)
        return conf(temp)

    def __str__(self):
        result=""
        for i in self.data:
            result+=i*"#"
            result+="\n"
        return result

    def load(self,loss,win):
        winf=open(win,'r')
        lossf=open(loss,'r')
        for i in lossf:
            line=tuple(i.split())
            conf.loss.add(line)
        lossf.close()
        for i in winf:
            pos=tuple(i.split()[0:1])
            val=tuple(i.split()[1:])
            conf.win[val]=pos
        winf.close()

    def save(self,loss,win):
        lossf=open(loss,'w')
        winf=open(win,'w')
        for i in conf.loss:
            temp=""
            for j in i:
                temp+=(str(j)+" ")
            temp+="\n"
            lossf.write(temp)
        lossf.close()
        for i in conf.win:
            temp=""
            for j in conf.win.get(i):
                temp+=(str(j)+" ")
            for j in i:
                temp+=(str(j)+" ")
            temp+="\n"
            winf.write(temp)
        winf.close()
            
                
                
            
                

def main():
    """
    print("Loading...")
    x=conf([1])
    x.load("loss.txt","win.txt")
    print("Done.")
    while(True):
        k=input("Configuration: ")
        if(k=="quit"):
            print("Saving...")
            x.save("loss.txt","win.txt")
            print("Done.")
            break
        else:
            try:
                lst=list(map(int,k.split()))
                x=conf(lst)
                print(x.winMove())
            except:
                print("Invalid")
    """
    x=conf([9,9,9,9])
    print(x.winMove())
    
main()
