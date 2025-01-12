from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Object doesn't have a tag")

        if self.children == None:
            raise ValueError("Children has missing value")

        children_str = ""
        for child in self.children:
            children_str += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"
