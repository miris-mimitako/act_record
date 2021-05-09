# coding:utf-8

### this file is not completed coding.

class Sql_Generator:

    def __init__(self,sql_keys):
        print ("Start: Sql_Generator / __init")

        self.sql_keys = sql_keys #recieving dictionary

        ## Open dictionary

        #Where keys input
        if self.sql_keys.get("s_where") != None:
            self.s_where=self.sql_keys["s_where"]
        ## end if

        #column keys input
        if self.sql_keys.get("s_column") != None:
            self.s_column=self.sql_keys["s_column"]
        ## end if

        #from keys input
        if self.sql_keys.get("s_from") != None:
            self.s_from=self.sql_keys["s_from"]
        ## end if

        print ("End: Sql_Generator / __init")

    def sql_search(self):
        #-------------------------------------------
        # This def is simple keyword serach
        # Must use dictionary method:
        #   key: s_column -- when no define, this def can automaticaly choose "*"
        #       You can input one column or multi comlumns.
        #       Multi comlumns use list in dictionary.
        #   key: s_from -- must input your table name or query
        #   key: s_where -- search keyword(s) in column(s)
        #       You must use SQL frase
        # Example:
        #   s=sql_search({s_column: [username, address], s_from: table_name, s_where: "country='Mexico' and sex = 'female'"})
        # 
        #-------------------------------------------
        print ("start: sql_search")
        #Variation definition
        _column_key = ""
        sql = ""
        n = 0 

        self.s_from = " FROM " + self.s_from

        # Colum may have list argument

        if isinstance(self.s_column, list):
            # s_column type is list
            for index, item in enumerate(self.s_column):
                if index > 0:
                    _column_key += ", "
                ## end if
                _column_key += item
            ## end for
        else:
            _column_key=self.s_column
        ## end if

        _column_key="SELECT " + _column_key
        if self.s_where != None:
            self.s_where = " WHERE " + self.s_where
        ## end if 


        sql = _column_key + self.s_from +  self.s_where + ";"
        
        return sql
        
        print ("End: sql_search")
    ## end of sql_search
    
## end of class Sql_Generator

if __name__=="__main__":
    pass


