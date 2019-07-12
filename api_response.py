from functools import wraps
import json


def http_response(func):
    '''Return an AWS Lambda API Gateway response'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        return {'headers': headers(),
                'statusCode': 200,
                'body': json.dumps(func(*args, **kwargs))}

    return wrapper


def headers(origin='', cert_valid_for=31536000):
    """
    :param origin: Originating domains that are allowed to display this content
    :param cert_valid_for: Time in seconds the certificate is considered valid
    :return: Sensible header defaults
    """
    return {
        'Access-Control-Allow-Origin': origin,
        'Content-Security-Policy': 'default-src null null',
        'Expect-CT': f'enforce,max-age={cert_valid_for}',
        'Referrer-Policy': 'no-referrer',
        'Strict-Transport-Security': f'max-age={cert_valid_for}',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block'}
