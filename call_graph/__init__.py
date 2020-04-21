import os
import sys
from inspect import getclosurevars, isfunction
from itertools import chain

from more_itertools import pairwise

# see pyproject.toml
__version__ = "0.0.1"
__author__ = "SaitoTsutomu <tsutomu7@hotmail.co.jp>"


def _target(f, done):
    return isfunction(f) and not f.__name__.startswith("_") and f.__name__ not in done


def get_call_graph(func, done):
    gcl = getclosurevars(func).globals
    done |= {func.__name__}
    return {k: get_call_graph(f, done) for k, f in gcl.items() if _target(f, done)}


def call_graph_view(call_graph, pre=""):
    for (k, v), (k2, _) in pairwise(chain(call_graph.items(), [("", {})])):
        _call_graph(v, pre, int(bool(k2)), k)


def _call_graph(children, pre, nxt, name):
    print(pre, "└├"[nxt], " ", name, sep="")
    call_graph_view(children, pre + "　│"[nxt])


def main():
    if len(sys.argv) <= 2:
        print("usage: call-graph module func")
        return
    module, funcname = sys.argv[1:3]
    print(funcname)
    func = __import__(module).__getattribute__(funcname)
    _no_target = "no_target"
    no_target = set()
    if os.path.exists(_no_target):
        with open(_no_target) as fp:
            no_target = set(fp.read().splitlines())
    call_graph = get_call_graph(func, no_target)
    call_graph_view(call_graph)
