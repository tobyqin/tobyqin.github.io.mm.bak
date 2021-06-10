from datetime import datetime
from pathlib import Path

import yaml

TRANSLATE_EN = True


def translate_to_en(text):
    return text


class Blog:
    file = ''
    file_obj = Path()
    file_name = ''
    title = ''
    en_title = ''
    raw_content = ''
    content = ''
    date = datetime.now()
    front_formatter = None

    def __init__(self, markdown_file):
        if isinstance(markdown_file, Path):
            self.file_obj = markdown_file
            self.file = str(markdown_file)
        else:
            self.file = markdown_file
            self.file_obj = Path(self.file)

        if self.is_ready():
            self.collect()

    def is_ready(self):
        return self.file_obj.exists() \
               and not self.file_obj.name.startswith('!') \
               and not self.file_obj.name.startswith('！')

    def collect(self):
        self.file_name = self.file_obj.stem
        self.raw_content = self.file_obj.read_text(encoding='utf8')
        self.date = datetime.fromtimestamp(self.file_obj.stat().st_ctime).strftime('%Y-%m-%d')
        self._build_front_formatter()
        self._build_content()

    def generate_post(self):
        pass

    def generate_draft(self):
        pass

    def _try_get_front_formatter(self):
        if self.front_formatter:
            return self.front_formatter
        else:
            self.front_formatter = dict()

        start, end = -1, -1
        content_list = self.raw_content.split('\n')

        for index, line in enumerate(content_list):
            if line.strip() == '---' and start == -1:
                start = index
            elif line.strip() == '---' and end == -1:
                end = index
                break

        if end > start:
            yaml_content = '\n'.join(content_list[start + 1:end])
            self.front_formatter = yaml.safe_load(yaml_content)
            return True

    def _build_title(self, build_en=TRANSLATE_EN):
        if self._try_get_front_formatter():
            self.title = self.front_formatter['title']
        else:
            self.title = self.file_name
            self.front_formatter['title'] = self.title

        if build_en:
            self.en_title = translate_to_en(self.title)

    def _build_category(self, default='Thoughts'):
        if not 'categories' in self.front_formatter.keys():
            self.front_formatter['categories'] = [default, ]

    def _build_tags(self, default='life'):
        if not 'tags' in self.front_formatter.keys():
            self.front_formatter['tags'] = [default, ]

    def _build_date(self):
        pass

    def _build_layout(self, layout=''):
        if layout:
            self.front_formatter['layout'] = layout
        else:
            if 'layout' in self.front_formatter.keys():
                del self.front_formatter['layout']

    def _build_front_formatter(self):
        self._build_title()
        self._build_category()
        self._build_tags()
        self._build_layout()

    def _build_content(self):
        self._fix_images()

    def _fix_images(self):
        pass

    def as_dict(self):
        return {
            'file': self.file,
            'file_name': self.file_name,
            'title': self.title,
            'en_title': self.en_title,
            'date': self.date,
            'is_ready': self.is_ready(),
            'front_formatter': self.front_formatter,
            'content': self.content
        }

    def __str__(self):
        return self.file


class DraftManager:
    folder = '_drafts'
    blog_list = []

    def __init__(self):
        self.load()

    def load(self):
        for f in Path(self.folder).glob('*.md'):
            blog = Blog(f)
            if blog.is_ready():
                self.blog_list.append(Blog(f))

    def process(self):
        for blog in self.blog_list:
            print(blog.as_dict())


if __name__ == '__main__':
    dm = DraftManager()
    dm.process()
