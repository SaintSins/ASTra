import unittest
from src.htmlnode import LeafNode, ParentNode
from src.inline_markdown import parse_inline_to_ast, text_to_children_nodes

class TestInlineMarkdown(unittest.TestCase):
    
    def test_parse_pure_text(self):
        text = "Just normal text"
        nodes = parse_inline_to_ast(text)
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].value, "Just normal text")
        self.assertEqual(nodes[0].tag, None)

    def test_parse_single_tag(self):
        text = "This is **bold** text"
        nodes = parse_inline_to_ast(text)
        
        self.assertEqual(len(nodes), 3)
        
        # "This is "
        self.assertEqual(nodes[0].value, "This is ")
        
        # "**bold**" -> ParentNode(b) -> LeafNode(bold)
        self.assertEqual(nodes[1].tag, "b")
        self.assertEqual(len(nodes[1].children), 1)
        self.assertEqual(nodes[1].children[0].value, "bold")
        
        # " text"
        self.assertEqual(nodes[2].value, " text")

    def test_parse_nested_tags(self):
        text = "This is **bold and _italic_**"
        nodes = parse_inline_to_ast(text)
        
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].value, "This is ")
        
        # The outer Bold node
        bold_node = nodes[1]
        self.assertEqual(bold_node.tag, "b")
        self.assertEqual(len(bold_node.children), 2)
        
        # Inside the Bold node: "bold and "
        self.assertEqual(bold_node.children[0].value, "bold and ")
        
        # Inside the Bold node: The nested Italic node
        italic_node = bold_node.children[1]
        self.assertEqual(italic_node.tag, "i")
        self.assertEqual(italic_node.children[0].value, "italic")

    def test_unclosed_tag_raises_error(self):
        text = "This is **unclosed bold"
        with self.assertRaises(ValueError):
            parse_inline_to_ast(text)

    def test_hybrid_bridge_with_escapes_and_links(self):
        # Testing the full pipeline: escapes + regex extractors + AST engine
        text = r"This is \*\*escaped\*\* and [a link](https://boot.dev)"
        nodes = text_to_children_nodes(text)
        
        self.assertEqual(len(nodes), 2)
        
        # The text node should have its literal asterisks restored!
        self.assertEqual(nodes[0].value, "This is **escaped** and ")
        self.assertEqual(nodes[0].tag, None)
        
        # The link node should be properly constructed
        self.assertEqual(nodes[1].tag, "a")
        self.assertEqual(nodes[1].value, "a link")
        self.assertEqual(nodes[1].props["href"], "https://boot.dev")

if __name__ == "__main__":
    unittest.main()