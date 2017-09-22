#import nose
import pytest
import inspect
import numpy
import unittest

from API.Fmf import FMF

class Test_Fmf:

    def setup(self):
        self.fmf_object = FMF()

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

    def test_add_meta_section_invalid_name(self):
        FMF.add_meta_section(self.fmf_object, 'Name')

    def test_add_meta_section_existing_name(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
        self.fmf_object.meta_sections.append(meta_section2)

    def test_create_fmf_with_table(self):
        self.fmf_object.table_sections.append(FMF.add_table(self.fmf_object, 'Table Name', 'Table Symbol'))

        assert self.fmf_object.table_sections is not None

        assert len(self.fmf_object.table_sections) > 0

    # Test to get the meta section by a valid name
    def test_get_meta_section_by_name(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

#        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
#        self.fmf_object.meta_sections.append(meta_section2)

#        meta_section3 = FMF.add_meta_section(self.fmf_object, 'Name3')
#        self.fmf_object.meta_sections.append(meta_section3)

        meta_section_returned = FMF.get_meta_section(self.fmf_object, 'Name')
        print meta_section_returned.name

        print "Method called: ", FMF.get_meta_section_by_name.called

        assert meta_section_returned is not None

        assert meta_section_returned.name == meta_section.name

    '''    # Test to get the meta section by an invalid name
    def test_get_meta_section_invalid_name(self):
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
        self.fmf_object.meta_sections.append(meta_section2)

        meta_section3 = FMF.add_meta_section(self.fmf_object, 'Name3')
        self.fmf_object.meta_sections.append(meta_section3)

        meta_section_returned = FMF.get_meta_section_by_name(self.fmf_object, 'Name')
        print meta_section_returned.name

        print "Method called: " , FMF.get_meta_section_by_name.called

        meta_section_returned2 = FMF.get_meta_section_by_name(self.fmf_object, 'Name2')
        print meta_section_returned2.name

        meta_section_returned3 = FMF.get_meta_section_by_name(self.fmf_object, 'Name3')
        print meta_section_returned3.name

        assert meta_section_returned is not None

        assert meta_section_returned.name == meta_section.name

        assert meta_section_returned2 is not None

        assert meta_section_returned3 is not None '''

    # Test to the meta section by iteration
    def test_get_meta_section_by_iteration(self):
        print "TESTING ITERATION ONLY ... "
        meta_section = FMF.add_meta_section(self.fmf_object, 'Name')
        self.fmf_object.meta_sections.append(meta_section)

        meta_section2 = FMF.add_meta_section(self.fmf_object, 'Name2')
        self.fmf_object.meta_sections.append(meta_section2)

        meta_section3 = FMF.add_meta_section(self.fmf_object, 'Name3')
        self.fmf_object.meta_sections.append(meta_section3)

        for index, item in enumerate(self.fmf_object.meta_sections):
            print ("Index is: ", index)
            print ("Item is: ", item.name)

        meta_section_returned = FMF.get_meta_section(self.fmf_object, None)

        print meta_section_returned.name

        meta_section_returned2 = FMF.get_meta_section(self.fmf_object, None)

        print meta_section_returned2.name

#        meta_section_returned3 = FMF.get_meta_section(self.fmf_object, None)

#        print meta_section_returned3.name

        assert meta_section_returned is not None

        assert  meta_section_returned2 is not None

    # Test to get the meta section by mixed calls
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


        meta_section_returned = FMF.get_meta_section(self.fmf_object, 'Name')

        print meta_section_returned.name

        meta_section_returned2 = FMF.get_meta_section(self.fmf_object, None)

        print meta_section_returned2.name

        assert meta_section_returned2 is None







