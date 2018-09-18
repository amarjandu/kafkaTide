# class will be derived from Super Exception
# actually there might be away to have this
class bouyError(Exception):
    def __init __(self,ids,boyArray):
        self.ids = ids.strip()


        def __str__(self):
            return(repr(self.ids))