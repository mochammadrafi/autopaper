import os

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar


def get_font_sizes(paragraph: LTTextContainer):
    """Get the font sizes for every LTChar element in this LTTextContainer"""
    return [
        char.size
        for line in paragraph
        for char in line
        if isinstance(char, LTChar)
    ]


def list_sized_paragraphs(page):
    """List all the paragraphs and their maximum font size on this page"""
    return [
        (max(get_font_sizes(paragraph)), paragraph.get_text())
        for paragraph in page
        if isinstance(paragraph, LTTextContainer)
    ]

exampleFile = os.listdir('files');
print(exampleFile)
for paper in exampleFile:
    content = []
    file_path = 'files/' + paper
    for page in extract_pages(os.path.expanduser(file_path)):
        content.append(max(list_sized_paragraphs(page)))

    print("The filename is: " + paper)
    print("The title of paper is: " + content[0][1])