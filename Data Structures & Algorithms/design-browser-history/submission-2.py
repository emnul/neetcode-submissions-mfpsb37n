class HistoryNode:
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = HistoryNode(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        self.cur.next = HistoryNode(url, None, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:

        cur = self.cur
        while cur != self.head and steps > 0:
            cur = cur.prev
            steps -= 1
        self.cur = cur
        return cur.url
        

    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur.next and steps > 0:
            cur = cur.next
            steps -= 1
        self.cur = cur
        return cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)