# I would consider this a hack. But technically the runtime is O(n log n). 
# It requires some extra memory but it runs faster than 98.69% of all python submissions
# Which is actually faster than my divide and conquer method

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        listall = []
        for listnode in lists:
            while listnode:
                listall.append(listnode)
                listnode = listnode.next
        listall.sort(key=lambda x: x.val)
        listall[-1].next = None
        for i in xrange(len(listall)-1):
            listall[i].next = listall[i+1]
        return listall[0]

if __name__ == "__main__":
    lists = [ListNode(3),ListNode(7),ListNode(1)]
    lists[0].next = ListNode(4)
    lists[1].next = ListNode(10)
    lists[2].next = ListNode(8)
    lists[2].next.next = ListNode(10)
    y = Solution()
    agg = y.mergeKLists(lists)
    while agg.next != None:
        print agg.val
        agg = agg.next
    print agg.val