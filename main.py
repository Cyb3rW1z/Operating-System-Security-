#!/usr/bin/python3
import time, sys
options=sys.argv
class PR:
    proc_count = 0
    total_count = 0
    total_bursts = 0
    total_idle = 0
    list_of_lists = []
    priorty1 = []
    priorty2 = []
    priority3 = []
    else_pro = []
    new_list = []
    start_time=[]
    start_time.append(int(0))
    startVals=0
    proc1 = 0
    proc2 = 0
    proc3 = 0
    proc4 = 0
    with open(options[3], "r") as f:
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)
    def CPU_Utalization(self):
        j = 3
        k = 0
        i = 0
        length = len(self.list_of_lists)
        for line in self.list_of_lists:
            if (self.list_of_lists[i][0] == 'proc'):
                self.proc_count = self.proc_count + 1
                self.new_list.append(self.list_of_lists[i])
            j = 3
            for z in range(len(line)):
                if (j >= int(len(line))):
                    if (self.list_of_lists[i][0] == 'idle'):
                        #print("idle Burst = ", self.list_of_lists[i][1])
                        self.total_idle = self.total_idle + int(self.list_of_lists[i][1])
                        #print("Total Bursts= ", self.total_bursts)
                    break
                if (self.list_of_lists[i][0] == 'proc'):
                    self.total_bursts = self.total_bursts + int(self.list_of_lists[k][j])
                    self.startVals=self.startVals+int(self.list_of_lists[k][j])
                    #print("proc with priority # ", self.list_of_lists[i][1], "Burst =", self.list_of_lists[k][j])
                    #print("Total Bursts =", self.total_bursts)
                    j = j + 1
            self.start_time.append(self.startVals)
            k = k + 1
            i = i + 1
        self.start_time=list(set(self.start_time))
        self.start_time.sort()
        return ( self.total_bursts/(self.total_bursts+self.total_idle))
    def AVG_TurnAroundTime(self):
        return(self.total_bursts/self.proc_count)

    def CPU_TimeLine(self):
        i=-1
        j=1
        for line in self.list_of_lists:
            i=i+1
            if (self.list_of_lists[i][0] == 'Done'):
                break
            if (self.list_of_lists[i][0] == 'idle'):
                #i=i+1
                continue
            if (int(self.list_of_lists[i][j]) == 1):
                if (self.list_of_lists[i][0] == 'proc'):
                    self.priorty1.append(line)
            elif (int(self.list_of_lists[i][j]) == 2):
                if (self.list_of_lists[i][0] == 'proc'):
                    self.priorty2.append(line)
            elif (int(self.list_of_lists[i][j]) == 3):
                if (self.list_of_lists[i][0] == 'proc'):
                    self.priority3.append(line)
            elif (int(self.list_of_lists[i][j]) > 3):
                if (self.list_of_lists[i][0] == 'proc'):
                    self.else_pro.append(line)
                    self.else_pro.sort()

        if(len(self.priorty1)):
            self.new_list.append(self.priorty1)
        if(len(self.priorty2)):
            self.new_list.append(self.priorty2)
        if(len(self.priority3)):
            self.new_list.append(self.priority3)
        if(len(self.else_pro)):
            self.new_list.append(self.else_pro)
        return self.new_list

    def Time_calc(self):
        i = 0
        j = 3
        self.new_list.sort()
        for line in self.new_list:
            j = 3
            for z in range(3, len(line)):
                if (i == 0):
                    self.proc1 = self.proc1 + int(self.new_list[i][z])
                if (i == 1):
                    self.proc2 = self.proc2 + int(self.new_list[i][z])
                if (i == 2):
                    self.proc3 = self.proc3 + int(self.new_list[i][z])
                if (i == 3):
                    self.proc4 = self.proc4 + int(self.new_list[i][z])
                j = j + 1
            i = i + 1
        self.proc2 = self.proc2 + self.proc1
        self.proc3 = self.proc3 + self.proc2
        self.proc4 = self.proc4 + self.proc3
        return

    def R_queue(self):
        new_listVals=[]
        new_listVals=self.start_time
        print(new_listVals)
        return new_listVals
        ''' 
        start_time=[]
        end_time=[]
        end=0
        start=0
        start_time.append(int(start))
        i=1
        j=3
        newlist=self.new_list
        newlist.sort()
        for line in newlist:
            j=3
            for val in range(3,len(line)):
                start=start+int(val)
                #end=end+line[j]
            start_time.append(start)
'''

