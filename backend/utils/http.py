from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

class APIException400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


def gen_success_response(msg="Success", data=None, status=status.HTTP_200_OK, headers=None):
    res = {
        "detail": msg
    }
    if data:
        res["data"] = data
    return Response(data=res, status=status, headers=headers)

def gen_error_response(msg="Error", status=status.HTTP_400_BAD_REQUEST, headers=None):
    return Response(data={
        "detail": msg
    }, status=status, headers=headers)