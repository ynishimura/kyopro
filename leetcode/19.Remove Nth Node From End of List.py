# https://qiita.com/happyisland44/items/ac516aad49809caf74ea
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0) # はじめの値を取り出すためにダミーをつくる
        dummy.next = head
        fast = slow = dummy
        for _ in xrange(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

s = Solution()
h = [1,2,3,4,5]
n = 2
print(s.removeNthFromEnd(h,n))