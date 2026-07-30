class HistoryNode:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        page = HistoryNode(url, self.cur, None)
        self.cur.next = page
        self.cur = page
        

    def back(self, steps: int) -> str:
        cur = self.cur
        while cur.prev and steps > 0:
            steps -= 1
            cur = cur.prev
        
        self.cur = cur
        return cur.url

    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur.next and steps > 0:
            steps -= 1
            cur = cur.next
        
        self.cur = cur
        return cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)