from enum import Enum
from leafnode import LeafNode
from htmlnode import HTMLNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return (
            self.text == target.text
            and self.text_type == target.text_type
            and self.url == target.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception

    if text_node.text_type == TextType.TEXT:
        leaf_node = LeafNode(None, text_node.text)
        return leaf_node

    if text_node.text_type == TextType.BOLD:
        leaf_node = LeafNode("b", text_node.text)
        return leaf_node

    if text_node.text_type == TextType.ITALIC:
        html_node = HTMLNode("i", text_node.text)
        return html_node

    if text_node.text_type == TextType.CODE:
        html_node = HTMLNode("code", text_node.text)
        return html_node

    if text_node.text_type == TextType.LINK:
        html_node = HTMLNode(
            "a", text_node.text, children=None, props={"href": text_node.url}
        )
        return html_node

    if text_node.text_type == TextType.IMAGE:
        html_node = HTMLNode(
            "img",
            value=None,
            children=None,
            props={"src": text_node.url, "alt": text_node.text},
        )
        return html_node
