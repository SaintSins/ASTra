import unittest
from src.textnode import TextNode, TextType
from src.inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold_asterisk(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_multiple_blocks_asterisk(self):
        node = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    
    def test_delimiter_bold_chained_words_asterisk(self):
        node = TextNode("This is **a chained bold phrase** in the text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("a chained bold phrase", TextType.BOLD),
                TextNode(" in the text", TextType.TEXT),
            ]
        )
    
    def test_delim_bold_underscore(self):
        node = TextNode("This is text with a __bolded__ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_bold_multiple_blocks_underscore(self):
        node = TextNode("This is text with a __bolded__ word and __another__", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    
    def test_delimiter_bold_chained_words_underscore(self):
        node = TextNode("This is __a chained bold phrase__ in the text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("a chained bold phrase", TextType.BOLD),
                TextNode(" in the text", TextType.TEXT),
            ]
        )

    def test_delim_italic_asterisk(self):
            node = TextNode("This is text with an *italic* word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
            self.assertEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word", TextType.TEXT),
                ],
                new_nodes,
            )

    def test_delim_italic_multiple_blocks_asterisk(self):
        node = TextNode("This is text with an *italic* word and *another*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.ITALIC)
            ],
            new_nodes,
        )
    
    def test_delimiter_italic_chained_words_asterisk(self):
        node = TextNode("This is *a chained italic phrase* in the text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("a chained italic phrase", TextType.ITALIC),
                TextNode(" in the text", TextType.TEXT),
            ]
        )

    def test_delim_italic_underscore(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_italic_multiple_blocks_underscore(self):
        node = TextNode("This is text with an _italic_ word and _another_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.ITALIC),
            ],
            new_nodes,
        )
    
    def test_delimiter_italic_chained_words_underscore(self):
        node = TextNode("This is _a chained italic phrase_ in the text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("a chained italic phrase", TextType.ITALIC),
                TextNode(" in the text", TextType.TEXT),
            ]
        )
    
    
    def test_delimiter_consecutive_empty_bold_asterisk(self):
        node = TextNode("This is **** empty bold", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode(" empty bold", TextType.TEXT),
            ]
        )
    
    def test_delimiter_consecutive_empty_bold_underscore(self):
        node = TextNode("This is ____ empty bold", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode(" empty bold", TextType.TEXT),
            ]
        )

    def test_delimiter_consecutive_empty_italic_asterisk(self):
        node = TextNode("This is ** empty italic", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode(" empty italic", TextType.TEXT),
            ]
        )

    def test_delimiter_consecutive_empty_italic_underscore(self):
        node = TextNode("This is __ empty italic", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode(" empty italic", TextType.TEXT),
            ]
        )
    
    def test_delimiter_unclosed_bold_asterisk(self):
        node = TextNode("This is **unclosed bold text", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed.")

    def test_delimiter_unclosed_bold_underscore(self):
        node = TextNode("This is __unclosed bold text", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed.")

    def test_delimiter_unclosed_italic_asterisk(self):
        node = TextNode("This is *unclosed italic text", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed.")

    def test_delimiter_unclosed_italic_underscore(self):
        node = TextNode("This is _unclosed italic text", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed.")

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "This has an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual([("link", "https://boot.dev")], matches)
    
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows.", TextType.TEXT),
            ],
            new_nodes,
        )