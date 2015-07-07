from ambry.bundle.loader import CsvBundle


class Bundle(CsvBundle):

    """"""

    @staticmethod
    def int_na_caster(v):
        try:
            return int(v.strip())
        except ValueError:
            return None
    
    def build_modify_row(self, row_gen, p, source, row):
        """Several of the data elements have trailing spaces, 
        this removes them
        """
        for i in row.keys():
            row[i] = row[i].strip()
