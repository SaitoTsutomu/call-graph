`call-graph` is a package for viewing call graph.
::

   $ call-graph
   usage: call-graph [-h] [-p PATH] [-u] [-o] [-n NO_TARGET] module func
   call-graph: error: the following arguments are required: module, func
   
   $ call-graph call_graph main
   main
   ├ get_names
   ├ get_call_graph
   └ call_graph_view

* "NO_TARGET" is used for ignoring names.
* Methods are ignored.
* Use `_ = function` for dummy call.

Requirements
------------
* Python 3.8 later, more-itertools

Features
--------
* nothing

Setup
-----
::

   $ pip install call-graph

History
-------
0.0.1 (2020-4-21)
~~~~~~~~~~~~~~~~~~
* first release

