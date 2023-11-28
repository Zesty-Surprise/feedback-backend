import os
from dotenv import load_dotenv
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType, MultipartSubtypeEnum
from fastapi import BackgroundTasks
from ....fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType, MultipartSubtypeEnum

from ....core.amp import (
            head,
            footer,
            enps,
            department,
            question,
        )

load_dotenv()

class Envs:
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') 
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') 
    MAIL_FROM = os.getenv('MAIL_FROM')
    MAIL_PORT = int(os.getenv('MAIL_PORT') or "587")
    MAIL_SERVER = os.getenv('MAIL_SERVER') 
    BACKEND_HOST = os.getenv('BACKEND_HOST') 

conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS=True,
)

def cont_get_html(template, session_id, form_id):
    # TODO: handle AMP fallback. Tell user to go on our webpage.
    host = Envs.BACKEND_HOST
    if (host == "localhost" or host == "127.0.0.1"):
        form_url = '<form action-xhr="http://{}/api/file/{}/{}" method="get" id="ic-form">'.format(host, session_id, form_id)
    else:
        form_url = '<form action-xhr="https://{}/api/file/{}/{}" method="get" id="ic-form">'.format(host, session_id, form_id)

    build = []
    
    for comp in template["components"]:
        if comp['type'] == "enps-component":
            build.append(set_text_for_component(comp, enps))
        elif comp['type'] == "department-component":
            build.append(set_text_for_component(comp, department))
        elif comp['type'] == "custom-component":
            build.append(question.format(comp['custom_text'], comp['id']))

    main = "".join(build)

    html = head + form_url + main + footer
    print(html)

    return html


def cont_send_email(background_tasks: BackgroundTasks, subject: str, email_to: list[str], body: str):
    # https://www.appsloveworld.com/python/661/how-to-send-amp-email-from-python-how-is-it-technically-different-from-normal-em
    test ="""
    <html>
  <head>
  <meta charset="utf-8">    
</head>
  <body>
    <p>Hi!<br>
    </p>
    <h1>Hello, I am an HTML MAIL!</h1>
  </body>
</html>
    """

    try:
        #Important: Some email clients only render the last MIME part, so it is
        #recommended to place the text/x-amp-html MIME part before the text/html.
        message = MessageSchema(
            subject=subject,
            recipients=email_to,
            body=body,
            subtype=MessageType.amp,
            alternative_body=test,
            multipart_subtype = MultipartSubtypeEnum.alternative
        )    
        fm = FastMail(conf)
        background_tasks.add_task(fm.send_message, message)
        return True
    except:
        return False


def set_text_for_component(comp, text):
    res = text.format(comp['custom_text'])
    return res
