# -*- coding: utf-8 -*-
"""This is the test class for FMF reader and writer"""
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

from pyfmflib.pyfmflib.fmf import FMF, MissingSubmission
import pytest
import os.path

# pylint: disable=bare-except
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
# pylint: enable=bare-except


class TestFmfWriterReader(object):
    """Class containing the setup and the tests for FMF
    read and write methods"""
    def setup(self):
        """Populate the whole FMF object"""
        # pylint: disable=attribute-defined-outside-init
        self.fmf_object = FMF()
        # pylint: enable=attribute-defined-outside-init
        misc_params = {'fmf_version': 1.0}
        self.fmf_object.set_header(None, None, None, misc_params)
        self.fmf_object.add_comment("comment after header section")
        self.fmf_object.set_reference(
            'Measurement of Faradays constant',
            'Andreas W. Liehr and Andreas J. Holtmann',
            'Physikalisches Institut, Universitaet Muenster',
            '1995-01-10',
            'andreas@uni-muenster.com')
        meta_section1 = self.fmf_object.add_meta_section('measurement')
        meta_section1.add_entry('room temperature', r'T = (292 \pm 1) K')
        meta_section1.add_entry('barometric pressure',
                                r'p = 1.0144 bar \pm 10 mbar')
        meta_section1.add_entry('current', r'I = (171 \pm 1) mA')
        meta_section_2 = self.fmf_object.add_meta_section('Analysis')
        meta_section_2.add_entry('estimation method', 'line of best fit')
        table1 = self.fmf_object.add_table('analysis', 'A')
        table1.add_column('Gas', 'G', '%s')
        table1.add_column('number of electrons', 'N_e', '%d')
        table1.add_column('volume per time interval', 'V', '%5.3f')
        table1.add_column('uncertainty of ratio', r"\Delta_{V'}", '%.3f')
        table1.add_column('Faraday constant', 'Fa', '%d')
        table1.add_column('error of Faraday constant', r'\Delta_{Fa}', '%d')
        table1.add_comment(r"G\tN_e\tV'\t\Delta_{V'} Fa\t\Delta_{Fa}")
        table1.add_data_row(['H_2', '2', '1.256', '0.065', '91400', '5500'])
        table1.add_data_row(['O_2', '4', '0.562', '0.04', '102200', '7800'])
        table2 = self.fmf_object.add_table('primary', 'P')
        table2.add_column('time', r't [min] \pm 5 [s]', '%.1f')
        table2.add_column('hydrogen volume', r'V_{H_2}(t) \pm 0.2 [cm^3]',
                          '%.1f')
        table2.add_column('oxygen volume', r'V_{O_2}(t) \pm 0.2 [cm^3]',
                          '%.1f')
        table2.add_data_column(['2.5', '4', '6'])
        table2.add_data_column(['2.0', '4.0', '6.6'])
        table2.add_data_column(['2.1', '2.4', '3.7'])

    def test_fmf_writer(self):
        """Test fmf write method"""
        output = StringIO()
        # Write the fmf object to memory
        output.write(self.fmf_object)
        self.fmf_object.write(output)
        # Location of fmf file
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        # Read from file and write to stream
        stream = StringIO()
        stream.write(open(fmf_file).read())
        stream = StringIO()
        stream.write(open(fmf_file).read())
        assert output.getvalue().strip() == stream.getvalue().strip()

    def test_fmf_writer_no_argument(self):
        """Write method without filepointer"""
        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            self.fmf_object.write(None)

    def test_fmf_reader_no_argument(self):
        """Read method without filepointer"""
        # pylint: disable=no-member
        with pytest.raises(MissingSubmission):
            # pylint: enable=no-member
            self.fmf_object.read(None)

    def test_fmf_reader_metasec_entries(self):
        """Test meta section entries (key and values)"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert len(self.fmf_object.meta_sections) == len(
            fmf_object_return.meta_sections)
        if len(self.fmf_object.meta_sections) == len(
                fmf_object_return.meta_sections):
            for key, val in self.fmf_object.meta_sections.entries.items():
                if key not in fmf_object_return.meta_sections.entries.keys():
                    raise Exception("Meta section keys do not match")
                if fmf_object_return.meta_sections.entries.get(key, None) \
                        != val:
                    raise Exception("Meta section values do not match")

    def test_fmf_reader_tablesec_entr(self):
        """Test number of table section entries"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert len(self.fmf_object.table_sections) == len(
            fmf_object_return.table_sections)

    def test_fmf_reader_data_def_entr(self):
        """Test data definition entries (keys and values)"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        for key, val in self.fmf_object.table_sections.data_definitions.\
                items():
            if key not in fmf_object_return.table_sections.data_definitions.\
                    keys():
                raise Exception("Data definition keys do not match")
            if fmf_object_return.table_sections.data_definitions.\
                    get(key, None) != val:
                raise Exception("Data definition values do not match")

    def test_fmf_reader_table_def_entr(self):
        """Test table definition entries (keys and values)"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        for key, val in self.fmf_object.table_sections.table_definitions.\
                items():
            if key not in fmf_object_return.table_sections.table_definitions.\
                    keys():
                raise Exception("Table definition keys do not match")
            if fmf_object_return.table_sections.table_definitions.get(
                    key, None) != val:
                raise Exception("Table definition values do not match")

    def test_fmf_reader_table_data(self):
        """Test content of table data"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert self.fmf_object.table_sections.data == fmf_object_return.\
            table_sections.data

    def test_fmf_reader_global_comments(self):
        """Test content of global comments"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert self.fmf_object.global_comments == fmf_object_return.\
            global_comments

    def test_fmf_reader_table_comments(self):
        """Test content of table comments"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert self.fmf_object.table_sections.comments == fmf_object_return.\
            table_sections.comments

    def test_fmf_read_and_write(self):
        """Compare output of read and write"""
        abs_path = os.path.abspath(os.path.dirname(__file__))
        fmf_file = abs_path + "/files/sample_fmf_file"
        fmf_file_pointer = open(fmf_file, "r")
        fmf_object_return = FMF()
        fmf_object_return = self.fmf_object.read(fmf_file_pointer)
        assert fmf_object_return is not None
        stream = StringIO()
        stream.write(fmf_file_pointer.read())
        output = StringIO()
        output.write(self.fmf_object)
        assert stream.getvalue().strip() == output.getvalue().strip()
