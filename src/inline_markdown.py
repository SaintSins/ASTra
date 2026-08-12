from src.textnode import TextNode, TextType
from src.htmlnode import ParentNode, LeafNode
from re import findall
from typing import List, Tuple
from src.escape_handlers import hide_escape_chars, restore_string, escape_map

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        splited_node = node.text.split(delimiter)
        if len(splited_node)%2 == 0: #Length of the splitted node will be in odd number if closing delimeter is present
            raise Exception("Invalid markdown, formatted section not closed.")
        for i, part in enumerate(splited_node):
            if i % 2 == 0:
                if part != "":
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                if part != "":
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str,str]]:
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

def extract_markdown_links(text: str) -> List[Tuple[str,str]]:
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_img = extract_markdown_images(node.text)
        if not extracted_img:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for img_alt, img_link in extracted_img:
            markdown_str = f'![{img_alt}]({img_link})'
            splited_node_img = remaining_text.split(markdown_str,1)
            if splited_node_img[0] != "":
                new_nodes.append(TextNode(splited_node_img[0], TextType.TEXT))
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_link))
            remaining_text = splited_node_img[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_link = extract_markdown_links(node.text)
        if not extracted_link:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for link_text, link_url in extracted_link:
            markdown_str = f'[{link_text}]({link_url})'
            splited_node_link = remaining_text.split(markdown_str,1)
            if splited_node_link[0] != "":
                new_nodes.append(TextNode(splited_node_link[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = splited_node_link[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def parse_inline_to_ast(text: str) -> list:
    if not text:
        return []

    delimiters = [
        ("**", "b"),
        ("__", "b"),
        ("*", "i"),
        ("_", "i"),
        ("`", "code")
    ]

    first_delim = None
    first_idx = len(text)
    first_tag = None

    for delim, tag in delimiters:
        idx = text.find(delim) 
        if idx != -1 and idx < first_idx:
            first_idx = idx
            first_delim = delim
            first_tag = tag

    if first_delim is None:
        clean_text = restore_string(text, escape_map)
        return [LeafNode(tag=None, value=clean_text)]

    closing_idx = text.find(first_delim, first_idx + len(first_delim))
    if closing_idx == -1:
        raise ValueError(f"Invalid Markdown: Unclosed '{first_delim}' tag.")

    before_text = text[:first_idx]
    inside_text = text[first_idx + len(first_delim) : closing_idx]
    after_text = text[closing_idx + len(first_delim) :]

    nodes = []

    if before_text:
        nodes.extend(parse_inline_to_ast(before_text))

    if inside_text:
        assert first_tag is not None
        inside_children = parse_inline_to_ast(inside_text)
        nodes.append(ParentNode(tag=first_tag, children=inside_children))

    if after_text:
        nodes.extend(parse_inline_to_ast(after_text))

    return nodes

def text_to_children_nodes(text: str) -> list:
    safe_text = hide_escape_chars(text, escape_map)
    
    nodes = [TextNode(safe_text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    final_html_nodes = []
    
    for node in nodes:
        if node.text_type == TextType.TEXT:
            final_html_nodes.extend(parse_inline_to_ast(node.text))
            
        elif node.text_type == TextType.IMAGE:
            clean_alt = restore_string(node.text or "", escape_map)
            clean_url = restore_string(node.url or "", escape_map)
            
            final_html_nodes.append(
                LeafNode(value="", tag="img", props={"src": clean_url, "alt": clean_alt})
            )
            
        elif node.text_type == TextType.LINK:
            clean_text = restore_string(node.text or "", escape_map)
            clean_url = restore_string(node.url or "", escape_map)
            
            final_html_nodes.append(
                LeafNode(value=clean_text, tag="a", props={"href": clean_url})
            )

    return final_html_nodes