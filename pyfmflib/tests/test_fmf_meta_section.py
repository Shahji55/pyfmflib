# -*- coding: utf-8 -*-
"""This is the test class for FMF meta section"""
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

import pytest
from pyfmflib.tests.fmf_test_base import FmfTestBase
from pyfmflib.pyfmflib.fmf import FMF, UndefinedObject, MultipleKey, \
    MissingSubmission, ForbiddenSubmission


class TestFmfMetaSection(FmfTestBase):
    """Class containing the tests for FMF meta section"""
    def setup(self):
        """Setup the empty fmf object"""
        super(TestFmfMetaSection, self).__init__()

#   Tests for add_meta_section
    def test_add_meta_section(self):
        """Add meta section by name"""
        self.fmf_object.add_meta_section('Meta Section Name')
        assert isinstance(self.fmf_object, FMF)
        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1
        meta_section = self.fmf_object.meta_sections[0]
        assert meta_section.name == 'Meta Section Name'

    def test_add_meta_sec_inval_name(self):
        """Add meta section by invalid name (* at start)"""
        # pylint: disable=no-member
        with pytest.raises(ForbiddenSubmission):
            # pylint: enable=no-member
            self.fmf_object.add_meta_section('*Meta Section Name')

    def test_add_meta_sec_exist_name(self):
        """Add meta section with already existing name"""
        self.fmf_object.add_meta_section('Meta Section Name')
        assert len(self.fmf_object.meta_sections) != 2
        # pylint: disable=no-member
        with pytest.raises(MultipleKey):
            # pylint: enable=no-member
            self.fmf_object.add_meta_section('Meta Section Name')

    def test_add_meta_sec_no_param(self):
        """Add meta section without name parameter"""
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

    def test_get_meta_sec_limit_iter(self):
        """Test limit of getting meta sections iteratively"""
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
        """Test getting meta section by mixed calls"""
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
