# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        nodeA = head
        nodeB = head.next

        if head.next.next == None:
            nodeA.next = None
            nodeB.next = nodeA
            return nodeB

        temp = nodeB.next
        nodeA.next = None # Unlink first node because it is now the last node
        while temp != None:
            temp = nodeB.next
            nodeA = self.swap_parent(nodeA, nodeB)
            nodeB = temp
        return nodeA
    
    def swap_parent(self, nodeA, nodeB):
        nodeB.next = nodeA
        return nodeB

if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    
    x = Solution()

    temp = node
    while temp != None:
        print temp.val
        temp = temp.next

    print "Reversing..."
    temp = x.reverseList(node)

    while temp != None:
        print temp.val
        temp = temp.next