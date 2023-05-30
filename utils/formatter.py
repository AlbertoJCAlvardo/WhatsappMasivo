import pandas as pd 
class Formatter:
    def format_string(self,text:str,data:pd.Series):

        words, tokens = [],[]
        formatted = ""
        lst = text.split("{")

        for i in lst:  
            if "}" in i:
                key = i.split("}")[0]
                formatted += f" {data[key]}"
                
            else:
                formatted += i

        return formatted


