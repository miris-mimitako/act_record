# coding:utf-8

### this file is not completed coding.

class Sql_Generator():
    def sql_search(self, table_name, *args):
        #-------------------------------------------
        # This def is simple keyword serach on single table.
        # *args are column key, search key word in WHERE frase
        # Ex. sample_column = "ex_word" then please input 'sample_column = "ex_word"'
        # 
        #-------------------------------------------
        print ("start: sql_search")

        #Variation definition
        _column_key = ""
        sql = ""
        n = 0 
        self.table_name = table_name
        self.search_word = search_word

        # comumn key word input
        for i in args:
            if n > 1:
                _column_key += "AND "
            ## end if

            _column_key += args[n]
            n += 1
        ## end of for

        sql = "SELECT"
        print ("End: sql_search")

    ## end of sql_search

    
## end of class Sql_Generator

if __name__=="__main__":
    pass


