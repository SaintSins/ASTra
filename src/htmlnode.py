from typing import List, Dict, Optional
class HTMLNode:

    def __init__(self,tag: Optional[str] = None,value: Optional[str] = None,children: Optional[List['HTMLNode']] = None,props: Optional[Dict[str, str]] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("Nothing is implemented in child classes.")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        empty_str = ""
        for key,value in self.props.items():
            empty_str += f' {key}="{value}"'
        return empty_str
    
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):

    def __init__(self, value: str, tag: Optional[str] = None, props: Optional[Dict[str, str]] = None) -> None:
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: List['HTMLNode'], props: Optional[Dict[str, str]]=None) -> None:
        super().__init__(tag = tag, value = None, children = children, props = props)
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Tag is missing.")
        if not self.children:
            raise ValueError("Children doesn't contain any value.")
        parent_str = ""
        for c in self.children:
            parent_str += c.to_html()
        return f'<{self.tag}{self.props_to_html()}>{parent_str}</{self.tag}>'

    