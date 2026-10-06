class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


def build(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def show(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


sol = Solution()

list1 = build([2, 4, 3])
list2 = build([5, 6, 4])
show(sol.addTwoNumbers(list1, list2))

list1 = build([0])
list2 = build([0])
show(sol.addTwoNumbers(list1, list2))

list1 = build([9, 9, 9, 9, 9, 9, 9])
list2 = build([9, 9, 9, 9])
show(sol.addTwoNumbers(list1, list2))