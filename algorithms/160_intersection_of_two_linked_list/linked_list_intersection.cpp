/**
  * defintion for singly-linked list.
  * struct ListNode {
  *     int val;
  *     ListNode *next;
  *     ListNode(int x) : val(x), next(NULL) {}
  * };
  */
class Solution {
private:
    ListNode * p_A;
    ListNode * p_B;
    
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        p_A = headA;
        p_B = headB;
        while(p_A != p_B){
            if(p_A)
                p_A = p_A->next;
            else
                p_A = headB;
            
            if(p_B)
                p_B = p_B->next;
            else
                p_B = headA;
        }
        return p_A;
    }
};
