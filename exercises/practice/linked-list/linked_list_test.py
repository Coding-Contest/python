import unittest

from linked_list import (
    LinkedList,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class LinkedListTest(unittest.TestCase):
    def test_pop_gets_element_from_the_list(self):
        lst = LinkedList()
        lst.push(7)
        self.assertEqual(lst.pop(), 7)

    def test_push_pop_respectively_add_remove_at_the_end_of_the_list(self):
        lst = LinkedList()
        lst.push(11)
        lst.push(13)
        self.assertEqual(lst.pop(), 13)
        self.assertEqual(lst.pop(), 11)

    def test_shift_gets_an_element_from_the_list(self):
        lst = LinkedList()
        lst.push(17)
        self.assertEqual(lst.shift(), 17)

    def test_shift_gets_first_element_from_the_list(self):
        lst = LinkedList()
        lst.push(23)
        lst.push(5)
        self.assertEqual(lst.shift(), 23)
        self.assertEqual(lst.shift(), 5)

    def test_unshift_adds_element_at_start_of_the_list(self):
        lst = LinkedList()
        lst.unshift(23)
        lst.unshift(5)
        self.assertEqual(lst.shift(), 5)
        self.assertEqual(lst.shift(), 23)

    def test_pop_push_shift_and_unshift_can_be_used_in_any_order(self):
        lst = LinkedList()
        lst.push(1)
        lst.push(2)
        self.assertEqual(lst.pop(), 2)
        lst.push(3)
        self.assertEqual(lst.shift(), 1)
        lst.unshift(4)
        lst.push(5)
        self.assertEqual(lst.shift(), 4)
        self.assertEqual(lst.pop(), 5)
        self.assertEqual(lst.shift(), 3)

    def test_count_an_empty_list(self):
        lst = LinkedList()
        self.assertEqual(len(lst), 0)

    def test_count_a_list_with_items(self):
        lst = LinkedList()
        lst.push(37)
        lst.push(1)
        self.assertEqual(len(lst), 2)

    def test_count_is_correct_after_mutation(self):
        lst = LinkedList()
        lst.push(31)
        self.assertEqual(len(lst), 1)
        lst.unshift(43)
        self.assertEqual(len(lst), 2)
        lst.shift()
        self.assertEqual(len(lst), 1)
        lst.pop()
        self.assertEqual(len(lst), 0)

    def test_popping_to_empty_doesn_t_break_the_list(self):
        lst = LinkedList()
        lst.push(41)
        lst.push(59)
        lst.pop()
        lst.pop()
        lst.push(47)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.pop(), 47)

    def test_shifting_to_empty_doesn_t_break_the_list(self):
        lst = LinkedList()
        lst.push(41)
        lst.push(59)
        lst.shift()
        lst.shift()
        lst.push(47)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.shift(), 47)

    def test_deletes_the_only_element(self):
        lst = LinkedList()
        lst.push(61)
        lst.delete(61)
        self.assertEqual(len(lst), 0)

    def test_deletes_the_element_with_the_specified_value_from_the_list(self):
        lst = LinkedList()
        lst.push(71)
        lst.push(83)
        lst.push(79)
        lst.delete(83)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst.pop(), 79)
        self.assertEqual(lst.shift(), 71)

    def test_deletes_the_element_with_the_specified_value_from_the_list_re_assigns_tail(
        self,
    ):
        lst = LinkedList()
        lst.push(71)
        lst.push(83)
        lst.push(79)
        lst.delete(83)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst.pop(), 79)
        self.assertEqual(lst.pop(), 71)

    def test_deletes_the_element_with_the_specified_value_from_the_list_re_assigns_head(
        self,
    ):
        lst = LinkedList()
        lst.push(71)
        lst.push(83)
        lst.push(79)
        lst.delete(83)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst.shift(), 71)
        self.assertEqual(lst.shift(), 79)

    def test_deletes_the_first_of_two_elements(self):
        lst = LinkedList()
        lst.push(97)
        lst.push(101)
        lst.delete(97)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.pop(), 101)

    def test_deletes_the_second_of_two_elements(self):
        lst = LinkedList()
        lst.push(97)
        lst.push(101)
        lst.delete(101)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.pop(), 97)

    def test_delete_does_not_modify_the_list_if_the_element_is_not_found(self):
        lst = LinkedList()
        lst.push(89)
        lst.delete(103)
        self.assertEqual(len(lst), 1)

    def test_deletes_only_the_first_occurrence(self):
        lst = LinkedList()
        lst.push(73)
        lst.push(9)
        lst.push(9)
        lst.push(107)
        lst.delete(9)
        self.assertEqual(len(lst), 3)
        self.assertEqual(lst.pop(), 107)
        self.assertEqual(lst.pop(), 9)
        self.assertEqual(lst.pop(), 73)

    # Additional tests for this track

    def test_hi(self):
        lst = LinkedList()
        lst.pop()
