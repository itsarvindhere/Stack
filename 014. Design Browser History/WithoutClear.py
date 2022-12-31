class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.forwardHistory = []
        
        # So that if we visit a new url, we avoid running clear() on the stack which is an O(N) operation
        self.forwardHistorySize = 0
        
        self.stack.append(homepage)

    def visit(self, url: str) -> None:
        self.stack.append(url)
        
        # Save the current size of forwardHistory stack
        self.forwardHistorySize = len(self.forwardHistory)
        
        # Avoid using clear()
        # self.forwardHistory.clear()

    def back(self, steps: int) -> str:
        # If you can only return x steps in the history and steps > x, you will return only x steps
        # Here, x simply means how many pages are there before current page. Or in other words, (length of stack - 1)
        steps = min(steps, len(self.stack) - 1)
        
        # As we move back in history, also keep pushing the urls in forward history
        # So that we don't lose track of them if we want to move forward
        while steps > 0:
            self.forwardHistory.append(self.stack.pop())
            steps -= 1
        
        # Return the current url (top of stack)
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        # If you can only forward x steps in the history and steps > x, you will forward only x steps.
        # Here, x simply means how many pages are there after current page. Or in other words, length of "forwardHistory" stack
        steps = min(steps, len(self.forwardHistory) - self.forwardHistorySize)
        
        while steps > 0:
            self.stack.append(self.forwardHistory.pop())
            steps -= 1
        
        # Return the current url (top of stack)
        return self.stack[-1]
        