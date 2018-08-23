# High-order Solution Transfer between Curved Meshes

This is work with Per-Olof Persson.

This originally appeared in my [thesis][1] and is now split out
into a standalone [paper][3].

This repository is laid out in a manner described in
[Good Enough Practices in Scientific Computing][2].

## Abstract

The problem of solution transfer between meshes arises frequently in
computational physics, e.g. in Lagrangian methods where remeshing
occurs. The interpolation process must be conservative, i.e. it
must conserve physical properties, such as mass. We extend previous
works &mdash; which described the solution transfer process for straight sided
unstructured meshes &mdash; by considering high-order isoparametric meshes
with curved elements. The implementation is highly reliant on accurate
computational geometry routines for evaluating points on and
intersecting B&#xe9;zier curves and triangles.

## Installation

The code used to build the manuscript, generate images and verify
computations is written in Python. To run the code, Python 3.7
should be installed, along with ``nox-automation``:

```
python -m pip install --upgrade nox-automation
```

Once installed, the various build jobs can be listed. For example:

```
$ nox --list-sessions
Available sessions:
* build_tex
```

To run ``nox -s build_tex`` (i.e. to build the PDF), ``pdflatex`` and
``bibtex`` are required.

[1]: https://github.com/dhermes/phd-thesis
[2]: https://arxiv.org/abs/1609.00037
[3]: doc/paper.pdf
