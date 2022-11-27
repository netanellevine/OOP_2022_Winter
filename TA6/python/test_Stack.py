import unittest
from unittest import TestCase

from Lesson5.Stack import Stack


class TestStack(unittest.TestCase):
    def create_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        return s

    def test_pop_regular_pop(self):
        s = self.create_stack()
        self.assertEqual(5, s.pop())

    """
    Good explanation for with keyword in python.
    https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
    """

    def test_pop_empty_case(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.pop()

    def test_pop_regular_pop_not_raises(self):
        s = self.create_stack()
        try:
            s.pop()
            self.assertEqual(1, 1)
        except Exception:
            self.fail()

    def test_push_empty_case(self):
        s = Stack()
        l = [1]
        s.push(1)
        self.assertEqual(l, s.elements)

    def test_push_regular_case(self):
        s = self.create_stack()
        l = [6, 5, 4, 3, 2, 1]
        s.push(6)
        if len(s) != len(l):
            self.fail()
        for i in range(len(s)):
            self.assertEqual(s.elements[i], l[i])

    def test_top_empty_case(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.top()

    def test_top_regular_case(self):
        s = self.create_stack()
        self.assertEqual(5, s.top())

    def test_len_empty_case(self):
        s = Stack()
        self.assertEqual(0, s.counter)

    def test_len_regular_case(self):
        s = self.create_stack()
        self.assertEqual(5, s.top())

    def test_constructor(self):
        s1 = Stack()
        self.assertIsInstance(s1, Stack)

    def test_constructor2(self):
        l = []
        self.assertIsInstance(l, Stack)
