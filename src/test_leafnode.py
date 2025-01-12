import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_plaintext(self):
        leaf_node = LeafNode(None, "Hello World!")
        self.assertEqual(leaf_node.to_html(), "Hello World!")

    def test_to_html_all_None(self):
        leaf_node = LeafNode(None, None)
        self.assertRaises(ValueError, leaf_node.to_html)


if __name__ == "__main__":
    unittest.main()
