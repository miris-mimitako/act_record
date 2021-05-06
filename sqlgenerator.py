# coding:utf-8

### this file is not completed coding.

class Sql_Generator():
    def sql_search(self, **kwargs):
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
        self.s_from = " FROM " + kwargs["s_from"]
        self.s_column="SELECT "

        #Where keys input
        if kwargs.get("s_where") != None:
            self.s_where=kwargs["s_where"]
        ## end if

        #column keys input
        for i in kwargs["s_column"]:
            if n > 1:
                self.s_column += ", "
            self.s_column = i
            ## end if

            n += 1
        ## end for

        sql = self.s_column + " FROM " + self.s_from + " WHERE " + self.s_where + ";"
        print ("End: sql_search")

    ## end of sql_search
    
## end of class Sql_Generator

if __name__=="__main__":
    pass


