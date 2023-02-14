from enum import Enum

"""Made for gathering documentation and structure all of that in a folder
"""

def check_create_dir(dire: str):
    import os
    try:
        os.chdir(dire)
    except Exception:
        try:
            os.mkdir(dire)
        except:
            pass

def identificate_doc(path: str, ):
    pass

class DocStyle(Enum):
    _decoding = "doc"
    _head = "head"
    _body = "body"
    PYTHON = ["head'''doc'''body", 'head"""doc"""body', "# docheadbody", "## docheadbody", "### docheadbody"]

if __name__ == "__main__":
    check_create_dir("test")