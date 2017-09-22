import pytest
import numpy
import unittest

#from nose.tools import assert_equal

from API.Meta_section import Meta_section
from API.Fmf import FMF
from API.Table import Table
from API.Meta_section import Meta_section_entry

class Test_Table:

    def setup(self):
        self.table = Table('Name', 'Symbol')

    def test_create_table(self):
        assert self.table is not None

    def test_table_object(self):
        assert isinstance(self.table, Table)

#    def test_table_with_arguments(self):

        # Specifying less arguments
    #    create_table_object('Name')

        # Specifying the minimum 2 arguments
#        Table.initialize(self.table)

#        assert Table is not None

    def test_add_table_with_data(self):
        fmf_object = FMF()

        mse1 = Meta_section_entry('voltage', 'V [V]')
        ms2 = Meta_section_entry('current', 'I(V) [A]')

        self.table.data_definitions = [mse1, ms2]
        self.table.data = numpy.array([[1, 2], [3, 4], [5, 6]], numpy.int32)
        self.table.no_rows = 3
        self.table.no_columns = 2

        fmf_object.table_sections.append(self.table)

        assert fmf_object is not None

    def test_get_table(self):

        symbol = 'Symbol'
#        fmf_object = FMF()

#        fmf_object.table_sections = [
#            Table.initialize('Table Name', 'Table Symbol',
#                             data_definitions=[
#                                 Meta_section.Meta_section_entry.initialize('voltage', 'V [V]'),
#                                 Meta_section.Meta_section_entry.initialize('current', 'I(V) [A]')],
#
#                             no_columns=2,
#                             no_rows=3,
#
#                             data=numpy.array([[1, 2], [3, 4], [5, 6]], numpy.int32)
#                             )
#            ]

        fmf_object = FMF()

        mse1 = Meta_section_entry('voltage', 'V [V]')
        ms2 = Meta_section_entry('current', 'I(V) [A]')

        self.table.data_definitions = [mse1, ms2]
        self.table.data = numpy.array([[1, 2], [3, 4], [5, 6]], numpy.int32)
        self.table.no_rows = 3
        self.table.no_columns = 2

        fmf_object.table_sections.append(self.table)

        self.table.name = 'Name'
        self.table.symbol = 'Symbol'

        assert fmf_object is not None

    def test_get_table_by_symbol(self):

        symbol = 'Symbol'
        self.table.s = 'Symbol'

        assert self.table.s == symbol

