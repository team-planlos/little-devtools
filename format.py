""" mod for formatting stuff
"""

def indent():
    pass

def dedent():
    pass

def tree_to_iterator(path: str) -> list[str]:
    pass

class FileHandle():

    path: str
    file_content: str

    def __init__(self, path: str) -> None:
        self.path = path

    def br(self):
        self.file_content = self.file_content + "\n"

    def add(self, s: str):
        self.file_content = self.file_content + s + "\n"

    def ready(self, path=""):
        if not path:
            path=self.path
        with open(path, "x") as file:
            file.write(self.file_content)
        del self

class GithubMarkdown(FileHandle):

    footnote_index: int
    footnotes: list[str]

    def __init__(self, path: str):
        super().__init__(self, path)
        self.footnote_index = 0

    def ready(self, path=""):
        self.drop_footnotes
        super().ready(path=path)

    def erase_all_md(self, s: str) -> str:
        for forbidden in ["*", "**", "_", "__", "~~", "#", ""]:
            s.replace(forbidden, "\{}".format(forbidden))

    def wrap(self, s: str, around: str):
        self.add(around + s + around)

    def header(self, s: str, deg: int):
        if deg > 6:
            deg = 6
        self.add("#" * deg + s)

    def bold(self, s: str):
        self.wrap(s, "**")

    def alt_bold(self, s: str):
        self.wrap(s, "__")

    def italic(self, s: str):
        self.wrap(s, "*")

    def alt_italic(self, s: str):
        self.wrap(s, "_")

    def crossed_out(self, s: str):
        self.wrap(s, "~~")

    def sub(self, s: str):
        self.add("<sub>" + s + "</sub>")

    def sup(self, s: str):
        self.add("<sup>" + s + "</sup>")

    def quote(self, s: str):
        self.add("> " + s)

    def code(self, s: str):
        self.wrap(s, "`")

    def codeblock(self, s: str):
        self.wrap(s, "\n```\n")

    def color_hexa(self, s: str):
        self.wrap(s, "`")

    def color_rgb(self, r: int, g: int, b: int):
        self.add("`rgb({}, {}, {})`".format(r, g, b))

    def color_hsl(self, h: int, s: int, l: int):
        self.add("`hsl({}, {}%, {}%)`".format(h, s, l))

    ## <picture>
    ## <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
    ## <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
    ## <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
    ## </picture>
    def embed(self, descr: str, link: str):
        self.add("[{}]({})".format(descr, link))

    def item(self, s: str):
        self.add("- " + s)

    def numberitem(self, s: str, number: int):
        self.add(str(number) + " " + s)

    def chbox(self, s: str, ticked: bool):
        tk = ""
        if ticked:
            tk = "x"
        self.item("[" + tk + "] " + s)

    def mention(self, s: str):
        self.add("@" + s)

    def issue_pr(self, nr_link: str):
        self.add("#" + nr_link)
    
    def emo(self, s: str):
        self.wrap(s, ":")

    def space(self):
        self.br()
        self.br()

    def footnote(self, short: str, long: str):
        self.footnote_index += 1
        self.add(short + "[^{}]".format(str(self.footnote_index)))
        self.footnotes.append(long)

    def drop_footnotes(self):
        index = 0
        for footnote in self.footnotes:
            self.add("[^{}]: {}".format(index, footnote))
            index += 1

    def comment(self, s: str):
        self.add("<!-- {} -->".format(s))

class HTML5(FileHandle):

    pass