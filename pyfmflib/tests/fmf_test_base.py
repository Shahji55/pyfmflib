# -*- coding: utf-8 -*-
"""This is the test class for FMF"""
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

from pyfmflib.pyfmflib.fmf import FMF, UndefinedObject, MultipleKey, \
    MissingSubmission, SpecificationViolation, ForbiddenSubmission
import numpy
import pytest


class FmfTestBase(object):
    """Class containing the setup and the tests for methods of FMF object"""
    def setup(self):
        """Set up an empty FMF object"""

        # pylint: disable=attribute-defined-outside-init
        self.fmf_object = FMF()
        # pylint: enable=attribute-defined-outside-init

#   Tests for initialize
    def test_initialize_empty(self):
        """Initialize empty FMF object"""
#        fmf0 = FMF()
        fmf = self.fmf_object.initialize()
        assert fmf is not None
        assert isinstance(fmf, FMF)
        # assert fmf0 == fmf

    def test_initialize_reference(self):
        """Initialize with mandatory parameters only"""
        fmf = self.fmf_object.initialize('test title', 'me',
                                         'aldebaran, universe',
                                         '1970-01-01')
        print "Length of fmf.meta_sections is: ", len(fmf.meta_sections)
        assert fmf is not None
        assert isinstance(fmf, FMF)
#       print "Length of fmf.meta_sectons is: " , len(fmf.meta_sections)
        assert len(fmf.meta_sections) == 1
        ref = fmf.meta_sections[0]

        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'

        # assert ref.entries == ['test title', 'me', \
        # 'aldebaran, universe', '1970-01-01']

    def test_initialize_reference_full(self):
        """Initialize with all parameters"""
        fmf = self.fmf_object.initialize('test title', 'me',
                                         'aldebaran, universe',
                                         '1970-01-01',
                                         'tux@example.com')

        print "Length of fmf.meta_sectons is: ", len(fmf.meta_sections)

        assert fmf is not None
        assert isinstance(fmf, FMF)
        assert len(fmf.meta_sections) == 1
        ref = fmf.meta_sections[0]
        print ref.title

        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'
        assert ref.contact == 'tux@example.com'

#       assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01', \
#                                   'tux@example.com']

#   Tests for set_reference
    def test_set_reference(self):
        """Set reference section with mandatory parameters"""
        # fmf = FMF()
        self.fmf_object.set_reference('test title', 'me',
                                      'aldebaran, universe',
                                      '1970-01-01', None)
#        assert fmf != None
#        assert isinstance(fmf, FMF)
#        assert fmf.meta_sections is not None
#        assert len(fmf.meta_sections) == 1
#        ref = fmf.meta_sections[0]

        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1

        ref = self.fmf_object.meta_sections[0]

        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'

#       assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01']

    def test_set_reference_full(self):
        """Set reference section with all parameters"""
        # fmf = FMF()
        self.fmf_object.set_reference('test title', 'me',
                                      'aldebaran, universe',
                                      '1970-01-01',
                                      'tux@example.com')
        # assert fmf != None
        # assert isinstance(fmf, FMF)
        # assert fmf.meta_sections is not None
        # assert len(fmf.meta_sections) == 1
        # ref = fmf.meta_sections[0]

        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1

        ref = self.fmf_object.meta_sections[0]

        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'
        assert ref.contact == 'tux@example.com'

#       assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01', \
#                                    'tux@example.com']

        self.fmf_object.set_reference('test title 2', 'me',
                                      'earth, universe',
                                      '1970-01-01',
                                      'bla@example.com')
        assert len(self.fmf_object.meta_sections) == 1
        ref = self.fmf_object.meta_sections[0]

        assert ref.title == 'test title 2'
        assert ref.creator == 'me'
        assert ref.place == 'earth, universe'
        assert ref.created == '1970-01-01'
        assert ref.contact == 'bla@example.com'

        # assert ref.entries == ['Why to always carry a towel', 'me', \
        #                                 'earth, universe', '1970-01-01', \
        #                                  'bla@example.com']

#   Tests for add_meta_section
    def test_add_meta_section(self):
        """Add meta section by name"""
#       fmf = FMF()
        self.fmf_object.add_meta_section('Meta Section Name')

        assert isinstance(self.fmf_object, FMF)
        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1
        meta_section = self.fmf_object.meta_sections[0]

        assert meta_section.name == 'Meta Section Name'

