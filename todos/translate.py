import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def translate(event, context, lang):
    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    
    # https://docs.aws.amazon.com/es_es/translate/latest/dg/translate-dg.pdf
    translate = boto3.client(service_name='translate', region_name='region', use_ssl=True)
 
    # Anadimos nuevo index con el resultado de idioma traducido.
    result[lang] = translate.translate_text(Text=result['Item'], SourceLanguageCode="es", TargetLanguageCode=lang)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result[lang],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
