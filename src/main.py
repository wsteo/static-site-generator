from textnode import *

node = TextNode("hello world", TextType.BOLD, "https://example.com")
print(node)


print(type(node))
leaf_node = text_node_to_html_node(node)
print(type(leaf_node))
