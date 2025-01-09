# High-order Solution Transfer between Curved Triangular Meshes

| Cite paper           |
| -------------------- |
| [![Paper DOI][9]][7] |

This is work with [Per-Olof Persson][6].

This originally appeared in my [thesis][1] and is now split out
into a standalone [paper][3].

This repository is laid out in a manner described in
[Good Enough Practices in Scientific Computing][2].

The content itself has been uploaded to the [arXiv][4] and was submitted to
the journal [CAMCoS][5] on October 12, 2018. The paper has been accepted and
was [published][7] [on][8] January 8, 2025.

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

## Citation

To cite this paper:

```
@article{Hermes2025,
  doi = {10.2140/camcos.2025.20.1},
  url = {http://dx.doi.org/10.2140/camcos.2025.20.1},
  year = {2025},
  month = {Jan},
  publisher = {Mathematical Sciences Publishers},
  volume = {20},
  number = {1},
  pages = {1--27},
  author = {Hermes, Danny and Persson, Per-Olof},
  title = {High-order solution transfer between curved triangular meshes},
  journal = {Communications in Applied Mathematics and Computational Science},
  ISSN = {1559-3940}
}
```

## Installation

The code used to build the manuscript, generate images and verify
computations is written in Python. To run the code, Python 3.7
should be installed, along with `nox`:

```
python -m pip install --upgrade 'nox == 2024.4.15'
```

Once installed, the various build jobs can be listed. For example:

```
$ nox --list-sessions
...
Sessions defined in .../noxfile.py:

* build_tex
* blacken -> Run black code formatter.

sessions marked with * are selected, sessions marked with - are skipped.
```

To run `nox -s build_tex` (i.e. to build the PDF), `pdflatex` and
`bibtex` are required.

## Images

The `images/` in this repository are from my [thesis][1], in particular:

- `images/preliminaries/`:
  - `inverted_element.pdf`
  - `main_figure01.pdf`
  - `main_figure26.pdf`
- `images/bezier-intersection/`:
  - `bbox_check.pdf`
  - `locate_in_triangle.pdf`
  - `main_figure21.pdf`
  - `main_figure22.pdf`
  - `main_figure23.pdf`
  - `main_figure24.pdf`
  - `subdivide_curve.pdf`
  - `subdivision_linearized.pdf`
  - `subdivision_process.pdf`
- `images/solution-transfer/`:
  - `main_figure00.pdf`
  - `main_figure02.pdf`
  - `main_figure11.pdf`
  - `main_figure13.pdf`
  - `main_figure14.pdf`
  - `main_figure15.pdf`
  - `main_figure16.pdf`
  - `main_figure25.pdf`
  - `main_figure30.pdf`

Scripts to generate these images can be found there.

[1]: https://github.com/dhermes/phd-thesis
[2]: https://arxiv.org/abs/1609.00037
[3]: doc/paper.pdf
[4]: https://arxiv.org/abs/1810.06806
[5]: https://msp.org/camcos/about/journal/about.html
[6]: https://popersson.github.io/
[7]: https://doi.org/10.2140/camcos.2025.20.1
[8]: https://github.com/dhermes/solution-transfer-curved-meshes/blob/main/doc/camcos-v20-n1-p01-s.pdf
[9]: https://img.shields.io/badge/DOI-10.2140%2Fcamcos.2025.20.1-blue.svg
