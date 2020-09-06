class Post:

    def __init__(self, post_id, author, post_time, title, tags, preview_text):
        self.post_id = post_id
        self.author = author
        self.post_time = post_time
        self.title = title
        self.tags = tags
        self.preview_text = preview_text

    def to_str(self):
        return f"Автор статьи - {self.author}\nНазвание статьи - {self.title}\n\n{self.preview_text}"

    @classmethod
    def from_bs_tag(cls, tag_object):
        post_id = tag_object['id'].split('post_')[1]
        author = tag_object.find('span', class_='user-info__nickname').text
        post_time = tag_object.find('span', class_='post__time').text
        title = tag_object.find('h2', class_='post__title').text.replace('\n', '')
        tags = list(map(
            lambda tag: tag.text
                .strip()
                .replace('\n', '')
                .replace(',', ''),
            tag_object.find_all('li', class_='inline-list__item')))
        preview_text = tag_object.find('div', class_='post__text').text.strip()
        return cls(post_id, author, post_time, title, tags, preview_text)