from enum import Enum
from typing import Optional
from src.htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text: str ,text_type: TextType ,url: Optional[str] = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
"""
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("Invalid markdown: link node must have a URL")
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("Invalid markdown: link node must have a URL")
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")
"""