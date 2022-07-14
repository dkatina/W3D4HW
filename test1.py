from unittest import TestCase, main
from hw import move_zeros, move_zeros2, move_zeros3

class MoveZerosTestCase(TestCase):

    def test_1_base(self):
        self.assertEqual(move_zeros([1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0])

    def test_2_double_O(self):
        self.assertEqual(move_zeros([5, 6, 0, 0, 7, 8]), [5, 6, 7, 8, 0, 0])

    def test_3_starting_with_0(self):
        self.assertEqual(move_zeros([0, 1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])

    def test_3_ending_with_0(self):
        self.assertEqual(move_zeros([0, 1, 2, 0, 3, 0, 4, 0, 0]), [1, 2, 3, 4, 0, 0, 0, 0, 0])

    def test_3_starting_with_0(self):
        self.assertEqual(move_zeros([0, 1, 2, 00, 3, 0, 4]), [1, 2, 3, 4, 0, 00, 0]) 

class MoveZeros3TestCase(TestCase):

    def test_1_base(self):
        self.assertEqual(move_zeros3([1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0])

    def test_2_double_O(self):
        self.assertEqual(move_zeros3([5, 6, 0, 0, 7, 8]), [5, 6, 7, 8, 0, 0])

    def test_3_starting_with_0(self):
        self.assertEqual(move_zeros3([0, 1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])

    def test_4_ending_with_0(self):
        self.assertEqual(move_zeros3([0, 1, 2, 0, 3, 0, 4, 0, 0]), [1, 2, 3, 4, 0, 0, 0, 0, 0])

    def test_5_00(self):
        self.assertEqual(move_zeros3([0, 1, 2, 00, 3, 0, 4]), [1, 2, 3, 4, 0, 00, 0])

    def test_6_String_0(self):
        self.assertEqual(move_zeros3(['0', 1, 2, '0', 3, '0', 4]), [1, 2, 3, 4, '0', '0', '0']) 

    def test_7_Zero(self):
        self.assertEqual(move_zeros3(['zero', 1, 2, 'zero', 3, 'zero', 4]), [1, 2, 3, 4, 'zero', 'zero', 'zero'])

    def test_8_All_Zer0s(self):
        self.assertEqual(move_zeros3(['0', 1, 2, 'zero', 3, 0, 4]), [1, 2, 3, 4, '0', 'zero', 0])

    def test_9_Empty_Nester(self):
        self.assertEqual(move_zeros3([]), [])

    
                      


if __name__ == "__main__":
    main()