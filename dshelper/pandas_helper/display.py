img_tag_template = \
    '<img src="{src}" alt="{alt}" height="{height}" width="{width}">'
default_alt = "can't load image"
default_height = "100%"
default_width = "100%"
default_link_text = 'link'
a_tag_template = \
    '<a href="{src}">{text}</a>'

def create_img_html_tag_from_img_link(srcs,
                                      alts=None, heights=None, widths=None):
    n_link = len(srcs)
    if alts is None:
        alts = [default_alt] * n_link
    if heights is None:
        heights = [default_height] * n_link
    if widths is None:
        widths = [default_width] * n_link
    img_html_tag = [img_tag_template.format(
        src=srcs[i],
        alt=alts[i],
        height=heights[i],
        width=widths[i]
    ) for i in range(n_link)]
    return img_html_tag


def create_a_html_tag_from_link(srcs, texts=None):
    n_link = len(srcs)
    if texts is None:
        texts = [default_link_text] * n_link
    a_html_tag = [a_tag_template.format(
        src=srcs[i],
        text=texts[i]
    ) for i in range(n_link)]
    return a_html_tag
