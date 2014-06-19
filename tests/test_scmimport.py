import unittest


class TestScmimport(unittest.TestCase):
    def test_assignment(self):
        """Verify import of assignment.scm.

        The following is the contents of the file:

        (define x 23)
        (define y 15)
        (define z 0)
        (define t (+ 2 3))
        (define a (if (= 2 3) (* 3 3) (* 4 4)))
        """
        # import the module.
        import scmimport
        import assignment

        # Verify the contents of the module.
        self.assertEqual(assignment.x, 23)
        self.assertEqual(assignment.y, 15)
        self.assertEqual(assignment.z, 0)
        self.assertEqual(assignment.t, 5)
        self.assertEqual(assignment.a, 16) 


if __name__=='__main__':
    unittest.main()
