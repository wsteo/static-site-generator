import unittest

from inline_markdown import *


class TestNodeConverter(unittest.TestCase):
    def test_split_delimiter_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        assert split_nodes_delimiter([node], "`", TextType.CODE) == output

    def test_split_delimiter_bold_block(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        assert split_nodes_delimiter([node], "**", TextType.BOLD) == output

    def test_split_delimiter_italic_block(self):
        node = TextNode("This is text with a *italic block* word", TextType.TEXT)
        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        assert split_nodes_delimiter([node], "*", TextType.ITALIC) == output

    def test_split_delimiter_code_multiple(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        node3 = TextNode("This is text with a *italic block* word", TextType.TEXT)

        new_nodes_list = split_nodes_delimiter(
            [node1, node2, node3], "`", TextType.CODE
        )
        new_nodes_list = split_nodes_delimiter(new_nodes_list, "**", TextType.BOLD)
        new_nodes_list = split_nodes_delimiter(new_nodes_list, "*", TextType.ITALIC)
        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        assert new_nodes_list == output

    def test_invalid_markdown_syntax(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], ".", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
