import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned_text = ''
    html_tag = True
    for symbol in html:
        if symbol == '<':
            html_tag = True
        elif symbol == '>':
            html_tag = False
        elif not html_tag:
            cleaned_text = cleaned_text + symbol
    cleaned_lines = []
    for line in cleaned_text.split('\n'):
        if line.strip():
            cleaned_lines.append(line)
    final_text = '\n'.join(cleaned_lines)
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)


delete_html_tags('draft.html', 'cleaned.txt')
