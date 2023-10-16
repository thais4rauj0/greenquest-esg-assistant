import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import warnings
import ssl

apikey='siKfoXWnC5ZftvVUx1McLwkdiMruVglcZIMKZCOJdtQr'
url = 'https://api.au-syd.assistant.watson.cloud.ibm.com'
assistantID = '5483b388-6611-4d73-8aa5-4c521654355a'

warnings.filterwarnings("ignore")

authenticator = IAMAuthenticator(apikey)

# Set the minimum TLS version
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

assistant = AssistantV2(version='2018-09-20', authenticator=authenticator)

assistant.set_service_url(url)

assistant.set_disable_ssl_verification(True)

session = assistant.create_session(assistantID).get_result()
session_json = json.dumps(session, indent=2)
session_dict = json.loads(session_json)
session_id = session_dict['session_id']
print(session_id)

#
# print('******* INICIANDO CONVERSA')
# message = assistant.message(
#     assistantID,
#     session_id,).get_result()
# message_json = json.dumps(message, indent=2)
# message_dict = json.loads(message_json)
# for i in range(len(message_dict['output']['generic'])):
#   print(message_dict['output']['generic'][i]['text'])
#
# # Inicialização da variável texto
# texto = input('Digite uma mensagem para o assistente: ')
#
# while texto:
#     try:
#         message = assistant.message(
#             assistantID,
#             session_id,
#             input={'text': texto}).get_result()
#
#         message_json = json.dumps(message, indent=2)
#         message_dict = json.loads(message_json)
#
#         for i in range(len(message_dict['output']['generic'])):
#             print(message_dict['output']['generic'][i]['text'])
#
#     except Exception as e:
#         print(f"Ocorreu um erro na interação com o assistente: {e}")
#
#     # Aguarda nova entrada do usuário
#     texto = input('Digite outra mensagem para o assistente (ou pressione Enter para sair): ')
#
# print("Encerrando o programa.")

print('*******Encerrando a sessão')
assistant.delete_session(assistantID,session_id)
print('Sessão encerrada')

