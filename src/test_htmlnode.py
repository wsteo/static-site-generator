import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        node = HTMLNode(props={"href": "https://www.boot.dev"})
        expected = ' href="https://www.boot.dev"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(str(node), "tag=None, value=None, children=None, props=None")


if __name__ == "__main__":
    unittest.main()
