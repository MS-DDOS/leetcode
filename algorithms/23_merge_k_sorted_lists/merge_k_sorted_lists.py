class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		minList = lists[0]
		minListIndex = 0
		for i in xrange(len(lists)):
			if lists[i][0].val < minList[0].val:
				minList = lists[i]
				minListIndex = i
		temp = lists[0]
		lists[0] = minList
		lists[minListIndex] = temp
		for llist in lists:
			print
			for node in llist:
				print node.val,
		'''
		counter = 0
		mergedList = []
		while True:
			for llist in lists:
		'''



if __name__ == "__main__":
	lists = [[ListNode(3), ListNode(4)],[ListNode(7), ListNode(10)],[ListNode(1), ListNode(10)]]
	y = Solution()
	y.mergeKLists(lists)
