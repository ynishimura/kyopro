class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '{': '}',
            '[':']',
            '<':'>',
            '(':')'
        }
        stack = []
        for char in s:
            if char in lookup.keys():
                stack.append(lookup[char]) # stackに閉じる記号を追加
            if char in lookup.values():
                if not stack:
                    return False # stackなにもないとき成り立たない
                if char != stack.pop():
                    return False # stackからpopできないときも成り立たない
        if stack:
            return False # 最後にstackになにか残ってたら成り立たない
        return True


if __name__ == '__main__':
    s = "()[]{}"
    p = Solution()
    r = p.isValid(s)
    print(r)
