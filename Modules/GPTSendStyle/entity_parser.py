from Modules.GPTSendStyle.imports import randint

class HTMLtags:
    bold = "<b>"
    italic = "<i>"
    block_code = "<blockquote>"

    #closed
    cbold = "</b>"
    citalic = "</i>"
    cblock_code = "</blockquote>"


def get_text_part(text, start, max_symbols_per_part= 60) -> int: 
    """
    return: offset (start + rand)
    """
    offset = 0
    rand = randint(0, max_symbols_per_part)

    stack_head = -1
    stack = []
    if (start+rand > len(text)):
        return len(text)
    
    for it in range(start, start + rand):
        if text[it] == "<":
            offset = it
            stack_head += 1
            stack.append(["<", offset])
        if text[it] == ">":
            if len(stack) == 0:
                pass
            else:
                stack.pop(stack_head)
                stack_head-=1
            offset = it
    if len(stack) == 0:
        offset=start + rand
    return offset


def get_tokens_stack(text, stack_tokens, start, end)-> str:
    start = start
    stack_tokens = stack_tokens[:]

    for it in range(start, end):
        if text[it] == "<":

            tag_type = text[it:it+2]
            
            if tag_type == "</":
                if len(stack_tokens) != 0:
                    stack_tokens.pop(-1)
            else:        
                short_tag = text[it:it+3]
                if short_tag == HTMLtags.bold:
                    stack_tokens.append([HTMLtags.bold, it+3])
                elif short_tag == HTMLtags.italic:
                    stack_tokens.append([HTMLtags.italic, it+3])
                else:
                    stack_tokens.append([HTMLtags.block_code, it+12])

    return stack_tokens


def get_tag_prefix_string(stack_tokens):
    tag_prefix = ""
    while len(stack_tokens) != 0:
        tag = stack_tokens.pop(-1)[0]
        if tag == HTMLtags.bold:
            tag_prefix += HTMLtags.cbold
        elif tag == HTMLtags.italic:
            tag_prefix += HTMLtags.citalic
        else:
            tag_prefix += HTMLtags.cblock_code
    return tag_prefix