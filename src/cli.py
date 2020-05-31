#!/usr/bin/env python3

import notebook


def main():
    bs = notebook.create_pdf(polynome=[2, 0, 0])
    with open('out.pdf', 'wb') as f:
        f.write(bs)


if __name__ == '__main__':
    main()
