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


#import nose
import pytest
import inspect
import numpy
import unittest

import sys
print sys.path
from pyfmflib.pyfmflib.fmf import FMF
from pyfmflib.pyfmflib.table import FMFTable

class Test_Fmf:

    def setup(self):
        self.fmf_object = FMF()

    # strict API example
    def test_initialize_empty(self):
            fmf0 = FMF()
            fmf = fmf0.initialize()
            assert fmf is not None
            assert isinstance(fmf, FMF)
 #           assert fmf0 == fmf

    def test_initialize_reference(self):

            fmf = FMF().initialize('test title', 'me', \
                                   'aldebaran, universe', '1970-01-01')
            print "Length of fmf.meta_sectons is: ", len(fmf.meta_sections)
            assert fmf != None
            assert isinstance(fmf, FMF)
#            print "Length of fmf.meta_sectons is: " , len(fmf.meta_sections)
            assert len(fmf.meta_sections) == 1
            ref = fmf.meta_sections[0]

            assert ref.title == 'test title'
            assert ref.creator == 'me'
            assert ref.place == 'aldebaran, universe'
            assert ref.created == '1970-01-01'

#            assert ref.entries == ['test title', 'me', \
 #                                  'aldebaran, universe', '1970-01-01']

    def test_initialize_reference_full(self):
            fmf = FMF().initialize('test title', 'me', \
                                   'aldebaran, universe', '1970-01-01', \
                                   'tux@example.com')

            print "Length of fmf.meta_sectons is: ", len(fmf.meta_sections)

            assert fmf != None
            assert isinstance(fmf, FMF)
            assert len(fmf.meta_sections) == 1
            ref = fmf.meta_sections[0]
            print ref.title

            assert ref.title == 'test title'
            assert ref.creator == 'me'
            assert ref.place == 'aldebaran, universe'
            assert ref.created == '1970-01-01'
            assert ref.contact == 'tux@example.com'

#            assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01', \
#                                   'tux@example.com']

    def test_set_reference(self):
            fmf = FMF()
            fmf.set_reference('test title', 'me', \
                              'aldebaran, universe', '1970-01-01', None)
            assert fmf != None
            assert isinstance(fmf, FMF)
            assert fmf.meta_sections is not None
            assert len(fmf.meta_sections) == 1
            ref = fmf.meta_sections[0]

            assert ref.title == 'test title'
            assert ref.creator == 'me'
            assert ref.place == 'aldebaran, universe'
            assert ref.created == '1970-01-01'

#            assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01']

    def test_set_reference_full(self):
            fmf = FMF()
            fmf.set_reference('test title', 'me', \
                              'aldebaran, universe', '1970-01-01', \
                              'tux@example.com')
            assert fmf != None
            assert isinstance(fmf, FMF)
            assert fmf.meta_sections is not None
            assert len(fmf.meta_sections) == 1
            ref = fmf.meta_sections[0]

            assert ref.title == 'test title'
            assert ref.creator == 'me'
            assert ref.place == 'aldebaran, universe'
            assert ref.created == '1970-01-01'
            assert ref.contact == 'tux@example.com'

#            assert ref.entries == ['test title', 'me', \
#                                   'aldebaran, universe', '1970-01-01', \
#                                    'tux@example.com']

            fmf.set_reference('test title 2', 'me', \
                              'earth, universe', '1970-01-01', \
                              'bla@example.com')
            assert len(fmf.meta_sections) == 1
            ref = fmf.meta_sections[0]

            assert ref.title == 'test title 2'
            assert ref.creator == 'me'
            assert ref.place == 'earth, universe'
            assert ref.created == '1970-01-01'
            assert ref.contact == 'bla@example.com'

 #          assert ref.entries == ['Why to always carry a towel', 'me', \
 #                                  'earth, universe', '1970-01-01', \
 #                                  'bla@example.com']

    def test_add_meta_section(self):

        fmf = FMF()
        fmf.add_meta_section('Meta Section Name')

        assert fmf is not None
        assert isinstance(fmf, FMF)
        assert fmf.meta_sections is not None
        assert len(fmf.meta_sections) == 1
        meta_section = fmf.meta_sections[0]

        assert meta_section.name == 'Meta Section Name'

