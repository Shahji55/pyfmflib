# -*- coding: utf-8 -*-
"""This is test class for the header, comment and verify methods of FMF"""
# Copyright (c) 2014 - 2018, Rectorate of the University of Freiburg
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

import numpy
from tests.fmf_test_base import FmfTestBase
from pyfmflib.fmf import FMF


class TestFmfBasics(FmfTestBase):
    """Class containing the tests for header, comment and verify methods
    of FMF"""

    def setup(self):
        """Setup the empty fmf object"""
        super(TestFmfBasics, self).__initialize__()

#   Tests for initialize
    def test_initialize_empty(self):
        """Initialize empty FMF object"""
        fmf = self.fmf_object.initialize()
        assert fmf is not None
        assert isinstance(fmf, FMF)

    def test_initialize_reference(self):
        """Initialize with mandatory parameters only"""
        fmf = self.fmf_object.initialize('test title', 'me',
                                         'aldebaran, universe',
                                         '1970-01-01')
        assert fmf is not None
        assert isinstance(fmf, FMF)
        assert len(fmf.meta_sections) == 1
        ref = fmf.meta_sections[0]
        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'

    def test_initialize_reference_full(self):
        """Initialize with all parameters"""
        fmf = self.fmf_object.initialize('test title', 'me',
                                         'aldebaran, universe',
                                         '1970-01-01',
                                         'tux@example.com')
        assert fmf is not None
        assert isinstance(fmf, FMF)
        assert len(fmf.meta_sections) == 1
        ref = fmf.meta_sections[0]
        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'
        assert ref.contact == 'tux@example.com'

#   Tests for set_header using generator
    def _check_set_header(self, mask):
        """Set header parameter values according to mask"""
        encoding = None
        comment_char = None
        separator = None
        misc_params = None
        if mask & 0x01:
            encoding = 'iso-8859-1'
        if mask & 0x02:
            comment_char = ','
        if mask & 0x04:
            separator = '-'

#       Commented out code for misc_params because structure in API undefined
#       if mask & 0x08:
#           misc_params = data = [('space_char', '\s')]

        header = self.fmf_object.set_header(
            encoding, comment_char, separator, misc_params)
        assert header is not None
        if mask & 0x01:
            assert header.encoding == encoding
        else:
            assert header.encoding == 'utf-8'
        if mask & 0x02:
            assert header.comment_char == comment_char
        else:
            assert header.comment_char == ';'
        if mask & 0x04:
            assert header.separator == separator
        else:
            assert header.separator == '\t'

#       Commented out code for misc_params because structure in API undefined
#        if mask & 0x08:
#            assert header.misc_params == misc_params
#        else:
#            assert header.misc_params is None

    def test_header(self):
        """Set header using generator"""
        for mask in range(16):
            yield self._check_set_header(mask)

#   Tests for set header without using generator
    def test_set_header(self):
        """Set header with encoding, comment_char and separator"""
        header = self.fmf_object.set_header('utf-9', ',', '\n', None)
        assert header is not None
        assert self.fmf_object.header is not None
        assert header.encoding == 'utf-9'
        assert header.comment_char == ','
        assert header.separator == '\n'
        assert header.misc_params is None

    def test_set_header_full(self):
        """Set header with encoding, comment_char,separator and
        misc_params key value pairs"""
        misc_params = {'fmf_version': 1.0, 'space_char': r'\s'}
        header = self.fmf_object.set_header('utf-9', ',', '\n', misc_params)
        assert header is not None
        assert self.fmf_object.header is not None
        assert header.encoding == 'utf-9'
        assert header.comment_char == ','
        assert header.separator == '\n'
        assert header.misc_params['fmf_version'] == 1.0
        assert header.misc_params['space_char'] == r'\s'

    def test_set_header_default_args(self):
        """Set header with default arguments"""
        header = self.fmf_object.set_header(None, None, None, None)
        assert header is not None
        assert self.fmf_object.header is not None
        assert header.encoding == 'utf-8'
        assert header.comment_char == ';'
        assert header.separator == '\t'
        assert header.misc_params is None

    def test_get_header(self):
        """Get the header object"""
        header = self.fmf_object.set_header('utf-9', ',', '\n', None)
        assert header is not None
        assert self.fmf_object.header is not None
        header_returned = self.fmf_object.get_header()
        assert header_returned is not None
        assert header_returned.encoding == 'utf-9'
        assert header_returned.comment_char == ';'
        assert header_returned.separator == '\t'
        assert header_returned.misc_params is None

