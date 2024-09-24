# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Modify the ``/ID [<...> <...>]`` line in a PDF file.

This is provided to make generated manuscripts (via ``pdflatex``) be
bitwise identical across runs.
"""

from __future__ import print_function

import argparse


SPLIT_TEXT = b"\n/ID [<"
ID_LINE = "{0}> <{0}>]"


def verify_id_snippet(id_snippet):
    """Verifies an ID snippet being replaced.

    ``id_snippet`` is expected to be of the form
    ``'{X}> <{X}>]'`` where ``X`` is 32 characters.
    """
    if len(id_snippet) != 69:
        raise ValueError(id_snippet, "Invalid length")

    actual_id = id_snippet[:32].decode("ascii")
    if not (set(actual_id) <= set("0123456789ABCDEF")):
        raise ValueError(actual_id, "ID is not composed of hex characters.")

    expected_line = ID_LINE.format(actual_id).encode("ascii")
    if id_snippet != expected_line:
        raise ValueError(
            id_snippet, "Unexpected ID line. Expected", expected_line
        )


def do_replace(path, new_id):
    with open(path, "rb") as file_obj:
        contents = file_obj.read()

    # Assert that there is exactly one match.
    pre, post = contents.split(SPLIT_TEXT)
    # ID line expected to be of the form:
    #     /ID [<...> <...>]
    id_snippet, post = post.split(b"\n", 1)
    verify_id_snippet(id_snippet)
    # which would just leave `<...> <...>]` after the split.
    new_id_line = ID_LINE.format(new_id).encode("ascii")

    new_contents = pre + SPLIT_TEXT + new_id_line + b"\n" + post
    with open(path, "wb") as file_obj:
        file_obj.write(new_contents)

    print("Updated {}".format(path))


def main():
    description = "Modify the `/ID` property in a PDF generated by `pdflatex`."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--base", required=True, help="Base path for PDF file to be modified."
    )
    parser.add_argument(
        "--id", dest="id_", required=True, help="The prescribed ID to add."
    )

    args = parser.parse_args()
    filename = "{}.pdf".format(args.base)
    do_replace(filename, args.id_)


if __name__ == "__main__":
    main()
