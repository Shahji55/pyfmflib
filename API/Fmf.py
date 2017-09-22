from API.Meta_section import Meta_section
from API.Reference_section import Reference_section
from API.Table import Table


def count_calls(function):
    def func_wrapper(*args, **kwargs):

            print("Args are: " , args)
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

class FMF:
    def __init__(self):

            self.header = None
            self.reference_section = None
            self.meta_sections = []
            self.table_sections = []
            self.global_comments = []
            self.compliance_level = None

    def initialize(*args, **kwargs):

        # args represents the regular arguments
        # kwargs represents the keyword arguments
        print args, kwargs
        print (len(args))
        print (len(kwargs))

        return FMF(header=None, meta_sections=[], tables=[], global_comments=[], compliance_level=None)


    def set_reference(self, title, creator, place, created, contact):
        self.reference_section = Reference_section(title, creator, created, place, contact)

        return self.reference_section


    def add_table(self, name, symbol):

        table = Table(name, symbol)

        return table

    def add_meta_section(self,name):

        if self.meta_sections is not None:
            for item in self.meta_sections:
                if item.name == name:
                    raise Exception('Meta section with this name already exists')

        if name.find("*") != -1:
            raise Exception(" '*' is not allowed as first character")

        meta_section = Meta_section(name)

#        self.meta_sections.append(meta_section)

        return meta_section

    def get_meta_section(self, name):
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
                        updated_index = function_calls -1
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

#            for item in self.meta_sections:
#                if item.name == name:
#                    print ('Meta section found')
#                    return item



                else:
                    print 'Meta section not found'
#                    raise Exception('Meta section with specified name does not exist')

            elif name is None:
                print 'name is none'

                if i[0] is not None:
                    print "Positon: " , i[0]
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






