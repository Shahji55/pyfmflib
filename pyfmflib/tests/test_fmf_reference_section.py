# -*- coding: utf-8 -*-
"""This is the test class for FMF reference section"""
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

from pyfmflib.tests.fmf_test_base import FmfTestBase


class TestFmfReferenceSection(FmfTestBase):
    """Class containing the tests for FMF reference section"""
    def setup(self):
        """Setup the empty fmf object"""
        super(TestFmfReferenceSection, self).__init__()

#   Tests for set_reference
    def test_set_reference(self):
        """Set reference section with mandatory parameters"""
        self.fmf_object.set_reference('test title', 'me',
                                      'aldebaran, universe',
                                      '1970-01-01', None)
        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1
        ref = self.fmf_object.meta_sections[0]
        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'

    def test_set_reference_full(self):
        """Set reference section with all parameters"""
        self.fmf_object.set_reference('test title', 'me',
                                      'aldebaran, universe',
                                      '1970-01-01',
                                      'tux@example.com')
        assert self.fmf_object.meta_sections is not None
        assert len(self.fmf_object.meta_sections) == 1
        ref = self.fmf_object.meta_sections[0]
        assert ref.title == 'test title'
        assert ref.creator == 'me'
        assert ref.place == 'aldebaran, universe'
        assert ref.created == '1970-01-01'
        assert ref.contact == 'tux@example.com'
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
