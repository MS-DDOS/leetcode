class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		return self.divide(lists, 0, len(lists)-1)

	def divide(self, lists, start, end):
		if start > end:
			return None
		if start == end:
			return lists[start]
		mid = (start + end)/2
		first = self.divide(lists, start, mid)
		second = self.divide(lists,mid+1, end)
		return self.mergeTwoLists(first, second)

	def mergeTwoLists(self, list1, list2):
		head = ret = ListNode(-1)
		while (list1 != None) and (list2 != None):
			if list1.val <= list2.val:
				ret.next = list1
				list1 = list1.next
			else:
				ret.next = list2
				list2 = list2.next
			ret = ret.next
		if list1 == None:
			ret.next = list2
		else:
			ret.next = list1
		return head.next

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