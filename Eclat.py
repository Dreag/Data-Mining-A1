'''
Created on Oct 1, 2015

@author: KartikS
'''


import argparse;
import re
import sys
import time


F = []


class node():
    
    tids = []
    itemids = []
    
    
def genlevel1(file,minsup):
    
    lines = []
    item_dict = {}
    level1 = []
    
    for line in file:   
        lines.append(re.split(':|,',line)) 

    for line in lines:
        tid = line[0]
        
        for i in range(1,len(line)):
            ids = line[i]
            
            if ids in item_dict:
                l = item_dict[ids]
                l.append(tid)
                item_dict[ids] = l
                
            else:
                l = [] 
                l.append(tid)
                item_dict[ids] = l
    
    
    for k,v in item_dict.items():
        
        n = node()
        n.tids = [k]
        n.itemids = v
        if len(v)>= minsup:
            level1.appened(n)
        
    return level1
    
       
def eclat(P, minsup):
    
    for i in range(0,len(P)):
        n = P[i]
        F.append(n)
        P_temp =[]
        tids = set(n.tids)
        itemids = set(n.itemids)
        for j in range(i+1,len(P)):
            nn = P[j]
            nntid = set(nn.tid)
            nnitem = set(nn.itemids)
            
            setitems = itemids.union(nnitem) 
            settid = tids.intersection(nntid)
            
            if len(settid) >= minsup:
                nm = node()
                nm.tids = list(settid)
                nm.itemids = list(setitems)
                
                P_temp.append(nm)
                
        if P_temp:
            eclat(P_temp,minsup) 
            

def freq_items():
    
    file = open('Frequent Itemsets.txt','w')
    
    for i in range(len(F)):
        file.write( '{' + F[i] + '} : Sup = ' + len(F[i]) )

    file.close()

    
       
        
       
def main():
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    parser.add_argument("-s", "--Minsup", type = int)
    parser.add_argument("-c", "--MinConf")
    
    args = parser.parse_args()
    
    print( 'Arguments : ' + str(args) )
    
    if(len(sys.argv) < 3):
        print ("Please Provide the necessary arguments to proceed")
        SystemExit(1)
     
     
    min_sup = args.Minsup
    min_conf = args.MinConf

    file = open(args.file,'r')  
    start_time = time.time()
    level1 = genlevel1(file,min_sup)
    eclat(level1, min_sup)
        
    freq_items()
    
    print ("Time to Execute ECALT is : %s seconds " % (time.time() - start_time))
#   file.Close()
        
if __name__ == '__main__':
    main();
    


