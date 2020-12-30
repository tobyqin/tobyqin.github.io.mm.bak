from pathlib import Path


class Blog():
    def __init__(self, markdown_file):
        file = markdown_file
        title = ''
        en_title = ''
        slug = ''
        category = ''
        layout = ''
        tags = ''
        source_content = ''
        content = ''
        date = ''
        front_formatter = None

    def is_ready(self):
        pass

    def generate_post(self):
        pass

    def generate_draft(self):
        pass

    def _build_title(self):
        pass

    def _build_front_formatter(self):
        pass

    def _build_body(self):
        pass

    def _build_images(self):
        pass


class DraftManager():

    def __init__(self):
        self.load()

    def load(self):
        pass

    def process(self):
        pass


if __name__ == '__main__':
    dm = DraftManager()
    dm.process()
