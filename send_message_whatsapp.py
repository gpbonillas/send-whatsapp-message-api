import pywhatkit 
import os
import sys
import traceback
 
# Usamos Un try-except
try: 
  # Enviamos el mensaje. Es importante tener abierta una sesión de whatsapp web en el navegador.
  # El mensaje aparecerá escrito en el cuadro de texto del mensaje, después de 20 segundos se enviará
  
  # Los parámetros son: 
  # String que representa el número de celular al que se enviará el mensaje en formato +<codigo pais><numero>. Ej: +593987654321 (Ecuador)
  # String que contiene el mensaje a enviarse. 
  # Int que representa la hora del día a enviarse. Desde 0 a 23
  # Int que represente el mínuto de la hora a enviarse el mensaje. Desde 0 a 59.
  pywhatkit.sendwhatmsg("+593987654321",  
                        "Mensaje de prueba desde el script, enviado por Patricio Bonilla",
                        18, 15) 
 
  print("Mensaje Enviado") 

except BaseException as e:
  # Get current system exception
  ex_type, ex_value, ex_traceback = sys.exc_info()
  # Extract unformatter stack traces as tuples
  trace_back = traceback.extract_tb(ex_traceback)
  # Format stacktrace
  stack_trace = list()
  # Message
  message_all = "";
  for trace in trace_back:
    message_all = message_all + trace[3]
    stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
  
  if len(str(ex_value)) == 0:
    ex_value = message_all

  print("Exception type : %s " % ex_type.__name__)
  print("Exception message : %s" %ex_value)
  print("Stack trace : %s" %stack_trace)
