import sys
'''from timeit import default_timer as timer'''
from time import sleep 


'''start = timer()
# ...
end = timer()
print(end - start)      '''

howlong = int(input('how much time would you like to play for \n suggested: \n for pros: 120 seconds \n for experienced: 150 seconds \n for begginers 180 seconds'))

class timer(howlong):
    def __init__(self):
        self.initial = howlong
    
    current = initial
    
    def current_time():
        return current


    def start_time():
        # timeit.timeit(howlong)
        for i in range(initial):
            if i > 0: 
                i -= 1
                current = i
                time.sleep(1)


userinputlist = []
def addtolist(userinput):
    isinlist = userinputlist.count(userinput)
    if isinlist != 0:
        print "that word has already been played!"
        break
    else: 
        userinputlist.append(userinput)




'''
check no doubles
def no_doubles(list):
    start_list = list
    wo_doubles = start_
    for i in range(list.length()):
        for w in range(list.length()):
            if list[i] == list[w] and i != w:
                list.remove(w) 
'''

class scoring(self):
    def __init__(self, word): 
        self.word = word
        self.score = 0

    def point_assign(self): 
        if len(self.word) <= 4:
            self.score+=1
        elif len(self.word) <= 5:
            self.score+=2
        elif len(self.word) <= 6:
            self.score+=3
        elif len(self.word) <= 7:
            self.score+=5
        elif len(self.word) >= 8:
            self.score+=11

print ('888                             888')         
print ('888                             888')         
print ('888                             888')         
print ('88888b.  .d88b.  .d88b.  .d88b. 888 .d88b.')
print ('888 "88bd88""88bd88P"88bd88P"88b888d8P  Y8b') 
print ('888  888888  888888  888888  88888888888888') 
print ('888 d88PY88..88PY88b 888Y88b 888888Y8b.')     
print ('88888P"  "Y88P"  "Y88888 "Y88888888 "Y8888')  
print('                     888     888')            
print ('                   Y8b   d88P')            
print ('               Y88P"  "Y88"')


print('insturctions: Boggle is just a simple word search game. The player gets three minutes to find as many words in the board that are longer than two letters. Words can only be created by touching tiles only and you can not use the same tile twice in the same word. ')