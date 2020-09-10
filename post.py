class Post:
    def __init__(self, post_link, post_id, author, post_time, title, tags, post_text):
        self.post_link = post_link
        self.post_id = post_id
        self.author = author
        self.post_time = post_time
        self.title = title
        self.tags = tags
        self.preview_text = post_text

    def to_str(self):
        return f"Link to post = {self.post_link}\nAuthor - {self.author}\nTitle - {self.title}\n\n{self.preview_text}"

    @classmethod
    def from_bs_tag(cls, tag_object):
        post_id = tag_object['id'].split('post_')[1]
        post_link = tag_object.find('a', class_='post__title_link')['href']
        post_author = tag_object.find('span', class_='user-info__nickname').text
        post_time = tag_object.find('span', class_='post__time').text
        post_title = tag_object.find('h2', class_='post__title').text.replace('\n', '')
        post_tags = list(map(
            lambda tag: tag.text
                .strip()
                .replace('\n', '')
                .replace(',', ''),
            tag_object.find_all('li', class_='inline-list__item')))
        preview_text = tag_object.find('div', class_='post__text').text.strip()

        return cls(post_link, post_id, post_author, post_time, post_title, post_tags, preview_text)

    def __eq__(self, another_post):
        return self.post_id == another_post.id