#   Test for add_comment
    def test_add_comment(self):
        """Add the comment with comment string"""
        comment = self.fmf_object.add_comment('Text')
        assert comment is not None
        assert comment.text == 'Text'
        assert comment.location is not None

#   Tests for verify
    def test_verify_correct_table_obj(self):
        """Verify number of rows and columns of table"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        table_added.no_rows = 5
        table_added.no_columns = 2
        table_added.data_definitions = ['Num1', 'Num2']
        # pylint: disable=no-member
        table_added.data = numpy.matrix([[1, 2], [3, 4], [5, 6], [7, 8],
                                         [9, 10]])
        # pylint: enable=no-member
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        verify_result = self.fmf_object.verify()
        assert verify_result is True

    def test_verify_incorrect_table_obj(self):
        """Verify incorrect table object"""
        table_added = self.fmf_object.add_table('Table Name', 'Table Symbol')
        table_added.no_rows = 5
        table_added.no_columns = 2
        table_added.data_definitions = ['Num1', 'Num2']
        # pylint: disable=no-member
        table_added.data = numpy.matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
        # pylint: enable=no-member
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 1
        verify_result = self.fmf_object.verify()
        assert verify_result is False

    def test_verify_table_name_and_sym(self):
        """Verify the name and symbol of table"""
        self.fmf_object.add_table('Table Name', 'Table Symbol')
        self.fmf_object.add_table('Table Name', 'Table Symbol')
        assert self.fmf_object.table_sections is not None
        assert len(self.fmf_object.table_sections) == 2
        verify_result = self.fmf_object.verify()
        assert verify_result is False

    def test_verify_correct_metasec_obj(self):
        """Verify the name of metasection object"""
        self.fmf_object.add_meta_section('Meta Section Name')
        self.fmf_object.add_meta_section('Meta Section Name 2')
        assert len(self.fmf_object.meta_sections) == 2
        verify_result = self.fmf_object.verify()
        assert verify_result is True

    def test_verify_incor_metasec_obj(self):
        """Verify incorrect meta section object"""
        self.fmf_object.add_meta_section('Meta Section Name')
        self.fmf_object.add_meta_section('Meta Section Name')
        assert len(self.fmf_object.meta_sections) == 2
        verify_result = self.fmf_object.verify()
        assert verify_result is False

    def test_verify_cor_metasec_keys(self):
        """Verify the uniqueness of keys within meta section object"""
        meta_section = self.fmf_object.add_meta_section('Measurement')
        meta_section.add_entry('room temperature', r'T = (292 \pm 1) K')
        meta_section.add_entry('current', r'I = (171 \pm 1) mA')
        meta_section.add_entry('solution', 'sodium hydroxide')
        assert len(self.fmf_object.meta_sections) == 1
        verify_result = self.fmf_object.verify()
        assert verify_result is True

    def test_verify_incor_metasec_keys(self):
        """Verify the duplication of keys within meta section object"""
        meta_section = self.fmf_object.add_meta_section('Measurement')
        meta_section.add_entry('room temperature', r'T = (292 \pm 1) K')
        meta_section.add_entry('solution', 'hydrogen oxide')
        meta_section.add_entry('solution', 'sodium hydroxide')
        assert len(self.fmf_object.meta_sections) == 1
        verify_result = self.fmf_object.verify()
        assert verify_result is False
