from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, preps=None):
        super().__init__(tag, value, None, preps)

    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
