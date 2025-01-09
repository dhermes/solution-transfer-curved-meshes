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

"""This is a configuration file for running ``nox`` on this project.

To determine the supported actions run ``nox --list-sessions`` from the
project root.
"""

import os

import nox
import py.path


NOX_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_INTERPRETER = "python3.7"


def get_path(*names):
    return os.path.join(NOX_DIR, *names)


class Remove(object):
    def __init__(self, prefix, extensions):
        self.prefix = prefix
        self.extensions = extensions

    def __call__(self):
        for extension in self.extensions:
            path = "{}.{}".format(self.prefix, extension)
            os.remove(path)


def build_tex_file(session, base, new_id, extensions=()):
    # NOTE: This assumes that ``session.chdir(get_path('doc'))``
    #       has been called.
    modify_id = get_path("scripts", "modify_pdf_id.py")

    session.run("pdflatex", base)
    session.run("bibtex", base)
    session.run("pdflatex", base)
    session.run("bibtex", base)
    session.run("pdflatex", base)
    session.run("pdflatex", base)

    path = get_path("doc", base)
    remove = Remove(path, extensions)
    session.run(remove)
    session.run("python3", modify_id, "--base", path, "--id", new_id)


@nox.session(py=False)
def build_tex(session):
    if py.path.local.sysfind("pdflatex") is None:
        session.skip("`pdflatex` must be installed")

    if py.path.local.sysfind("bibtex") is None:
        session.skip("`bibtex` must be installed")

    session.chdir(get_path("doc"))

    build_tex_file(
        session,
        "paper",
        "5178018C9121C4981906E150C72BEC1B",
        extensions=("aux", "bbl", "blg", "log", "out"),
    )


@nox.session(py=DEFAULT_INTERPRETER)
def blacken(session):
    """Run black code formatter."""
    session.install("black >= 23.3.0")
    session.run("black", "--line-length", "79", ".")
