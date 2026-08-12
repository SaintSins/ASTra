import unittest
from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

        node3 = TextNode("This is an text node", TextType.ITALIC, "https://www.italics.com")
        node4 = TextNode("This is an text node", TextType.IMAGE, "https://imghost.com")
        self.assertNotEqual(node3,node4)

        node5 = TextNode("This is an text node", TextType.CODE, "https://www.code.com")
        node6 = TextNode("This is an text node", TextType.CODE, "https://www.code.com")
        self.assertEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()