
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import *
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action   #detail_route, list_route


class PollViewSet(viewsets.ModelViewSet, viewsets.ViewSetMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods= ["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices  = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)


    @action(detail=True, methods= ["POST"])
    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class PollListView(generics.GenericAPIView, mixins.ListModelMixin,
                   mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    authentication_classes = [ TokenAuthentication,SessionAuthentication, BasicAuthentication,]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)




class PollApiView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PollDetailApiView(APIView):
    def get_object(self, id):
        try:
            instance = Question.objects.get(id=id)
            return instance
        except Question.DoesNotExist as e:
            return JsonResponse( {"error": "Given question object not found."}, status=404)

    def get(self, request, id=None):
        try:
            instance = Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)
        #instance = self.get_object(id)
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):

        #instance = self.get_object(id)
        try:
            instance = Question.objects.get(id=id)
            return instance
        except Question.DoesNotExist as e:
            return JsonResponse( {"error": "Given question object not found."}, status=404)
        data = request.data
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=204)



@csrf_exempt
def poll(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poll_details(request, id):
    try:
        instance = Question.objects.get(id=id)
    except Question.DoesNotExist as e:
        return JsonResponse({"error": "Given question object not found."},status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(instance)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return  JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instance.delete()
        return  HttpResponse(status=204)