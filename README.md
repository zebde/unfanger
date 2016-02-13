# CVE-Builder
[![Code Health](https://landscape.io/github/cwtaylor/unfanger/master/landscape.svg?style=flat)](https://landscape.io/github/cwtaylor/unfanger/master)

A selection of scripts that "unfang" strings from files.

"Fanging", is the process that is common amongst professionals to share malicious network observables safely. This is to ensure that observable is not represented as a hyperlink and clicked on.

This means that `192.168.1.1`, turns into `192[.]168[.]1[.]1`. This is good and is not so much of an issue when you only have one or two. But when you get 100+ observables in this format it can be a pain.

This repository contains various different implementations of code that "unfangs" the observables.

Each implementation must be able to carry out the following transformations:

- `[.]` to `.`
- `hxxp://` to `http://`
- `hxxps://` to `https://`
- `[at]` to `@`

## License
See the [LICENSE](LICENSE) file for license rights and limitations (GPLv3).
