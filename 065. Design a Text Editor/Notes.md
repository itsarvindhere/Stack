# PROBLEM STATMENET

Design a text editor with a cursor that can do the following:

 - Add text to where the cursor is.
 - Delete text from where the cursor is (simulating the backspace key).
 - Move the cursor either left or right.

When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

 - TextEditor() Initializes the object with empty text.
 - void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
 - int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
 - string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
 - string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.

# EXAMPLE

Input
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]

Output
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

# APPROACH

The code is commented so you can easily understand what each line does. In short, the "leftStack" will always have the characters to the left of the cursor.

It means, no matter if "cursorLeft" or "cursorRight" is called, the returned string will be from leftStack only.


