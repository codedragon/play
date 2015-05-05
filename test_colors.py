import unittest
import color_world as cw


class ColorWorldTests(unittest.TestCase):

    def test_make_color_map(self):
        colors = ['r', 'b']
        color_map, axis_map = cw.make_color_map(colors)
        # mapping, x, y, z, r is 0, g is 1, b is 2
        known = {'x_axis': 0, 'y_axis': 2, 'z_axis': None, 0: 0, 1: None, 2: 1}
        self.assertEqual(color_map, known)

    def test_make_color_map_with_z(self):
        colors = ['r', 'b', 'g']
        color_map, axis_map = cw.make_color_map(colors)
        known = {'x_axis': 0, 'y_axis': 2, 'z_axis': 1, 0: 0, 1: 2, 2: 1}
        self.assertEqual(color_map, known)

if __name__ == "__main__":
    unittest.main(verbosity=2)