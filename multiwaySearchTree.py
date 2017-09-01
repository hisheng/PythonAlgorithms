# 多路搜索树

class Tree :
    def __init__(self,kids,next = None):
        self.kids = kids
        self.next = next



t = Tree(Tree(Tree("a",Tree('b',Tree('c',Tree('d'))))))

print(t.kids.next.next.val)