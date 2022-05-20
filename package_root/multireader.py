import os
from package_root.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class MultiReader():
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension)
        self.filename = filename
        self.f = opener(filename, 'rt') 
    
    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
        