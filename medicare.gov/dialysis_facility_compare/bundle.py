from ambry.bundle.loader import CsvBundle


class Bundle(CsvBundle):

    
    #def line_mangler(self, source, row_gen, l):

    #    return l.replace('N\A', '').replace('\0', '')
      
    
    @staticmethod
    def int_na_caster(v):
        try:
            return int(v)
        except ValueError:
            return None

    def build_modify_row(self, row_gen, p, source, row):
        """Several of the data elements have trailing spaces, 
        this removes them
        """
        for i in row.keys():
            row[i] = row[i].strip()