class RR:
    proc_count = 0
    total_count = 0
    total_bursts = 0
    total_idle = 0
    list_of_lists = []
    priorty1 = []
    priorty2 = []
    priority3 = []
    else_pro = []
    new_list = []
    proc1=0
    proc2=0
    proc3=0
    proc4=0
    with open(options[3], "r") as f:
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)
    def CPU_Utalization(self):
        timeslice=options[2]
        j = 3
        k = 0
        i = 0
        length = len(self.list_of_lists)
        for line in self.list_of_lists:
            if (self.list_of_lists[i][0] == 'proc'):
                self.proc_count = self.proc_count + 1
                self.new_list.append(self.list_of_lists[i])
            j = 3
            for z in range(len(line)):
                if (j >= int(len(line))):
                    if (self.list_of_lists[i][0] == 'idle'):
                        #print("idle Burst = ", self.list_of_lists[i][1])
                        self.total_idle = self.total_idle + int(self.list_of_lists[i][1])
                        #print("Total Bursts= ", self.total_bursts)
                    break
                if (self.list_of_lists[i][0] == 'proc'):
                    self.total_bursts = self.total_bursts + int(self.list_of_lists[k][j])
                    #print("proc with priority # ", self.list_of_lists[i][1], "Burst =", self.list_of_lists[k][j])
                    #print("Total Bursts =", self.total_bursts)
                    j = j + 1
            k = k + 1
            i = i + 1
        return ( self.total_bursts/(self.total_bursts+self.total_idle))
    def AVG_TurnAroundTime(self):
        return(self.total_bursts/self.proc_count)
    def CPU_TimeLine(self):
        i = -1
        j = 1
        for line in self.list_of_lists:
            i = i + 1
            if (self.list_of_lists[i][0] == 'Done'):
                break
            if (self.list_of_lists[i][0] == 'idle'):
                # i=i+1
                continue
            self.new_list.append(line)
        return self.new_list
    def Time_calc(self):
        i=0
        j=3
        for line in self.new_list:
            j=3
            for z in range(3,len(line)):
                if (i == 0):
                    self.proc1 = self.proc1 + int(self.new_list[i][z])
                if (i == 1):
                    self.proc2 = self.proc2 + int(self.new_list[i][z])
                if (i == 2):
                    self.proc3 = self.proc3 + int(self.new_list[i][z])
                if (i == 3):
                    self.proc4 = self.proc4 + int(self.new_list[i][z])
                j=j+1
            i=i+1
        self.proc2=self.proc2+self.proc1
        self.proc3=self.proc3+self.proc2
        self.proc4=self.proc4+self.proc3
        return
    def R_queue(self):
        i=1
        j = 0
        newlist = []
        newlist = self.new_list
        for line in newlist:
            if(i==1):
                print("The proc waiting time is 0 ms for proc with number ",i)
                print("Priority number ", i, " is the following:", line)
            if (i == 2):
                print("The proc waiting time is",self.proc1," ms for proc with number ",i)
                print("Priority number ", i, " is the following:", line)
            if (i == 3):
                print("The proc waiting time is",self.proc2," ms for proc with number ",i)
                print("Priority number ", i, " is the following:", line)
            if (i == 4):
                print("The proc waiting time is",self.proc3," ms for proc with number ",i)
                print("Priority number ", i, " is the following:", line)

            i = i + 1
        return


if(options[1]=='PR'):
    obj1=PR()
    print("Input File Name: ",options[2])
    print("CPU Scheduling Algo.:",options[1])
    print("Total CPU utalization time in ms = ",obj1.CPU_Utalization())
    print("Average Turn Arond time in ms =" ,obj1.AVG_TurnAroundTime())
    obj1.Time_calc()
    obj1.R_queue()
    print("The CPU Timeline will work in the following format:")
    CPU_Timeline1=obj1.new_list
    chare = 'a'
    obj1.start_time=list(set(obj1.start_time))
    obj1.start_time.sort()
    index = 0
    index2=1
    for val in obj1.start_time:
        if(int(index2)>=len(obj1.start_time) or int(index)>=len(obj1.start_time)):
            break
        print(' %c(%d->%d) ' % (chare, obj1.start_time[index],obj1.start_time[index2]))
        index += 1
        index2+=1
        chare= chr(ord(chare) + 1)

    #for line in CPU_Timeline1:
   #     print(line)

if(options[1]=='RR'):
    obj2 = RR()
    print("Input File Name: ", options[3])
    print("CPU Scheduling Algo.:", options[1])
    print("Total CPU utalization time in ms = ", obj2.CPU_Utalization())
    print("Average Turn Arond time in ms =", obj2.AVG_TurnAroundTime())
    print("The CPU Timeline will work in the following format:")
    CPU_Timeline2=obj2.new_list
    for line in CPU_Timeline2:
        print(line)
    print("The Read Queue will look like:")
    obj2.Time_calc()
    obj2.R_queue()
