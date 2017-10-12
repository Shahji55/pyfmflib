# -*- coding: utf-8 -*-

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


import pytest
import numpy

from pyfmflib.pyfmflib.meta_section import Meta_section_entry
from pyfmflib.pyfmflib.table import FMFTable
from pyfmflib.pyfmflib.fmf import FMF

class test_table():

    def setup(self):
        self.table = FMFTable('Name', 'Symbol')

    def test_create_table(self):
        assert self.table is not None

    def test_table_object(self):
        assert isinstance(self.table, FMFTable)

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
