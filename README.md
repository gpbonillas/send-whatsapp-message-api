# send-whatsapp-message-api

Este script permite enviar mensaje de texto a cualquier número consumiendo el API de WhatsApp.

## Uso y ejecución

Los parámetros a configurarse son: 

1. Un string que representa el número de celular al que se enviará el mensaje en formato +[codigo pais][numero]. 

> Ej: +593987654321 (Para Ecuador con código +593)

2. Un string que contiene el mensaje a enviarse. 
3. Un entero que representa la hora del día a enviarse el mensaje. Desde 0 a 23
4. Un entero que represente el mínuto de la hora a enviarse el mensaje. Desde 0 a 59.

Ejemplo: 

```python
pywhatkit.sendwhatmsg("+593987654321",  
                        "Mensaje de prueba desde el script, enviado por Patricio Bonilla",
                        18, 15) 
```

## NOTA: 
> Es importante tener abierta una sesión de whatsapp web en el navegador. Cuando se cumpla la hora y minutos configuradas el mensaje aparecerá escrito en el cuadro de texto del mensaje en el chat y después de 20 segundos se enviará.