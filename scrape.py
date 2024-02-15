from re import compile, findall
from urllib.parse import urlparse

def extract(text, exclude=None):
    urls = findall(compile(r'https?://\S+|www\.\S+'), text)

    normalize = [urlparse(url)._asdict() for url in urls]

    for url in normalize:
        url['path'] = url['path'].split(',')[0].split('"')[0]

    if exclude:
        normalize = [url for url in normalize if exclude not in url['path']]

    return normalize

def main():

    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    urls = extract(text, exclude='board_thumbnail')
    with open("output.txt", 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(f"{url['scheme']}://{url['netloc']}{url['path']}\n")

if __name__ == "__main__":
    main()
