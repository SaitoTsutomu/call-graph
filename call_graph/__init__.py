import argparse
import os
from inspect import getclosurevars, isfunction
from itertools import chain

from more_itertools import pairwise

# see pyproject.toml
__version__ = "0.1.0"
__author__ = "SaitoTsutomu <tsutomu7@hotmail.co.jp>"


def _target(f, path, done, use):
    return (
        isfunction(f)
        and (use or not f.__name__.startswith("_"))
        and f.__name__ not in done
        and path not in f.__code__.co_filename
    )


def get_call_graph(func, path, done, use):
    gcl = getclosurevars(func).globals
    done |= {func.__name__}
    return {k: get_call_graph(f, path, done, use) for k, f in gcl.items() if _target(f, path, done, use)}


def call_graph_view(call_graph, pre, only):
    for (k, v), (k2, _) in pairwise(chain(call_graph.items(), [("", {})])):
        _call_graph(v, pre, int(bool(k2)), k, only)


def _call_graph(children, pre, nxt, name, only):
    print(*[pre, "└├"[nxt], " ", name][only * 3 :], sep="")  # noqa
    call_graph_view(children, pre + "　│"[nxt], only)


def get_names(filename):
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as fp:
            return set(fp.read().splitlines())
    return set()


def main():
    """
    Show call graph.
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("module", help="Target module")
    parser.add_argument("func", help="Target function")
    parser.add_argument("-p", "--path", default="/lib/python3", help="Sub path of library.")
    parser.add_argument("-u", "--use", default=False, help="Use private function.", action="store_true")
    parser.add_argument("-o", "--only", default=False, help="Show only name.", action="store_true")
    parser.add_argument("-n", "--no-target", default="", help="File which contains name of no target.")
    args = parser.parse_args()
    no_target = get_names(args.no_target)
    print(args.func)
    func = getattr(__import__(args.module), args.func)
    call_graph = get_call_graph(func, args.path, no_target, args.use)
    call_graph_view(call_graph, "", args.only)
