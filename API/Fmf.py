from API.Meta_section import Meta_section
from API.Reference_section import Reference_section
from API.Table import Table

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

        if name.find("*") != -1:
            raise Exception(" '*' is not allowed as first character")

        meta_section = Meta_section(name)

        return self.meta_sections.append(meta_section)