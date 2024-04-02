from typing import Optional
from pathlib import Path
from dataclasses import dataclass


EXCLUDE_DIR = {'FILES'}
SORT = ['指南', 'pvf', '服务端']


def gen_sub(p: Path, deepth: int = 0, prefix_idx: str = '') -> list[str]:
    ret = []
    i = 1
    for fp in p.iterdir():
        if fp.is_dir():
            if fp.name in EXCLUDE_DIR:
                continue
            children = gen_sub(fp, deepth=deepth + 1, prefix_idx=f'{prefix_idx}{i}.')
            ret.append(f'{deepth * "\t"}* [{prefix_idx}{i} {fp.name}]({fp})')
            ret.extend(children)
            i += 1
        else:
            ret.append(f'{deepth * "\t"}* [{prefix_idx}{i} {fp.name.removesuffix('.md')}]({fp})')
            i += 1
    return ret


def sort_by(paths: list[Path]) -> list[Path]:
    return sorted(paths, key=lambda p: SORT.index(p.name) if p.name in SORT else 0)


def gen():
    ret = []
    i = 1
    for p in sort_by(list(Path('.').iterdir())):
        if p.is_dir():
            if p.name in EXCLUDE_DIR:
                continue
            ret.append(f'* [{i}. {p.name}]({p})')
            ret.extend(gen_sub(p, 1, f'{i}.'))
            i += 1

    with Path('_sidebar.md').open('w') as f:
        f.write('\n'.join(ret))


if __name__ == '__main__':
    gen()
