from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != TextType.TEXT.value:
            new_nodes.append(node)
        else:
            temp_list = []
            text_split = node.text.split(delimiter)
            temp_list.extend(text_split)
            new_nodes.append(temp_list)

    # print(new_nodes)
    converted_nodes = []
    for new_node in new_nodes:
        if len(new_node) > 1:
            print(new_node)
            for i in range(len(new_node)):
                if i % 2 == 1:
                    converted_nodes.append(TextNode(new_node[i], text_type))
                else:
                    converted_nodes.append(TextNode(new_node[i], TextType.TEXT))
        else:
            converted_nodes.append(TextNode(new_node[0], TextType.TEXT))

    return converted_nodes


node1 = TextNode("This is text with a `code block` word", TextType.TEXT)

new_nodes_list = split_nodes_delimiter([node1], "`", TextType.CODE)
for node in new_nodes_list:
    print(node)
print("----------")
