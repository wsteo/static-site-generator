import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode


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

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), LeafNode)
        assert html_node.tag == None
        assert html_node.value == "This is a text node"
        assert html_node.props == None

        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), LeafNode)
        assert html_node.tag == "b"
        assert html_node.value == "This is a text node"
        assert html_node.props == None

        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), HTMLNode)
        assert html_node.tag == "i"
        assert html_node.value == "This is a text node"
        assert html_node.props == None

        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), HTMLNode)
        assert html_node.tag == "code"
        assert html_node.value == "This is a text node"
        assert html_node.props == None

        node = TextNode("link", TextType.LINK, "https://example/com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), HTMLNode)
        assert html_node.tag == "a"
        assert html_node.value == "link"
        assert html_node.props == {"href": "https://example/com"}

        node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(type(html_node), HTMLNode)
        assert html_node.tag == "img"
        assert html_node.value == None
        assert html_node.props == {"src": "image.jpg", "alt": "Alt text"}


if __name__ == "__main__":
    unittest.main()
