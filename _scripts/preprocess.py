import argparse
from os.path import join, basename
import re


def fix_url(line, verbose=False):
    """
    Replace Jekyll-specific URLs with document internal fragments
    """
    url = re.compile('(\(\{\{ site\.baseurl \}\}/)(.+?\))')
    if line.startswith('#'):
        return line
    if line.startswith('Table of Contents'):
        return ''
    m = url.search(line)
    if m is None:
        return line
    else:
        path = m.group(2)
        frag = '(#{}'.format(path.split('#')[-1])
        newline = line.replace(m.group(0), frag)
        if verbose:
            #print(newline)
            print('replacing {} with {}'.format(m.group(0), frag))
        return newline

def header_id(meta):
    """
    Add new MD title and title identifier
    """
    title = meta['title']
    title = title[1:-1] #strip quotes from string
    title_fmt = '# {} {{#{}}}\n'
    lc_title = title.lower().replace(' ', '_')
    if lc_title.endswith('?'):
        lc_title = lc_title[:-1]
    new_title = title_fmt.format(title, lc_title)
    return new_title


def strip_header(text, verbose=False):
    """
    Strip the YAML header from Jekyll files, and fix URLs and anchors
    """
    out = []
    header = False
    meta = {}
    for line in text:
        line = line[:-1]
        if line.startswith("---") and not header:
            header = True
            continue
        if header:
            try:
                k, v = line.split(':')
                meta[k] = v.strip()
            except ValueError:
                pass
            if line.startswith("---"):
                header=False
                new_title = header_id(meta)
                out.append(new_title)
        else:
            line = fix_url(line, verbose=verbose)
            out.append(line)
    if verbose:
        print('copied {} lines'.format(len(out)))
    return out



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-outdir', required=True)
    parser.add_argument('infile', nargs='*')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        print('\n' * 2)
        print('#' * 50)
        print('\n' * 2)
    for infile in args.infile:
        with open(infile) as f:
            if args.verbose:
                print('opening file {}'.format(infile))

            headless = strip_header(f, verbose=args.verbose)
            infile = basename(infile)
            outfile = join(args.outdir, infile)

            with open(outfile, "w", encoding='utf8') as outf:
                if args.verbose:
                    print('writing to file {}'.format(outfile))
                for line in headless:
                    outf.write(line + '\n')
                    #args.outfile.write(line + '\n')
