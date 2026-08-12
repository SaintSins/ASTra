# The Ultimate AST Stress Test

Welcome to the production test environment. This document is designed to push your new recursive engine to its limits.

## 1. The Nesting Grounds

This paragraph tests how well your engine handles deep recursion. Here is a sentence with **bold text that suddenly contains _italic text_ inside of it**. We can also flip it and write _italic text that hides **bold text** within_. 

## 2. The Great Escape

Formatting is great, but sometimes you just want to talk about math like 5 \* 5 = 25. If the engine works, this literal \* asterisk and this literal \_ underscore will render perfectly in the HTML, without triggering any bold or italic tags. You can even print a backslash \\ without breaking the matrix.

## 3. Mixed Media

Let's see if the Hybrid Bridge correctly separates regex extraction from the recursive AST parser. 
Here is a [link to Boot.dev](https://boot.dev) sitting right next to an image: ![A cool placeholder](https://via.placeholder.com/150). 

What happens if we put a literal \* right next to a **bold tag**? It should handle both perfectly without swallowing the formatting.

## 4. Block Level Integration

* A standard list item.
* An item containing `inline code` and a \_literal underscore\_.
* An item with **bold text and _italic_ text**.

> "A recursive Abstract Syntax Tree is the difference between parsing text and understanding structure. Also, here is a literal \* just to make sure the quote block is using the escape map."