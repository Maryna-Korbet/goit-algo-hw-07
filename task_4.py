# Implement a data structure for the comments system so that comments can have replies, 
# which in turn can have replies, thus forming a hierarchical structure.

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This comment has been deleted."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)


if __name__ == "__main__":
    root_comment = Comment("What a wonderful book!", "Bogdan")
    reply1 = Comment("The book is a complete disappointment :(", "Andrii")
    reply2 = Comment("What's great about it?", "Maryna")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Not a book, but they translated a bunch of paper for nothing...", "Sergey")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    # Display the comments structure
    root_comment.display()