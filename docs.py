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

def identificate_doc(path: str):
    pass

if __name__ == "__main__":
    pass