from enum import Enum
from src.htmlnode import ParentNode, LeafNode, HTMLNode
from src.inline_markdown import text_to_children_nodes
from typing import List

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    HORIZONTAL_RULE = "horizontal_rule"
    
def markdown_to_blocks(markdown: str) -> List[str]:
    raw_blocks = markdown.split('\n\n')
    
    cleaned_blocks = []
    current_code_block = []
    in_code_block = False
    
    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block == "":
            continue
            
        if not in_code_block:
            if stripped_block.startswith("```") and not stripped_block.endswith("```"):
                in_code_block = True
                current_code_block.append(block)
            else:
                cleaned_blocks.append(stripped_block)
                
        else:
            current_code_block.append(block)
            if stripped_block.endswith("```"):
                in_code_block = False
                glued_block = "\n\n".join(current_code_block).strip()
                cleaned_blocks.append(glued_block)
                current_code_block = []
                
    if current_code_block:
        cleaned_blocks.append("\n\n".join(current_code_block).strip())
        
    return cleaned_blocks

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
        
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith("---"):
        return BlockType.HORIZONTAL_RULE
        
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered = True
    for line in lines:
        if not line.startswith(("- ", "* ")):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    counter = 1
    for line in lines:
        if not line.startswith(f'{counter}. '):
            is_ordered = False
            break
        else:
            counter += 1
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_nodes.append(text_to_paragraph_node(block))
            case BlockType.HEADING:
                html_nodes.append(text_to_heading_node(block))
            case BlockType.CODE:
                html_nodes.append(text_to_code_node(block))
            case BlockType.QUOTE:
                html_nodes.append(text_to_quote_node(block))
            case BlockType.UNORDERED_LIST:
                html_nodes.append(text_to_unlist_node(block))
            case BlockType.ORDERED_LIST:
                html_nodes.append(text_to_olist_node(block))
            case BlockType.HORIZONTAL_RULE:
                html_nodes.append(text_to_hr_node())
            case _:
                raise Exception("Invalid Block")
    return ParentNode("div", html_nodes)
 
def text_to_children(text: str) -> List[HTMLNode]:
    return text_to_children_nodes(text)
    
def text_to_paragraph_node(block: str) -> ParentNode:
    child_nodes = text_to_children(block)
    return ParentNode("p", child_nodes)

def text_to_heading_node(block: str) -> ParentNode:
    splited_block = block.split(" ",1)
    level = len(splited_block[0])
    if level < 1 or level > 6:
        raise Exception("Invalid heading level.")
    child_nodes = text_to_children(splited_block[1])
    return ParentNode(f'h{level}', child_nodes)

def text_to_unlist_node(block: str) -> ParentNode:
    lines = block.split("\n")
    list_items = []
    for line in lines:
        cleaned_text = line.split(" ",1)[1]
        child_node = text_to_children(cleaned_text)
        list_items.append(ParentNode("li", child_node))
    return ParentNode("ul", list_items)

def text_to_olist_node(block: str) -> ParentNode:
    lines = block.split("\n")
    list_items = []
    for line in lines:
        cleaned_text = line.split(" ",1)[1]
        child_node = text_to_children(cleaned_text)
        list_items.append(ParentNode("li", child_node))
    return ParentNode("ol", list_items)

def text_to_code_node(block: str) -> ParentNode:
    cleaned_text = block.strip("`").strip()
    code_node = LeafNode(tag="code", value=cleaned_text)
    return ParentNode(tag="pre", children= [code_node])

def text_to_quote_node(block: str) -> ParentNode:
    lines = block.split("\n")
    cleaned_str = []
    for line in lines:
        cleaned_text = line.lstrip(">").strip()
        cleaned_str.append(cleaned_text)
    child_node = text_to_children(" ".join(cleaned_str))
    return ParentNode("blockquote", child_node)

def text_to_hr_node() -> LeafNode:
    return LeafNode("","hr")

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("Title not found")