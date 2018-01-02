import unittest
import helpers
import imp

imp.reload(helpers)

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
 
    def test_node_with_most_edges_1(self):
        """
        empyt set returns None
        """
        result = helpers.node_with_most_edges({},[1,1])
        self.assertEqual(result, None)
    def test_node_with_most_edges_2(self):
        """
        returns index with most edges
        """
        result = helpers.node_with_most_edges({0,1,5},[1,3,6,1,1,1])
        self.assertEqual(result, 1)
 
    def test_empty_node_1(self):
        """
        works even with just one set
        """
        result = helpers.is_any_node_empty([[1,1,5]])
        self.assertEqual(result, False)
    def test_empty_node_2(self):
        """
        works even with just one set
        """
        result = helpers.is_any_node_empty([[]])
        self.assertEqual(result, True)
    def test_empty_node_3(self):
        """
        works even with multiple sets
        """
        result = helpers.is_any_node_empty([[0], [1], [0, 2], [1], [2], [2], [0, 2], [], [0, 1], [1]])
        self.assertEqual(result, True)
    def test_empty_node_4(self):
        """
        works even with multiple sets
        """
        result = helpers.is_any_node_empty([[0], [1], [0, 2], [1], [2], [2], [0, 2], [0, 1], [1]])
        self.assertEqual(result, False)
 
    def test_propagate_1(self):
        """
        removes 1 option for node 0
        """
        result = helpers.prop_not_same_color([[0,1],[0,1],[1]],
                                             [[0,1],[0,2]])
        self.assertEqual(result, [[0],[0,1],[1]])
    def test_propagate_2(self):
        """
        doesn't remove anything
        """
        result = helpers.prop_not_same_color([[0,1],[0,1],[0,1]],
                                             [[0,1],[0,2]])
        self.assertEqual(result, [[0,1],[0,1],[0,1]])
    def test_propagate_3(self):
        """
        test of handles case that should never make it there
        """
        result = helpers.prop_not_same_color([[1],[0,1],[1]],
                                             [[0,1],[0,2]])
        self.assertEqual(result, [[1],[0],[]])

    def test_less_color_left_1(self):
        """
        doesn't pick the 1 left
        """
        result = helpers.with_less_color_left([[2],[0],[0,1],[1],[1]])
        self.assertEqual(result, [2])
    def test_less_color_left_2(self):
        """
        picks multiple
        """
        result = helpers.with_less_color_left([[2],[0,4],[0,1],[1],[1]])
        self.assertEqual(result, [1,2])
        
    def test_update_1(self):
        """
        updates node 2
        """
        result = helpers.update_solution([0,-1,-1,1],
                                         [[0],[0,1],[1],[1]])
        self.assertEqual(result, [0,-1,1,1])
if __name__ == '__main__':
    unittest.main()