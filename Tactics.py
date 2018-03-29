import collections
from operator import itemgetter

def tactics(hand, times):
   # <param name=“hand”>手札</param>
   # <param name=“times”>回数</param>
   # <returns>変更するカード番号を返す</returns>

   handdict={}
   numlist = []
   suitlist = []
   change = []

   print(hand)
   for i in range(len(hand)):
       numlist.append(hand[i].num)
       suitlist.append(hand[i].suit)

   numdict = collections.Counter(numlist)
   suitdict = collections.Counter(suitlist)

   #####
   for i,j in enumerate(numlist):
       handdict[i] = j
   handdict = sorted(handdict.items(), key=lambda x:x[1])
   print(handdict)


   i=0
   while(i<4 and times <= 5):
       print(i)
       if(i==2):
           if(handdict[3][1] - handdict[4][1] != 1):
               return max(handdict.items(), key=lambda x:x[1])[0]
       if(i==3):
           return []

       if(handdict[i][1] - handdict[i+1][1]) == 1:
           i+=1
       else:
           break
    #####
    
   for c in numdict.items():
       if(c[1] == 1):
           i = 0
           for h in numlist:
               if(c[0] == h):
                   change.append(i)
               i += 1

   print(change)
   return change
