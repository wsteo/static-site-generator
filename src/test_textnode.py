import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example/com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://example/com")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example/com")
        node2 = TextNode("This is a text", TextType.ITALIC, "http://example/com")
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example/com")
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example/com")
        node2 = TextNode("This is a text node", TextType.TEXT, "http://example/com")
        self.assertNotEqual(node, node2)

    def test_TEXT_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(type(converted_node), LeafNode)

    def test_BOLD_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.BOLD)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(type(converted_node), LeafNode)


if __name__ == "__main__":
    unittest.main()
