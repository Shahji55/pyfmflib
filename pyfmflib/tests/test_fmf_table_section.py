# -*- coding: utf-8 -*-
"""This is the test class for FMF table section"""
# Copyright (c) 2014 - 2017, Rectorate of the University of Freiburg
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the Freiburg Materials Research Center,
#   University of Freiburg nor the names of its contributors may be used to
#   endorse or promote products derived from this software without specific
#   prior written permission.
#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pyfmflib.pyfmflib.fmf import UndefinedObject, MultipleKey, \
    MissingSubmission, SpecificationViolation
import pytest
from pyfmflib.tests.fmf_test_base import FmfTestBase


class TestFmfTableSection(FmfTestBase):
    """Class containing the tests for FMF table section"""
    def setup(self):
        """Setup the empty fmf object"""
        super(TestFmfTableSection, self).__init__()

#   Tests for add_table
    def test_add_table_by_name_symbol(self):
        """Add a table with name and symbol"""
        self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table = self.fmf_object.table_sections[0]
        assert table.name == 'Table Name'
        assert table.symbol == 'Table Symbol'

    def test_add_table_exist_name_sym(self):
        """Test adding a table with already existing name and symbol"""
        self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table = self.fmf_object.table_sections[0]
        assert table.name == 'Table Name'
        assert table.symbol == 'Table Symbol'
        # pylint: disable=no-member
        with pytest.raises(MultipleKey):
            # pylint: enable=no-member
            self.fmf_object.add_table('Table Name', 'Table Symbol')

    def test_add_table_no_name_sym(self):
        """Add a table without name and symbol"""
        self.fmf_object.add_table(None, None)
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table = self.fmf_object.table_sections[0]
        assert table.name is None
        assert table.symbol is None

    def test_add_table_with_name_only(self):
        """Add a table with name and without symbol"""
        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            self.fmf_object.add_table('Table Name', None)

    def test_add_table_with_symbol_only(self):
        """Add a table without name and with symbol"""
        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            self.fmf_object.add_table(None, 'Table Symbol')

    def test_add_table_missing_param(self):
        """Test adding second table without name and symbol"""
        self.fmf_object.add_table('Table Name', 'Table Symbol')
        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            self.fmf_object.add_table(None, None)

    def test_add_table_spec_violate(self):
        """Adding second table without name and symbol should give exception"""
        self.fmf_object.add_table(None, None)
        # pylint: disable=no-member
        with pytest.raises(SpecificationViolation):
            # pylint: enable=no-member
            self.fmf_object.add_table(None, None)

#   Tests for get_table
    def test_get_table_by_symbol(self):
        """Get table by valid symbol"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert table_added is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table_returned = self.fmf_object.get_table('Table Symbol')
        assert table_returned is not None
        assert table_returned == table_added

    def test_get_table_invalid_sym(self):
        """Get table by invalid symbol"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert table_added is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table_returned = self.fmf_object.get_table('Invalid Table Symbol')
        assert table_returned != table_added

    def test_get_table_iterative_sym(self):
        """Test get table iteratively with existing table symbol"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert table_added is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table_returned = self.fmf_object.get_table(None)
        assert table_returned is not None
        assert table_returned == table_added
        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_table(None)

    def test_get_table_iterate_no_sym(self):
        """Test get table iteratively without existing table symbol"""
        table_added = self.fmf_object.add_table(None, None)
        assert table_added is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        table_returned = self.fmf_object.get_table(None)
        assert table_returned is not None
        assert table_returned == table_added
        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_table(None)

    def test_get_table_no_further_iter(self):
        """Test limit of getting table iteratively """
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        table_added_2 = self.fmf_object.add_table(
            'Table Name 2', 'Table Symbol 2')
        assert table_added is not None
        assert table_added_2 is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 2
        table_returned = self.fmf_object.get_table(None)
        assert table_returned is not None
        assert table_returned == table_added
        table_returned_2 = self.fmf_object.get_table(None)
        assert table_returned_2 is not None
        assert table_returned_2 == table_added_2
        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_table(None)

    def test_get_table_mixed_calls(self):
        """Test get table in case of mixed calls"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        table_added_2 = self.fmf_object.add_table(
            'Table Name 2', 'Table Symbol 2')
        assert table_added is not None
        assert table_added_2 is not None
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 2
        table_returned = self.fmf_object.get_table(None)
        assert table_returned is not None
        assert table_returned == table_added
        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_table(None)
