#!/usr/bin/python3
""" test console """
import os
import sys
from console import HBNBCommand
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestConsole(TestCase):

    def test_good1(self):
        """best1"""
        with patch('sys.stdout', new=StringIO()) as prog:
            HBNBCommand().onecmd("create State")
        msg = prog.getvalue()[:-1]
        self.assertEqual(type(msg), str)

    def test_good2(self):
        """best2"""
        with patch('sys.stdout', new=StringIO()) as prog:
            HBNBCommand().onecmd('create State name="Texas"')
            HBNBCommand().onecmd('all State')
        msg = prog.getvalue()[:-1]
        self.assertTrue("'name': 'Texas'" in msg)
    def test_good3(self):
        """ best3"""
        with patch('sys.stdout', new=StringIO()) as prog:
            HBNBCommand().onecmd('create Place nuber_bathrms=2 price=1.345')
            HBNBCommand().onecmd('all Place')
        msg = prog.getvalue()[:-1]
        self.assertTrue("'nuber_bathrms': 2" in msg)
        self.assertTrue("'price': 1.345" in msg)

    def test_noname(self):
        """missing class name"""
        with patch('sys.stdout', new=StringIO()) as prog:
            HBNBCommand().onecmd("create")
        msg = prog.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def test_worngname(self):
        """ wrong  name of classe"""
        with patch('sys.stdout', new=StringIO()) as prog:
            HBNBCommand().onecmd("create bz")
        msg = prog.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")
