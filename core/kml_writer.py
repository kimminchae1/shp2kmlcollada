import os

# template.kml 파일 내용을 문자열로 읽기
def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_kml(output_path, template, data):
    content = template.format(**data)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)