`call-graph` is a package for viewing call graph.
::

   $ call-graph
   usage: call-graph module func
   
   $ call-graph call_graph main
   main
   ├ get_call_graph
   │└ getclosurevars
   │　├ ismethod
   │　├ isfunction
   │　└ ismodule
   └ call_graph_view
   　└ pairwise

* "no_target" is used for ignoring names.
* Methods are ignored.

Requirements
------------
* Python 3.7 later

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

