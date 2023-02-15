#! /usr/bin/env python3

#
# Copyright (c) 2019-23 Dan Trickey.
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
from pathlib import Path
import re

FOLDER_REGEX = re.compile("^20\d{2}$")
FILENAME_REGEX = re.compile(r"^(20\d{2})-(\d{2})-(\d{2})(-[a-z0-9-]+)?\.md$")

IGNORED_FOLDERS = {".git", ".github", "scripts"}
IGNORED_FILES = {".gitignore", ".gitattributes", ".editorconfig", "verify_filenames.py", "README.md"}

def main() -> None:
    all_passed = True
    print("✍️  Verifying minutes filenames 👮")

    repo = Path(".")

    year_folders = []

    for file in repo.iterdir():
        if file.is_dir():
            if file.name in IGNORED_FOLDERS:
                print(f"🙈 Found folder {file.stem}, ignoring 🙈")
            else:
                year_folders.append(file)
        elif file.is_file():
            if file.name not in IGNORED_FILES:
                print(f"🦹 Found bad file name: {file.name} 🦹")
                all_passed = False

    for year_folder in year_folders:

        # Verify folder name is valid

        result = FOLDER_REGEX.match(year_folder.name)

        if result is None:
            print(f"💔 Found bad folder name: {year_folder.name}")
            all_passed = False
        else:
            print(f"💙 Found valid folder name: {year_folder.name}")

        for file in year_folder.iterdir():
            if file.is_dir():
                print(f"\t💔 Found nested directory: {year_folder.stem}/{file.stem}")
                all_passed = False
            else:

                # Verify file name
                file_result = FILENAME_REGEX.match(file.name)

                if file_result is None:
                    print(f"\t💔 Found bad file name: {file.name}")
                    all_passed = False
                else:
                    # Verify file year
                    year, month, day, description = file_result.groups()

                    if year != year_folder.name:
                        print(f"\t😠 Found file in wrong folder: {year_folder.name}/{file.name}")
                        all_passed = False
                    else:
                        print(f"\t✔️ Found valid file name: {file.name}")

    if all_passed:
        print("👍 All tests passed. 👍")
    else:
        print("🙅 Some tests failed. 😞")
        exit(1)

if __name__ == "__main__":
    main()
