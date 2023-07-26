import threading
from .sender import Sender

class SenderThread(threading.Thread):
    
    def __init__(self,sender,formatter):
          self.sender = sender_
          self.formatter = formatter

    def run(progressBar,sender,numbers,filepath,message,auxdata):
        count = 0
        progress = 0

        c_dict = {}
        rechazados = []
        rejected_rows = []
        wrong_numbers = []



        for i in numbers:
            if i not in c_dict.keys():
                 c_dict[i] = 0
                

        for i in range(len(numbers)):
                    
            row  = auxdata[self.controller.data["NUMERO_TELEFONO"] == numbers[i]]
            row = row.iloc[[c_dict[numbers[i]]]] 
                   
            c_dict[numbers[i]]+=1
            progress = (i+1)//len(numbers)*100
                    
            message = self.formatter.format_string(message,row.iloc[0])
                    
            if self.controller.filepath == "":
            
                if self.sender.send_message(message, numbers[i],wrong_numbers):
                            count += 1
                        
                else:
                            
                    if numbers[i] not in wrong_numbers:
                            
                        row["TIPO_ERROR"] = "Error del navegador"
                            
                    else:
                                
                            row["TIPO_ERROR"] = "Num no Existe en Whatsapp"
                            
                    rechazados.append(numbers[i])
                    rejected_rows.append(row)
                            
                            
                    
                    
                    else:
                        print("Sending file...")
                        if self.sender.send_file_message(message, formatted_numbers[i],self.controller.filepath,wrong_numbers):
                            count += 1
                        else:

                            if formatted_numbers[i] not in wrong_numbers:
                                row["TIPO_ERROR"] = "Error del navegador"
                            else:
                                row["TIPO_ERROR"] = "Num no Existe en Whatsapp"
                            
                            rechazados.append(numbers[i])
                            rejected_rows.append(row)
