from datetime import date
import datetime
import os
from juniper import settings
import markdown
import codecs
from django.utils.safestring import mark_safe

class Entry(object):
    def __init__(self, md_file):
        self.md_file = md_file
        # default values
        self.post_title = u""
        self.post_date = date(1970,1,1)
        self.post_visible = False
        self.post_theres_more = False
        self.post_tags = []
        self.post_content_html_short = u""
        self.post_content_md = u""
        self.post_content_html = u""
        self.post_lang = ['ro', 'en']


    def read(self):
        f = codecs.open(os.path.join(settings.MARKDOWN_DIR, self.md_file), mode="r", encoding="utf-8")
        all_lines = f.readlines()

        for ln in list(all_lines):

            split = ln.split(':',1) #split by colon but only by the first colon.
            tag = split[0].strip()
            value = split[1].strip()

            if tag == "POST_TITLE":
                self.post_title = value
            elif tag == "POST_DATE":
                self.post_date = datetime.datetime.strptime(value, '%d-%m-%Y %H:%M')
            elif tag == "POST_VISIBLE":
                self.post_visible = (value == u"True")
            elif tag == "POST_TAGS":
                self.post_tags = [t.strip() for t in value.split(',')]
            elif tag == "POST_LANG":
                self.post_lang = [t.strip() for t in value.split(',')]
            elif tag == "POST_CONTENT":
                all_lines.remove(ln)
                break;

            all_lines.remove(ln)

        self.post_content_md = ''.join(all_lines)
        self.post_content_html = mark_safe(markdown.markdown(self.post_content_md))

        index = self.post_content_md.find("{.}")
        if index > -1:
            self.post_content_html_short = mark_safe(markdown.markdown(self.post_content_md[0:index]))
            self.post_theres_more = True
            self.post_content_html = mark_safe(self.post_content_html.replace("{.}", ""))






if __name__ == "__main__":
    e = Entry("F:/_work/gits/juniper/posts/markdown/post1.md")
    e.read()





