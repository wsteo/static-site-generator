import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if delimiter not in ["`", "*", "**"]:
        raise Exception("that is not an invalid markdown syntax")

    for node in old_nodes:
        if delimiter in node.text and node.text_type == TextType.TEXT:
            text_list = node.text.split(delimiter)
            for i in range(len(text_list)):
                if i % 2 == 1:
                    new_nodes.append(TextNode(text_list[i], text_type))
                else:
                    new_nodes.append(TextNode(text_list[i], TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
