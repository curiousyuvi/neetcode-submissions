class Heap:
    def percolate_down(self,pairs,index):
        n=len(pairs)-1
        j=index
        while 2*j<=n:
                    # if swap with right child
                    if (2*j+1)<=n and pairs[2*j+1][1]>=pairs[2*j][1] and pairs[2*j+1][1]>pairs[j][1]:
                        temp=pairs[2*j+1]
                        pairs[2*j+1]=pairs[j]
                        pairs[j]=temp
                        j=2*j+1
                    # if swap with left child
                    elif pairs[2*j][1]>pairs[j][1]:
                        print("l")
                        temp=pairs[2*j]
                        pairs[2*j]=pairs[j]
                        pairs[j]=temp
                        j=2*j
                    else:
                        print("b")
                        break


    def heapify(self,pairs: List[tuple(int,int)]):
            pairs.append(pairs[0])

            pairs[0]=(-1,-1)

            n=len(pairs)-1

            i=n//2
            while i>=1:
                # percolate down
                self.percolate_down(pairs,i)

                i-=1

    def __init__(self,pairs):
        self.heap_pairs=pairs
        self.heapify(self.heap_pairs)

    def pop(self):
        
        n=len(self.heap_pairs)-1

        if n>1:
            result=self.heap_pairs[1]
            self.heap_pairs[1]=self.heap_pairs.pop()
            self.percolate_down(self.heap_pairs,1)
            return result
        else:
            return self.heap_pairs[1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht=[0]*2001

        for num in nums:
            ht[num+1000]+=1
            
        # (number , frequency) pair
        pairs=[]

        for i in range(2001):
            if ht[i]>0:
                pairs.append((i-1000,ht[i]))

        heap=Heap(pairs)

        output=[]

        for i in range(k):
            output.append(heap.pop()[0])
        
        return output






            
        
        


        