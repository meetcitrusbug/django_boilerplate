from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .language_translate import language_translate
from core.models import Language


msg = 'Please fill missing field(s) or sovle error(s)'


def get_first_msg(data):
    try:
        if data:
            first_key = list(data.keys())[0]
            error = data.get(first_key)
            if error:
                error_msg = str(error[0])
                error_msg = error_msg.replace('This', first_key)
                error_msg = error_msg.replace('"', '')
                return error_msg
        return ''
    except Exception as e:
        print(e)
        return 'Something went wrong'


def ReturnResponse(data={}, code=HTTP_200_OK, message='', status=False, query_params={}):
    language = query_params.get('language', 'english')
    language = Language.objects.filter(title=language).first()
    
    lang_code =  language.code if language != None  else 'en'
    
    if not status and data and not message:
        message = get_first_msg(data)

    message = language_translate(message, code=lang_code)
    return Response({
        "status": status,
        "code": code,
        "message": message,
        "data": data
    }, status=code)
