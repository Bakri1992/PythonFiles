# When to use class methods and to use static method ?

class Item:
    
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class, but
        not sth that must be unique per instance!
        '''

    @classmethod
    def instantiate_from_sth(cls):
        '''
        This should also do sth thath has a relationship with the class, but 
        usually, those are used to manipulate different structures of data to 
        instantiate objects, like we have done with csv.
        '''

    # However, those could be also called from instances.
item=Item()
item.is_integer()
item.instantiate_from_sth()