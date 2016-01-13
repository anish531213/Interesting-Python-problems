from Deque import Deque

def using_deque_for_pallindrome(s):
    d = Deque()
    for i in s:
        d.add_rear(i)
    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
        return True

z = using_deque_for_pallindrome('roror')
print(z)
