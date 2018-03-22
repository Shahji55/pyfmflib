# -*- coding: utf-8 -*-
"""This is the class for all FMF methods"""
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


from pyfmflib.meta_section import FMFMetaSection
from pyfmflib.reference_section import ReferenceSection


class MissingSubmission(Exception):
    """At least one mandatory keyword or parameter not submitted"""
    pass


class ForbiddenSubmission(Exception):
    """Submitted keyword or parameter contains forbidden character(s)"""
    pass


class MultipleKey(Exception):
    """Submitted key does already exists"""
    pass


class UndefinedObject(Exception):
    """Object could not be retrieved"""
    pass


class AmbiguousObject(Exception):
    """Object not properly specified"""
    pass


class SpecificationViolation(Exception):
    """Object doesn't comply with compliance level or version specifications"""
    pass


class FMF(object):
    """Class containing the FMF methods"""
    def __init__(self):
        """Specify the FMF attributes"""
        self.header = None
        self.reference_section = None
        self.meta_sections = []
        self.table_sections = []
        self.global_comments = []
        self.compliance_level = None

    def initialize(*args):
        """Initialize the FMF object"""
        fmf = FMF()

        if len(args) == 1:
            return fmf

        # Order of arguments in API: title, creator, place,
        # created and contact
        title = args[1]
        creator = args[2]
        place = args[3]
        created = args[4]

        if len(args) == 5:
            contact = None
            ref_section = fmf.set_reference(title, creator, place,
                                            created, contact)
            fmf.meta_sections.append(ref_section)
            return fmf

        contact = args[5]
        ref_section = fmf.set_reference(title, creator, place,
                                        created, contact)
        fmf.meta_sections.append(ref_section)
        return fmf

    # pylint: disable=too-many-arguments
    def set_reference(self, title, creator, place, created, contact):
        """Create/update reference section with given params"""
        if self.reference_section is None:
            self.reference_section = ReferenceSection(title, creator, place,
                                                      created, contact)
            self.meta_sections.append(self.reference_section)

        else:
            self.reference_section.title = title
            self.reference_section.creator = creator
            self.reference_section.place = place
            self.reference_section.created = created
            self.reference_section.contact = contact

        return self.reference_section
    # pylint: enable=too-many-arguments

    def add_meta_section(self, name):
        """Add meta section object to the FMF"""
        if name is not None:
            if name.find("*") != -1:
                raise ForbiddenSubmission(" '*' is not allowed as"
                                          " first character")

            for item in self.meta_sections:
                if item.name == name:
                    raise Exception('Meta section with this name '
                                    'already exists')

            meta_section = FMFMetaSection(name)
            self.meta_sections.append(meta_section)
            return meta_section
        raise Exception('Meta section name is mandatory')

    def get_meta_section(self, name):
        """Get the meta section object with given name"""
        if self.meta_sections is not None:
            for item in self.meta_sections:
                if item.name == name:
                    return item

                else:
                    raise Exception('Meta section with specified name'
                                    ' does not exist')

        raise Exception('No meta section exists')

    def set_header(self, encoding, comment_char, separator, misc_params):
        """Set the parameters of FMF header object"""
        pass

    def get_header(self):
        """Get the FMF header object"""
        pass

    def get_table(self, symbol):
        """Get table which matches symbol"""
        pass

    def add_table(self, name, symbol):
        """Add table with given params to FMF"""
        pass

    def add_comment(self, comment_string):
        """Add comment with text in comment_string to FMF"""
        pass

    def read(self, filepointer):
        """Read FMF from filepointer into FMF object"""
        pass

    def write(self, filepointer):
        """Write to filepointer"""
        pass

    def verify(self):
        """Verify if the FMF object is valid"""
        # Code commented out due to table functionality not implemented
        # Pylint will show... Method could be a function (no-self-use)
        '''
        for table in self.table_sections:
            result = table.verify()

            if not result:
                break

        for meta_section in self.meta_sections:
            result = meta_section.verify()

            if not result:
                break
        '''


'''
# Count calls method is used to detect the mixing of iterative and
# symbol calls for the get_meta_section method. It can also be used
# for the same purpose for the get_table method

def __count_calls(function):
    """Count the number of times function is called"""
    def func_wrapper(*args, **kwargs):
        """Function wrapper for the count decorator"""
        if args[1] is None:
            if func_wrapper.called is None:
                func_wrapper.called = 0
                func_wrapper.called += 1

        else:
            func_wrapper.called = None

        return function(*args, **kwargs)
    func_wrapper.called = 0
    func_wrapper.__name__ = function.__name__
    return func_wrapper


def count_decorator(name_flag):
    def count_calls(function):
        def func_wrapper(*args, **kwargs):
            if name_flag is True and len(args) > 1:
                func_wrapper.called = None

            elif name_flag is False and len(args) == 1:
                func_wrapper.called += 1

            return function(*args, **kwargs)
        func_wrapper.called = 0
        func_wrapper.__name__ = function.__name__
        return func_wrapper
    return count_calls
'''
