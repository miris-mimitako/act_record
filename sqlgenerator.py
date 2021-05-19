# coding:utf-8

### this file is not completed coding.

'''
This program must use type of dictionary
key: s_column---Table / query column name(s) (multiple method you must use list in dictionary)
key: s_table---Table name 
key: s_where---search items
key: s_value---column and value (You must use dictionary method. Multiple lines shall use values in list)
Use following dictionary
dic_sql_generator={
    #--- select method ---*
    "s_column": xxx,
    "s_table": xxx,
    "s_where": xxx
    #--- insert method ---*
    "s_table": xxx,
    "s_column_value": {column1: value1, column2: value2, ...} or {column1: [value1, value2,...], ...}
}
'''


class Sql_Generator:

    def __init__(self,sql_keys):
        print ("Start: Sql_Generator / __init")

        self.sql_keys = sql_keys #recieving dictionary
        self.s_column_value= [] #list define
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
        if self.sql_keys.get("s_table") != None:
            self.s_table=self.sql_keys["s_table"]
        ## end if

        #column and value input
        if self.sql_keys.get("s_column_value") != None:
            if isinstance(self.s_column, list):
                self.s_column_value.extend(self.sql_keys["s_column_value"]) #add list
            
            else:
                self.s_column_value.append(self.sql_keys["s_column_value"]) #add a value
            ## end if
        ## end if

        print ("End: Sql_Generator / __init")

    def sql_search(self):
        #-------------------------------------------
        # This def is simple keyword serach
        # Must use dictionary method:
        #   key: s_column -- when no define, this def can automaticaly choose "*"
        #       You can input one column or multi comlumns.
        #       Multi comlumns use list in dictionary.
        #   key: s_table -- must input your table name or query
        #   key: s_where -- search keyword(s) in column(s)
        #       You must use SQL frase
        # Example:
        #   s=sql_search({s_column: [username, address], s_table: table_name, s_where: "country='Mexico' and sex = 'female'"})
        # 
        #-------------------------------------------
        print ("start: sql_search")
        #Variation definition
        _column_key = ""
        sql = ""
        n = 0 
        self.s_table = " FROM " + self.s_table
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


        sql = _column_key + self.s_table +  self.s_where + ";"
        
        return sql
        
        print ("End: sql_search")
    ## end of sql_search
    
    def sql_insert(self):
        # Initialize valiation
        _columns =" ("
        _values ="VALUES ("
        sql = ""
        n = 0 
        flag_value = 0 # 1 = value has list type

        # Input data
        self.s_table = "INSERT INTO " + self.s_table

        for index, item in enumerate(self.s_column_value.values()):
            if isinstance(item, list):
                #s_column_value has list then flag 
                flag_value = 1
                break
            ## end if
        ## end for

        if flag_value == 0:
            for index, item_colums_key in enumerate(self.s_column_value.keys()):
                if index > 0:
                    _columns += ", " + item_colums_key
                    _values += ", " + self.s_column_value[item_colums_key]
                else:
                    _columns += item_colums_key
                    _values += self.s_column_value[item_colums_key]
                ## end if
            ## end for
        else:
            
            """
            s_columun_lenの値は複数のリストが利用されるケースが想定される。
            Lenでリストの最大数を把握しながら、もし足りない要素が出てきた場合に最後の値で埋めるようにしなければならない
            x=2,y=3,z=4のリストを持っている場合は、3週目以降xはその最大値を利用する。
            yは4週目からyの最大値を利用することになる。

            for文で回しながら次の処理を実行する
            indexで何回目の処理かを確認
            読み込む対象リストの読み込み位置　x
            x＜Indexならxの最大位置を読み込み
            x＞≡IndexならIndex位置を読み込み
            

            """

            ## below code shall not use -- not work
            for index, item_colums_key in enumerate(self.s_column_value.keys()):
                if index > 0:
                    _columns += ", " + item_colums_key
                    _values += ", "

                    if isinstance(self.s_column_value[item_colums_key], list):
                        for index_inner, item_value in enumerate(self.s_column_value[item_colums_key]):
                            if index_inner > 0:
                                _values += ", "
                            ## end if
                            _values += item_value
                        ## end for
                    else:
                        _values += self.s_column_value[item_colums_key]
                    ## end if
                else:
                    _columns += item_colums_key
                    if isinstance(self.s_column_value[item_colums_key], list):
                        for index_inner, item_value in enumerate(self.s_column_value[item_colums_key]):
                            if index_inner > 0:
                                _values += ", "
                            ## end if
                            _values += item_value
                        ## end for
                    else:
                        _values += self.s_column_value[item_colums_key]
                    ## end if
                ## end if
            ## end for
        ## end if

        _columns += ")"
        _values += ")"
        sql = self.s_table + _columns + _values + ";"

        return sql

    ## end of sql_insert

    def __del__(self):
        print ("call deconstructor")
    ## end of del

## end of class Sql_Generator

if __name__=="__main__":
    pass


