# -*- coding: utf-8 -*-
"""This is the test base class for FMF"""
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

from pyfmflib.pyfmflib.fmf import FMF

class FmfTestBase(object):
    """Class containing the setup and the tests for methods of FMF object"""
    def __int__(self):
        """Set up an empty FMF object"""
        # pylint: disable=attribute-defined-outside-init
        self.fmf_object = FMF()
        # pylint: enable=attribute-defined-outside-init

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
