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


from pyfmflib.pyfmflib.meta_section import Meta_section
from pyfmflib.pyfmflib.reference_section import Reference_section
from pyfmflib.pyfmflib.table import FMFTable

def count_calls(function):
    def func_wrapper(*args, **kwargs):

            print("Args are: ", args)
            print("kwargs are: ", kwargs)

            print(args[1])

            print ("Previous value of calls: ", func_wrapper.called)

            if args[1] is None:
                if func_wrapper.called is None:
                    func_wrapper.called = 0
                    func_wrapper.called += 1

                print ("Updated value of calls: ", func_wrapper.called)

            else:
                func_wrapper.called = None

            return function(*args, **kwargs)
    func_wrapper.called = 0
    func_wrapper.__name__= function.__name__
    return func_wrapper

def count_decorator(name_flag):
 def count_calls(function):
    def func_wrapper(*args, **kwargs):
            print "Inside wrapped_f()"
            print "Decorator arguments:", name_flag

#            print("Args are: ", args[1])
            print("Args LENGTH is: ", len(args))

            if name_flag is True and len(args) > 1:
                func_wrapper.called = None

            elif name_flag is False and len(args) == 1:
                func_wrapper.called += 1

            return function(*args, **kwargs)
    func_wrapper.called = 0
    func_wrapper.__name__= function.__name__
    return func_wrapper
 return count_calls

def count_calls1(function):
    def func_wrapper(*args, **kwargs):

        print(args)
        print(kwargs)

        func_wrapper.called += 1

        return function(*args, **kwargs)

    func_wrapper.called = 0
    func_wrapper.__name__ = function.__name__
    return func_wrapper


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
    """Object does not comply with compliance level or version specifications"""
    pass


class FMF:
    def __init__(self):

            self.header = None
            self.reference_section = None
            self.meta_sections = []
            self.table_sections = []
            self.global_comments = []
            self.compliance_level = None


    def initialize(*args):
        # args represents the regular arguments
        print args
        print ("No. of arguments: ", len(args))

        fmf = FMF()
        length = len(fmf.meta_sections)
#        print length

        if length > 0:
            for index, item in enumerate(fmf.meta_sections):
                print index, item

        if len(args) == 1:
            return fmf

        else:
            title = args[1]
            creator = args[2]
            place = args[3]
            created = args[4]

            print title, creator, place, created

            if len(args) == 5:
                print "in if condition args == 5"
                contact = None
                ref_section = fmf.set_reference(title, creator, place, created, contact)
#                fmf.meta_sections.append(ref_section)
                return fmf

            else:
                print "in else condition args == 6"
                contact = args[5]
                ref_section = fmf.set_reference(title, creator, place, created, contact)
#                fmf.meta_sections.append(ref_section)
                return fmf

    def set_reference(self, title, creator, place, created, contact):
        print self.reference_section

        if self.reference_section is None:
            self.reference_section = Reference_section(title, creator, place, created, contact)
            self.meta_sections.append(self.reference_section)

        else:
            self.reference_section.title = title
            self.reference_section.creator = creator
            self.reference_section.place = place
            self.reference_section.created = created
            self.reference_section.contact = contact

        return self.reference_section

#    def add_table(self, name, symbol):
#
#        table = FMFTable(name, symbol)
#
#        return table

    def add_meta_section(self, name):
        if name:

            if name.find("*") != -1:
                raise ForbiddenSubmission(" '*' is not allowed as first character")

            for item in self.meta_sections:
                if item.name == name:
                    raise Exception('Meta section with this name already exists')

            meta_section = Meta_section(name)
            self.meta_sections.append(meta_section)
            return meta_section

    def get_meta_section(self, name):
        if self.meta_sections is not None:
            for item in self.meta_sections:
                if item.name == name:
                    print ('Meta section found')
                    return item

                else:
                    raise Exception('Meta section with specified name does not exist')

    def get_meta_section1(self, name):
        if name is not None:
            print "Name not none... calling by name"
            meta_section_returned = FMF.get_meta_section_by_name(self, name)
            return meta_section_returned

        else:
            print "Name not none... calling by iteration"
            meta_section_returned = FMF.get_meta_section_by_iteration(self)
            return meta_section_returned

            #    @count_calls

    @count_decorator(True)
    def get_meta_section_by_name(self, name):
        if self.meta_sections is not None:
            print ("Size of list is: ", len(self.meta_sections))

            for index, item in enumerate(self.meta_sections):
                print ("Section index is: ", index)
                print ("Section name is: ", item.name)

            if name is not None:
                print "Name is not none"
                #                FMF.get_meta_section_by_name.called == 0
                for index, item in enumerate(self.meta_sections):

                    print "PERFORMING COMPARISON"
                    print ("Name is: ", name)
                    print ("Item name is: ", item.name)

                    if item.name == name:
                        print ('Meta section found')
                        print index
                        print "Method called: ", FMF.get_meta_section_by_name.called
                        return item

                    elif index == (len(self.meta_sections) - 1):
                        print 'Meta section not found'
                        raise Exception('Section Not Found')

            elif name is None:
                print 'name is none'

                function_calls = FMF.get_meta_section_by_name.called

                print "Method called with no name: ", function_calls

                if FMF.get_meta_section_by_name.called is None:
                    raise Exception("Iterative and mixed calls cannot be mixed")

                else:
                    for index, item in enumerate(self.meta_sections):
                        print function_calls
                        updated_index = function_calls - 1
                        print updated_index
                        print self.meta_sections[updated_index].name
                        return self.meta_sections[updated_index]

    @count_decorator(False)
    def get_meta_section_by_iteration(self):
        if self.meta_sections is not None:
            print ("Size of list is: ", len(self.meta_sections))

            print "Name is None"

            function_calls = FMF.get_meta_section_by_iteration.called

            print "Method called iteration: ", function_calls

            print "Method called name: ", FMF.get_meta_section_by_name.called

            #           if function_calls > 1 and FMF.get_meta_section_by_name.called is None:
            #                raise Exception("Iterative and mixed calls cannot be mixed")
            #               pass

            #          else:
            for index, item in enumerate(self.meta_sections):
                print function_calls
                updated_index = function_calls - 1
                print updated_index
                print self.meta_sections[updated_index].name
                return self.meta_sections[updated_index]

    def get_meta_section_2(self, name, i=[0]):

        if self.meta_sections is not None:
            if name is not None:
                print "Name is not none"
                for index, item in enumerate(self.meta_sections):
                    if item.name == name:
                        print ('Meta section found')
                        print index
                        return item, index == None

                    # for item in self.meta_sections:
                    #                if item.name == name:
                    #                    print ('Meta section found')
                    #                    return item



                    else:
                        print 'Meta section not found'
                        #                    raise Exception('Meta section with specified name does not exist')

            elif name is None:
                print 'name is none'

                if i[0] is not None:
                    print "Positon: ", i[0]
                    index = i[0]

                else:
                    index = 0

            print self.meta_sections[index].name

            i[0] += 1
            print i[0]

            return self.meta_sections[index], i[0]

    def __get_list_index(self, item):

        print 'private method'

        if item is not None:
            index = None
            return index

    def set_header(self, encoding, comment_char, separator, misc_params):
        pass

    def verify(self):

        # Code commented out due to table functionality not implemented
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