#        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
#        self.fmf_object.meta_sections.append(meta_section)

    def test_add_meta_sec_inval_name(self):
        """Add meta section by invalid name (* at start)"""

        # pylint: disable=no-member
        with pytest.raises(ForbiddenSubmission):
            # pylint: enable=no-member
            self.fmf_object.add_meta_section('*Meta Section Name')

    def test_add_meta_sec_exist_name(self):
        """Add meta section with already existing name"""
        self.fmf_object.add_meta_section('Meta Section Name')

#        fmf.add_meta_section('Meta Section Name')

        assert len(self.fmf_object.meta_sections) != 2

        # pylint: disable=no-member
        with pytest.raises(MultipleKey):
            # pylint: enable=no-member
            self.fmf_object.add_meta_section('Meta Section Name')

    def test_add_meta_sec_no_param(self):
        """Add meta section without name parameter"""
#        fmf.add_meta_section()

        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            # pylint: disable=no-value-for-parameter
            self.fmf_object.add_meta_section()
            # pylint: enable=no-value-for-parameter

#   Tests for get_meta_section
    def test_get_meta_section_by_name(self):
        """Get meta section by name"""
        meta_section = self.fmf_object.add_meta_section('Meta Section Name')

        meta_section_returned = self.fmf_object.get_meta_section(
            'Meta Section Name')

        assert meta_section_returned is not None
        assert meta_section_returned == meta_section

    def test_get_meta_sec_invalid_name(self):
        """Get meta section by an invalid name"""
        meta_section = self.fmf_object.add_meta_section('Meta Section Name')

        meta_section_returned = self.fmf_object.get_meta_section(
            'Invalid Meta Section Name')

        assert meta_section is not None
        assert meta_section_returned != meta_section

    def test_get_meta_sec_iteratively(self):
        """Get meta section iteratively i.e without specifying name"""
        meta_section = self.fmf_object.add_meta_section('Meta Section Name')

        meta_section_returned = self.fmf_object.get_meta_section(None)

        assert meta_section is not None
        assert meta_section_returned is not None
        assert meta_section_returned == meta_section

    def test_get_meta_section_limit(self):
        """Add 2 meta sections, get them iteratively;
        on 3rd call exception is raised"""
        meta_section = self.fmf_object.add_meta_section('Meta Section Name')

        meta_section2 = self.fmf_object.add_meta_section('Meta Section Name 2')

        meta_section_returned = self.fmf_object.get_meta_section(None)

        assert meta_section is not None
        assert meta_section_returned is not None
        assert meta_section_returned == meta_section

        meta_section_returned2 = self.fmf_object.get_meta_section(None)

        assert meta_section2 is not None
        assert meta_section_returned2 is not None
        assert meta_section_returned2 == meta_section2

        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_meta_section(None)

    def test_get_meta_sec_mixed_calls(self):
        """First get meta section by name; then getting iteratively
        raises an exception"""
        meta_section1 = self.fmf_object.add_meta_section('Meta Section Name')

        meta_section2 = self.fmf_object.add_meta_section('Meta Section Name 2')

        assert meta_section1 is not None
        assert meta_section2 is not None

        meta_section_returned1 = self.fmf_object.get_meta_section(
            'Meta Section Name')

        assert meta_section_returned1 == meta_section1

        # pylint: disable=no-member
        with pytest.raises(UndefinedObject):
            # pylint: enable=no-member
            self.fmf_object.get_meta_section(None)

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
        """Adding a table with already existing name and symbol
        should give exception"""
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
        """After adding table with name and symbol, adding second table
         without both should give exception"""
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
        """Initially table was added with name and symbol;
        then get it iteratively"""
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
        """Initially table was added without name and symbol;
        then get it iteratively"""
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

    def test_get_table_no_further(self):
        """Add 2 tables, get them both iteratively and on 3rd call
        exception is raised"""
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
        """Add 2 tables, get table by symbol first and then iteratively;
        error raised"""
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

#   Tests for set_header
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

#        if mask & 0x08:
#            misc_params = data = [('space_char', '\s')]

        header = self.fmf_object.set_header(
            encoding, comment_char, separator, misc_params)

        assert header is not None
        # assert self.fmf_object.header is not None

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

#        if mask & 0x08:
#            assert header.misc_params == misc_params
#        else:
#            assert header.misc_params is None

    def test_header(self):
        """Set header using generator"""
        for mask in range(16):
            yield self._check_set_header(mask)

    #
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
