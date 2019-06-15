from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

class APIException400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


def gen_success_response(msg="Success", data=None, status=status.HTTP_200_OK):
    res = {
        "detail": msg
    }
    if data:
        res["data"] = data
    return Response(res, status)

def gen_error_response(msg="Error", status=status.HTTP_400_BAD_REQUEST):
    return Response({
        "detail": msg
    }, status)