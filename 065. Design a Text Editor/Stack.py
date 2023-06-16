class TextEditor:

    def __init__(self):
        # Two Stacks
        
        # This will have the text on the left of the cursor
        self.leftStack = []
        
        # This will have the text on the right of the cursor
        self.rightStack = []

    def addText(self, text: str) -> None:
        # Add text to the leftStack
        # We will add character by character
        # So that it is easier to return when we want to return some portion
        for c in text: self.leftStack.append(c)
        

    def deleteText(self, k: int) -> int:
        # At any time, wherever the cursor is
        # The text on left of that cursor will always be in leftStack
        
        # And it is also possible that "k" is more than the size of leftStack
        # so, we also need to handle those scenarios
        # We can empty at most the whole leftStack
        k = min(k, len(self.leftStack))
        
        # Delete "k" elements
        n = k
        while n > 0:
            self.leftStack.pop()
            n -= 1
            
        # Return the number of elements deleted, that is, "k"
        return k
        

    def cursorLeft(self, k: int) -> str:
        # Return the characters
        return self.moveCursorAndReturnCharacters(k, self.leftStack, self.rightStack, True) 

    def cursorRight(self, k: int) -> str:
        # Return the characters
        return self.moveCursorAndReturnCharacters(k, self.leftStack, self.rightStack, False)
    
    def moveCursorAndReturnCharacters(self, k, leftStack, rightStack, isLeft):
        # When we move the cursor to left/right
        # It simply means, take the elements from top of leftStack/rightStack
        # And put then in rightStack/leftStack
        
        # Again, "k" might be larger than length of leftStack/rightStack
        # So that's also something we need to take care of
        n = min(k, len(self.leftStack) if isLeft else len(self.rightStack))
        
        
        while n > 0:
            if isLeft: self.rightStack.append(self.leftStack.pop())
            else: self.leftStack.append(self.rightStack.pop())
            n -= 1
        
        # Finally, we can figure out how many characters to return
        charactersToReturn = min(10, len(self.leftStack))
        startIdx = len(self.leftStack) - charactersToReturn
        
        # Return the characters
        return "".join(self.leftStack[startIdx:])
    


textEditor = TextEditor()
print(textEditor.addText("leetcode"));
print(textEditor.deleteText(4));
print(textEditor.addText("practice"));
print(textEditor.cursorRight(3));
print(textEditor.cursorLeft(8));
print(textEditor.deleteText(10));
print(textEditor.cursorLeft(2));
print(textEditor.cursorRight(6));






