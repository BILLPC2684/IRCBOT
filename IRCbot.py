import time,socket
def sleep(s):
    time.sleep(s)
from _thread import *
global Nick,log_autotalk
Nick="TheRedGamer2684"
IP="irc.openredstone.org"
Port=6667
Channel="#openredstone"#"#bottesting"#
log_autotalk=["PRIVMSG nickserv identify 2684","PRIVMSG "+Channel+" TESTBOT loaded!"]
secs=10

#Channel = ""
#IRCread = ""
def takeWhile(String, predicate):
    ret = ""
    for char in String:
        if predicate(char) :
            ret += char
        else :
            return ret
def dropWhile(String, predicate):
    ret = ""
    dropped = True
    for char in String:
        if predicate(char) & dropped == True:
            pass
        else :
            dropped = False
        if dropped == False :
            ret += char
    return ret

class BOT(object):
    def __init__(self, Name, Server, Port):
        super(BOT, self).__init__()
        self.Name = Name
        self.Server = Server
        self.Port = Port
        self.sock = socket.socket()
        self.chan = ""
        self.buff = ""
        
    def sendRaw(self, raw):
        self.sock.send(bytes(raw,"UTF-8"))
        
    def sendMSG(self, msg):
      	self.sendRaw("PRIVMSG "+msg+"\r\n")
        
    def send(self, msg, Chan):
      	self.sendRaw("PRIVMSG "+Chan+" "+msg+"\r\n")
        
    def Connect(self):
        self.sock.connect((self.Server,self.Port))
        self.sendRaw("NICK %s\r\n" %self.Name)
        self.sendRaw("USER %s %s Bot :%s\r\n" %(self.Name, self.Name, self.Name))
        
    def Join(self, Chan):
        self.chan = Chan
        self.sendRaw("JOIN %s\r\n" % Chan)
        self.Listen(Chan)
        
    def PING(self, msg):
        self.sendRaw("PONG %s\r\n" % msg)
        
    def startup(self):
        global sleep,log_autotalk,secs
        sleep(secs)
        for i in len(range(log_autotalk)):
            self.sendRaw(log_autotalk[i])
        
    def btl(self,string):
          l=[]
          print(string,len(string))
          for i in range(len(string)):
           print(i)
           try:
            l.append(int(string[i]))
           except ValueError:
            break
          return l
    def ALU(self,A,B,IA,IB,Cin,OR,FC):
         try:u
          preC,Carry,C=[0 for i in range(len(A)+1)],[0 for i in range(len(A)+2)],[0 for i in range(len(A)+1)]
          for i in range(len(A)):
           if IA:
            if A[i] == 1:
                A[i] = 0
            else:
                A[i] = 1
           if IB:
            if B[i] == 1:
                B[i] = 0
            else:
                B[i] = 1
          A=[0]+A
          B=[0]+B
          print(A,B)
          if Cin or FC:
           Carry[len(A)]=1
          else:
           Carry[len(A)]=0
          i=len(A)-1
          while i != 0:
           if (A[i]&B[i])==1:
            if not OR:
             Carry[i]=1
            else:
             preC[i]=1
           elif (A[i]|B[i])==1:
            preC[i]=1
           if FC:
            Carry[i]=1
           if (preC[i]&Carry[i+1])==1:
            Carry[i]=1
           elif (preC[i]|Carry[i+1])==1:
            C[i]=1
           i-=1
          i=0
          out=''
          while i != len(A):
           if i != 0:
            out=str(out)+str(C[i])
           i+=1
          return out
         except IndexError:
          return 'a error was found, do you have a and b the same length?'
    def fib(self,n,Chan):
        o=[0,1]
        p=0
        out=''
