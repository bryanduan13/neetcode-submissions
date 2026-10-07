# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 =l1
        curr2 = l2
        carry = False
        prev = None
        while curr1 and curr2:
            prev = curr1
            curr1.val += curr2.val
            if carry:
                curr1.val+=1
                carry = False
            if curr1.val >= 10:
                curr1.val -=10
                carry = True
            curr1=curr1.next
            curr2=curr2.next
        if curr2 and not curr1:
            prev.next = curr2
            while curr2:
                prev2=curr2
                if carry:
                    curr2.val+=1
                    carry = False
                if curr2.val >=10:
                    curr2.val-=10
                    carry=True
                curr2=curr2.next
            if carry:
                carry = False
                prev2.next = ListNode(1)
            
        while curr1:
            prev=curr1
            if carry:
                curr1.val+=1
                carry = False
            if curr1.val >=10:
                curr1.val-=10
                carry=True
            curr1=curr1.next
        
        if carry:
            carry=False
            prev.next = ListNode(1)

        return l1
            