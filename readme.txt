En su archivo .env debera agregar su id y clave secreta de la API de OPENAI

    PROJECT_ID="tu_id_del_proyecto"
    KEY_API_OPENAI="tu_clave_secreta"

Para usar la api deberá uliizar la siguiente url: 
    "mi-dominio.com/chatbot"

A traves del metodo POST, enviando por el request un campo "message" con la pregunta que le hara a chatgpt. Junto con una
API KEY enviada como "Authorization" con el valor de "Api-Key gJm1SPPZ.0MttQxE3kELqhvVNxRTfQsZl3uzxYMC0"