import unittest
from hw8.path_search import *


class TestPathSearch(unittest.TestCase):
    def path_str(self, ps_test, path):
        error_msg = ""
        for p in path[1:-1]:
            if not p.value == "*":
                p.value = "-"
        return str(ps_test) + error_msg

    def neighbor_of(self, node1, node2):
        r1 = node1.row
        c1 = node1.col
        r2 = node2.row
        c2 = node2.col
        if abs(r2-r1) == 1 or abs(c2-c1) == 1:
            return True
        else:
            return False

    def is_valid_path(self, ps_test, path):
        prev_node = path[0]
        for node in path[1:-1]:
            if node.value == "*":
                error_msg = "\nError: Path through blocked node: (" + str(node.row) + ", " + str(node.col) + ")"
                return False, error_msg
            if not self.neighbor_of(prev_node, node):
                msg = "(" + str(node.row) + ", " + str(node.col) + ") not adjacent to (" + str(prev_node.row) + ", " + str(prev_node.col) + ")"
                return False, msg
            prev_node = node
        if path[0] != ps_test.start_node:
            return False, "Path doesn't start at start node: (" + str(ps_test.start_node.row) + ", " + str(ps_test.start_node.col) + ")"
        if path[-1] != ps_test.goal_node:
            return False, "Path doesn't end at goal node: (" + str(ps_test.goal_node.row) + ", " + str(ps_test.goal_node.col) + ")"
        return True, ""

    def path_test(self, sr, sc, gr, gc, blocked_cells=0):
        ps_test = PathSearchTest(size=10, blocked_cells=blocked_cells)
        path_search = PathSearch(ps_test.neighbors_cb)
        ps_test.start_node.value = "."
        ps_test.start_node = PathSearchTest.TestCell(sr, sc)
        ps_test.start_node.value = "s"
        ps_test.grid[sr][sc] = ps_test.start_node
        ps_test.goal_node.value = "."
        ps_test.goal_node = PathSearchTest.TestCell(gr, gc)
        ps_test.goal_node.value = "g"
        ps_test.grid[gr][gc] = ps_test.goal_node
        # print ps_test
        path = path_search.search(ps_test.start_node, ps_test.goal_node)
        # path[1].value = "*"    # Uncomment to test path through blocked node
        # del path[1]            # Uncomment to test non-continuous path
        # del path[0]            # Uncomment to test path starting at start node
        # del path[-1]           # Uncomment to test path ending at goal node
        valid, msg = self.is_valid_path(ps_test, path)
        self.assertTrue(valid,
            "Path from ["+str(sr)+", "+str(sc)+"] to ["+str(gr)+", "+str(gc)+"] invalid:\n"
            + self.path_str(ps_test, path)
            + msg)
        # print self.path_str(ps_test, path)

    def test_search_one_over_no_blocked_cells(self):
        self.path_test(5, 5, 5, 6, blocked_cells=0)

    def test_search_row_left_to_right_no_blocked_cells(self):
        self.path_test(2, 2, 2, 8, blocked_cells=0)

    def test_search_right_to_left_no_blocked_cells(self):
        self.path_test(2, 8, 2, 2, blocked_cells=0)

    def test_search_top_to_bottom_no_blocked_cells(self):
        self.path_test(3, 4, 7, 4, blocked_cells=0)

    def test_search_bottom_to_top_no_blocked_cells(self):
        self.path_test(7, 4, 3, 4, blocked_cells=0)

    def test_search_diagonal_no_blocked_cells(self):
        self.path_test(3, 1, 6, 4, blocked_cells=0)

    def test_search_one_over_blocked_cells(self):
        self.path_test(5, 5, 5, 6, blocked_cells=20)

    def test_search_row_left_to_right_blocked_cells(self):
        self.path_test(2, 2, 2, 8, blocked_cells=20)

    def test_search_right_to_left_blocked_cells(self):
        self.path_test(2, 8, 2, 2, blocked_cells=20)

    def test_search_top_to_bottom_blocked_cells(self):
        self.path_test(3, 4, 7, 4, blocked_cells=20)

    def test_search_bottom_to_top_blocked_cells(self):
        self.path_test(7, 4, 3, 4, blocked_cells=20)

    def test_search_diagonal_blocked_cells(self):
        self.path_test(3, 1, 6, 4, blocked_cells=20)

unittest.main()