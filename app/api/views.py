from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ChildSerializer, ParentSerializer
from .models import Child, Parent
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome !"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_child(request, child_id):
    child = Child.objects.filter(id=child_id)
    serializer = ChildSerializer(child, many=True)
    return JsonResponse({'child': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_child(request):
    payload = json.loads(request.body)
    try:
        parent_id = Parent.objects.get(id=payload["parent"])
        child = Child.objects.create(
            name=payload["name"],
            lastname=payload["lastname"],
            parent=parent_id,
        )
        serializer = ChildSerializer(child)
        return JsonResponse({'child': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_child(request, child_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        child_item = Child.objects.filter(id=child_id)
        # returns 1 or 0
        child_item.update(**payload)
        child = Child.objects.get(id=child_id)
        serializer = ChildSerializer(child)
        return JsonResponse({'child': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_child(request, child_id):
    user = request.user.id
    try:
        child = Child.objects.get(id=child_id)
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_parent(request, parent_id):
    parent = Parent.objects.filter(id=parent_id)
    serializer = ParentSerializer(parent, many=True)
    return JsonResponse({'parent': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_parent(request):
    payload = json.loads(request.body)
    try:
        parent = Parent.objects.create(
            name=payload["name"],
            lastname=payload["lastname"],
            street=payload["street"],
            city=payload["city"],
            zipcode=payload["zipcode"],
            state=payload["state"],
        )
        serializer = ParentSerializer(parent)
        return JsonResponse({'parent': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_parent(request, parent_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        parent_item = Parent.objects.filter(id=parent_id)
        # returns 1 or 0
        parent_item.update(**payload)
        parent = Parent.objects.get(id=parent_id)
        serializer = ParentSerializer(parent)
        return JsonResponse({'parent': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_parent(request, parent_id):
    user = request.user.id
    try:
        parent = Parent.objects.get(id=parent_id)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
