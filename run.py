# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)


## RESULTS ##
bfs_result = search.breadth_first_graph_search(ab)
dfs_result = search.depth_first_graph_search(ab)
bb_result = search.branch_and_bound_graph_search(ab)
bbh_result = search.branch_and_bound_heuristic_graph_search(ab)

## PRINTS ##

print("Generated:",  bfs_result[1], ", Visited:", bfs_result[2], ", Total Cost:", bfs_result[3], ", Path:", bfs_result[0].path())
print("Generated:",  dfs_result[1], ", Visited:", dfs_result[2], ", Total Cost:", dfs_result[3], ", Path:", dfs_result[0].path())
print("Generated:",  bb_result[1], ", Visited:", bb_result[2], ", Total Cost:", bb_result[3], ", Path:", bb_result[0].path())
print("Generated:",  bbh_result[1], ", Visited:", bbh_result[2], ", Total Cost:", bbh_result[3], ", Path:", bbh_result[0].path())

## OLD PRINTS ##
##print(search.breadth_first_graph_search(ab).path())
##print(search.depth_first_graph_search(ab).path())
##print(search.branch_and_bound_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