#        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
#        self.fmf_object.meta_sections.append(meta_section)

    def test_add_meta_section_invalid_name(self):
        fmf = FMF()
        fmf.add_meta_section('*Meta Section Name')

        meta_section = fmf.meta_sections[0]
        print meta_section.name

        assert fmf is not None
        assert len(fmf.meta_sections) != 1

    def test_add_meta_section_existing_name(self):
        fmf = FMF()
        fmf.add_meta_section('Meta Section Name')

        fmf.add_meta_section('Meta Section Name')

        assert fmf is not None
        assert len(fmf.meta_sections) != 2

    def test_get_meta_section_by_name(self):
        fmf = FMF()
        meta_section = fmf.add_meta_section('Meta Section Name')

        meta_section_returned = fmf.get_meta_section('Meta Section Name')

        assert fmf is not None
        assert meta_section_returned is not None
        assert meta_section_returned == meta_section

    def test_get_meta_section_by_invalid_name(self):
        fmf = FMF()
        meta_section = fmf.add_meta_section('Meta Section Name')

        meta_section_returned = fmf.get_meta_section('Invalid Meta Section Name')

        assert fmf is not None
        assert meta_section is not None
        assert meta_section_returned != meta_section

    def test_get_meta_section_iteratively(self):
        fmf = FMF()
        meta_section = fmf.add_meta_section('Meta Section Name')

        meta_section_returned = fmf.get_meta_section(None)

        assert fmf is not None
        assert meta_section is not None
        assert meta_section_returned is not None
        assert meta_section_returned == meta_section

    def test_get_meta_section_mixed_calls(self):
        fmf = FMF()
        meta_section1 = fmf.add_meta_section('Meta Section Name')

        meta_section2 = fmf.add_meta_section('Meta Section Name 2')

        meta_section_returned = fmf.get_meta_section('Meta Section Name')

        assert fmf is not None
        assert meta_section1 is not None
        assert meta_section_returned == meta_section1

        meta_section_returned2 = fmf.get_meta_section(None)

        assert meta_section_returned2 != meta_section2

    '''
    def test_get_table_iteratively(self):
            fmf = FMF()
            table = FMFTable()
            fmf.tables = [table]
            fmftable = fmf.get_table()
            assert fmftable == table
            with pytest.raises(UndefinedObject) as e_info:
                fmf.get_table()

    def test_get_table_by_symbol(self):
            fmf = FMF()
            table = FMFTable().initialize('table', 'tab')
            fmf.tables = [table]
            fmftable = fmf.get_table('tab')
            assert fmftable == table
            with pytest.raises(UndefinedObject) as e_info:
                fmf.get_table('tub')

    def test_get_table_mixed(self):
            fmf = FMF()
            table1 = FMFTable().initialize('table1', 'tab1')
            table2 = FMFTable().initialize('table2', 'tab2')
            fmf.tables = [table1, table2]
            fmftable = fmf.get_table('tab1')
            assert fmftable == table1
            with pytest.raises(AmbigousObject) as e_info:
                fmf.get_table()

    # strict API example
    '''

    '''
    def test_empty_fmf(self):
        assert self.fmf_object is not None

    def test_empty_fmf_instance(self):

        assert isinstance(self.fmf_object, FMF)

    def test_create_fmf_with_reference(self):

        self.fmf_object.reference_section = self.fmf_object.set_reference(self, 'title', 'Creator', 'Created', 'Place')

        self.fmf_object.meta_sections.append(self.fmf_object.reference_section)

        assert self.fmf_object.meta_sections is not None

        assert len(self.fmf_object.meta_sections) > 0
#        assert isinstance(self.fmf_object, Fmf.FMF)

    def test_create_fmf_meta_section(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        assert self.fmf_object.meta_sections is not None

        assert len(self.fmf_object.meta_sections) > 0

    def test_add_meta_section_invalid_name1(self):
        FMF.add_meta_section(self.fmf_object, '*Name')

    def test_add_meta_section_existing_name1(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section2)

    def test_create_fmf_with_table(self):
        self.fmf_object.table_sections.append(FMF.add_table(self.fmf_object, 'Table Name', 'Table Symbol'))

        assert self.fmf_object.table_sections is not None

        assert len(self.fmf_object.table_sections) > 0

    def test_get_meta_section1(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section_returned = FMF.get_meta_section(self.fmf_object, 'Name1')
        print meta_section_returned.name

        assert meta_section_returned is not None

    def test_get_meta_section_by_name(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        #        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
        #        self.fmf_object.meta_sections.append(meta_section2)

        #        meta_section3 = FMF.add_meta_section(self.fmf_object, 'Name3')
        #        self.fmf_object.meta_sections.append(meta_section3)

        meta_section_returned = FMF.get_meta_section_by_name(self.fmf_object, 'Name')
        print meta_section_returned.name

        print "Method called: ", FMF.get_meta_section_by_name.called

        assert meta_section_returned is not None

        assert meta_section_returned.name == meta_section.name

    def test_get_meta_section_invalid_name(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section_returned = FMF.get_meta_section_by_name(self.fmf_object, 'Name')
        print meta_section_returned.name

        print "Method called: ", FMF.get_meta_section_by_name.called

        assert meta_section_returned is not None

        assert meta_section_returned.name == meta_section.name

    def test_get_meta_section_by_iteration(self):
        print "TESTING ITERATION ONLY ... "
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        for index, item in enumerate(self.fmf_object.meta_sections):
            print ("Index is: ", index)
            print ("Item is: ", item.name)

        meta_section_returned = FMF.get_meta_section_by_name(self.fmf_object, None)

        print meta_section_returned.name

        assert meta_section_returned is not None

    def test_get_meta_section_by_mixing_calls(self):

        print "TESTING MIXED CALLS ... "
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
        self.fmf_object.meta_sections.append(meta_section2)

        meta_section3 = FMF.add_meta_section(self.fmf_object, 'Name3')
        self.fmf_object.meta_sections.append(meta_section3)

        for index, item in enumerate(self.fmf_object.meta_sections):
            print ("Index is: ", index)
            print ("Item is: ", item.name)

        meta_section_returned = FMF.get_meta_section_by_name(self.fmf_object, 'Name')

        print meta_section_returned.name

        meta_section_returned2 = FMF.get_meta_section_by_name(self.fmf_object, None)

        print meta_section_returned2.name
    '''



