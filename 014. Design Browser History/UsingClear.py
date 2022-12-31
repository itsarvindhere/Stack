class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.forwardHistory = []
        
        self.stack.append(homepage)

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.forwardHistory.clear()

    def back(self, steps: int) -> str:
        # As we move back in history, also keep pushing the urls in forward history
        # So that we don't lose track of them if we want to move forward
        print(steps, len(self.stack), self.stack)
        steps = min(steps, len(self.stack) - 1)
        while steps > 0:
            self.forwardHistory.append(self.stack.pop())
            steps -= 1
        
        # Return the current url
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.forwardHistory))
        while steps > 0:
            self.stack.append(self.forwardHistory.pop())
            steps -= 1
        
        # Return the current url
        return self.stack[-1]