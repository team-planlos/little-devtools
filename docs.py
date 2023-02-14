from enum import Enum

"""Made for gathering documentation and structure all of that in a folder
"""

def check_create_dir(dire: str):
    import os
    try:
        os.chdir(dire)
    except Exception:
        os.mkdir(dire)

class DocStyles(Enum):
    _decoding = "doc"
    _head = "head"
    _body = "body"
    PYTHON = ["head'''doc'''body", 'head"""doc"""body', "# docheadbody", "## docheadbody", "### docheadbody"]
    RUST = ["///docheadbody", "//!docheadbody"]

class Documentation():

    docstyles: DocStyles
    target: str # "web", "md" and "raw" is usual
    content: list[str]

    def __init__(self, docstyles: DocStyles):
        self.docstyles = docstyles

    def raw_doc_head(self, path: str, docstyle: DocStyles):
        pass

    def generate_docs(self):
        pass

if __name__ == "__main__":
    # identificate_doc("docs.py", DocStyles.PYTHON)
    help(Documentation)