#        if n > 16:
#            n=16
        for i in range(n):
          if p==0:
            o[0]+=o[1]
            out=out+str(o[0])+"_"
            p=1
          elif p==1:
            o[1]+=o[0]
            out=out+str(o[1])+"_"
            p=0
          #sleep(0.1)
        self.sendMSG(Chan+" "+out)
    def Listen(self,Chan):
      global Nick,br
      #start_new_thread(self.startup,())
      logged=0
      while True:
        self.buff = self.buff+self.sock.recv(1024).decode("UTF-8")
        temp = self.buff.lstrip(":")
        #forward = takeWhile(temp, lambda c: c!="!")
        #endward = dropWhile(temp, lambda c: c!=":").lstrip(":")
        #print("%s %s" % (forward, endward))
        #User = ""
        Message = temp#forward, endward
        #User = str(forward)
        #User = str.split(User)
        #users = User in sudousers
        #Message = str(endward)
        #Message = str.split(Message)
        curln = str.split(self.buff, "\n")
        self.buff = curln.pop()
        for line in curln:
            line = str.rstrip(line).split()
            I=0
            if line[0] == "PING":
                self.PING((line[1]))
            elif line[0] == "None" or line[0] == "NONE":
                self.PING((line[1]))
            else:
                #print(line)
                for k in range(len(line)):
                    temp=''
                    for i in line[k]:
                     if i!=":" and i!="!" and i!=".":
                      temp=str(temp)+i
                     if i=="!" or i==".":
                      break
                    line[k]=temp
                br=0
                print(line)#['OREBuild', 'PRIVMSG', '#openredstone', 'BILLPC2684', 'test']
                if line[0]=="OREBuild" or line[0]=="ORESchool" or line[0]=="ORESurvival":
                    Chan=str(line[0])+" /msg "+str(line[3])
                else:
                    Chan=line[0]
                #while parts[p]!="!" or parts[p]!=".":# p!=len(line[0]-1):
                    #if parts[p]!="!" or parts[p]!=".":# p!=len(line[0]-1):
                        #user+str(user)+parts[p]
                    #p+=1
                    #try:
                        #if parts[p]!="!" or parts[p]!=".":
                            #sleep(0)
                    #except IndexError:
                        #break
                #print(user)
                for i in line:
                    if i == "hello" or i == "hi" or i == "hola" or i == "hey" or i == "hya" or i == "hia" or i == "moshi-moshi" or i == "moshi-moshi(hello)" or i == "welcome" or i == "Welcome" or i == "WELCOME":
                        for j in line:
                            if j == Nick:
                                self.sendMSG(Chan+" moshi-moshi(hello)")
                                br=1
                                break
                    elif i == "*login":
                        if logged==1:
                            self.sendMSG(Chan+" TestBot is already logged in")
                        elif logged==0:
                            self.sendMSG("NickServ identify 2684")
                            sleep(2)
                            self.sendMSG(Chan+" TestBot logged in")
                            logged=1
                    elif i == "*info":
                        self.sendMSG(Chan+" TestBot: a Bot for testing, Mode:IRC")
                        self.sendMSG(Chan+" For eny help type *help .")
                        self.sendMSG(Chan+" IRC system from VoltzLive, Bot from BILLPC2684.")
                    elif i == "*help":
                        for j in line:
                            if j == "commands":
                                self.sendMSG(Chan+" Commands: *info, *help, *fib, *add, *sub, *and, *or, *xor(don't work that well...)")
                                br=1
                                break
                            elif j == "info":
                                self.sendMSG(Chan+" info: displays info of the bot.")
                                br=1
                                break
                            elif j == "fib":
                                self.sendMSG(Chan+" usage: *fib <cycles>")
                                self.sendMSG(Chan+" fib: prints to you the cycles of fibonacci.")
                                br=1
                                break
                        if br==0:
                            self.sendMSG(Chan+" usage: *help <topic>")
                            self.sendMSG(Chan+" Toppics: commands, info, fib")
                            br=1
                    elif i == "*fib":
                        temp=i
                    elif temp == "*fib":
                        temp=""
                        try:
                            start_new_thread(self.fib,(int(i),Chan,))
                        except ValueError as err:
                            self.sendMSG(Chan+" -error: got '"+str(err)+"' when expecting int(number)...")
                            self.sendMSG(Chan+" usage: *fib <how many times to loop>")
                    elif i == "*add":
                        temp=i
                        temp2=''
                    elif temp == "*add" and temp2 == '':
                        temp2=i
                    elif temp == "*add" and temp2 != '':
                           self.sendMSG(Chan+" "+str(self.ALU(self.btl(temp2),self.btl(i),0,0,0,0,0)))
                    elif i == "*sub":
                        temp=i
                        temp2=''
                    elif temp == "*sub" and temp2 == '':
                        temp2=i
                    elif temp == "*sub" and temp2 != '':
                           self.sendMSG(Chan+" "+str(self.ALU(self.btl(temp2),self.btl(i),0,1,1,0,0)))
                    elif i == "*and":
                        temp=i
                        temp2=''
                    elif temp == "*and" and temp2 == '':
                        temp2=i
                    elif temp == "*and" and temp2 != '':
                           self.sendMSG(Chan+" "+str(self.ALU(self.btl(temp2),self.btl(i),1,1,1,1,1)))
                    elif i == "*or":
                        temp=i
                        temp2=''
                    elif temp == "*or" and temp2 == '':
                        temp2=i
                    elif temp == "*or" and temp2 != '':
                           self.sendMSG(Chan+" "+str(self.ALU(self.btl(temp2),self.btl(i),0,0,0,1,0)))
                    elif i == "*xor":
                        temp=i
                        temp2=''
                    elif temp == "*xor" and temp2 == '':
                        temp2=i
                    elif temp == "*xor" and temp2 != '':
                           self.sendMSG(Chan+" "+str(self.ALU(self.btl(temp2),self.btl(i),0,1,0,0,1)))
                    if br==1:
                        break
def main():
    bot1 = BOT(Nick,IP,Port)
    bot1.Connect()
    sleep(5)
    bot1.Join(Channel)
#input()
main()
