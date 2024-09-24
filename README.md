# High-order Solution Transfer between Curved Triangular Meshes

This is work with [Per-Olof Persson][6].

This originally appeared in my [thesis][1] and is now split out
into a standalone [paper][3].

This repository is laid out in a manner described in
[Good Enough Practices in Scientific Computing][2].

The content itself has been uploaded to the [arXiv][4] and was submitted to
the journal [CAMCoS][5] on October 12, 2018.

## Abstract

The problem of solution transfer between meshes arises frequently in
computational physics, e.g. in Lagrangian methods where remeshing
occurs. The interpolation process must be conservative, i.e. it
must conserve physical properties, such as mass. We extend previous
works &mdash; which described the solution transfer process for straight sided
unstructured meshes &mdash; by considering high-order isoparametric meshes
with curved elements. To facilitate solution transfer, we numerically
integrate the product of shape functions via Green's theorem along the
boundary of the intersection of two curved elements. We perform a numerical
experiment and confirm the expected accuracy by transferring test fields
across two families of meshes.

## Installation

The code used to build the manuscript, generate images and verify
computations is written in Python. To run the code, Python 3.7
should be installed, along with `nox-automation`:

```
python -m pip install --upgrade 'nox-automation == 0.19.1'
```

Once installed, the various build jobs can be listed. For example:

```
$ nox --list-sessions
Available sessions:
* build_tex
* make_images
* update_requirements
* blacken -> Run black code formatter.
```

To run `nox -s build_tex` (i.e. to build the PDF), `pdflatex` and
`bibtex` are required.

[1]: https://github.com/dhermes/phd-thesis
[2]: https://arxiv.org/abs/1609.00037
[3]: doc/paper.pdf
[4]: https://arxiv.org/abs/1810.06806
[5]: https://msp.org/camcos/about/journal/about.html
[6]: https://popersson.github.io/
