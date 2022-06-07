import unittest


def are_mutually_reverse(list1, list2):
    '''
    Return True if the two lists are mutually reverse, False otherwise
    You may not use any built in function besides
    len(list) and accessing attributes using index
    '''

    first_index = 0
    last_index = -1
    counter = 0
    condition_reverse = True

    if len(list1) == len(list2):
        while counter < len(list1):
            if list1[first_index] == list2[last_index]:
                condition_reverse = True
                first_index += 1
                last_index -= 1
                counter += 1
            else:
                condition_reverse = False
                break
    else:
        condition_reverse = False

    return condition_reverse


class Tester(unittest.TestCase):
    def test_are_mutually_reverse(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        self.assertTrue(are_mutually_reverse(list1, list2))
        list2 = [3, 2, 4]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list2 = [4, 2, 1]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list2 = [3, 2, 1, 0]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list1 = [0] * 1000
        list2 = [0] * 1000
        list1[0] = 8
        list2[-1] = 8
        self.assertTrue(are_mutually_reverse(list1, list2))


if __name__ == '__main__':
    unittest.main()
