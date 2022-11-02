from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# 1 Businessschedule 목록을 보여주는 역할
class BusinessscheduleList(APIView):
    # list를 보여줄 때
    def get(self, request):
        bss = Businessschedule.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = BusinessscheduleSerializer(bss, many=True)
        return Response(serializer.data)

    # 새로운 Businessschedule 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = BusinessscheduleSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Businessschedule detail을 보여주는 역할
class BusinessscheduleDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return Businessschedule.objects.get(pk=pk)
        except Businessschedule.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        bs1 = self.get_object(pk)
        serializer = BusinessscheduleSerializer(bs1)
        return Response(serializer.data)

    #  수정하기
    def put(self, request, pk, format=None):
        bs1 = self.get_object(pk)
        serializer = BusinessscheduleSerializer(bs1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  삭제하기
    def delete(self, request, pk, format=None):
        bs1 = self.get_object(pk)
        bs1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# 2 Counselingmanual 목록을 보여주는 역할
class CounselingmanualList(APIView):
    # list를 보여줄 때
    def get(self, request):
        cm = CounselingManual.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = CounselingmanualSerializer(cm, many=True)
        return Response(serializer.data)

    # 새로운 Counselingmanual 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = CounselingmanualSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Counselingmanual detail을 보여주는 역할
class CounselingManualDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return CounselingManual.objects.get(pk=pk)
        except CounselingManual.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        cm = self.get_object(pk)
        serializer = CounselingmanualSerializer(cm)
        return Response(serializer.data)

    #  수정하기
    def put(self, request, pk, format=None):
        cm = self.get_object(pk)
        serializer = CounselingmanualSerializer(cm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  삭제하기
    def delete(self, request, pk, format=None):
        cm = self.get_object(pk)
        cm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3 Counselingmanual 목록을 보여주는 역할
class CounselingManualCommentList(APIView):
    # list를 보여줄 때
    def get(self, request):
        cmc = CounselingManualComment.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = CounselingmanualcommentSerializer(cmc, many=True)
        return Response(serializer.data)

    # 새로운 CounselingManualComment 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = CounselingmanualcommentSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CounselingManualComment detail을 보여주는 역할
class CounselingManualCommentDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return CounselingManualComment.objects.get(pk=pk)
        except CounselingManualComment.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        cmc = self.get_object(pk)
        serializer = CounselingmanualSerializer(cmc)
        return Response(serializer.data)

    #  수정하기
    def put(self, request, pk, format=None):
        cmc = self.get_object(pk)
        serializer = CounselingmanualcommentSerializer(cmc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  삭제하기
    def delete(self, request, pk, format=None):
        cmc = self.get_object(pk)
        cmc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 4 Counselingtype 목록을 보여주는 역할
class CounselingtypeList(APIView):
    # list를 보여줄 때
    def get(self, request):
        ct = Counselingtype.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = CounselingtypeSerializer(ct, many=True)
        return Response(serializer.data)

    # 새로운 Counselingtype 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = CounselingtypeSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Counselingtype detail을 보여주는 역할
class CounselingtypeDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return CounselingManualComment.objects.get(pk=pk)
        except CounselingManualComment.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        ct = self.get_object(pk)
        serializer = CounselingmanualSerializer(ct)
        return Response(serializer.data)

    #  수정하기
    def put(self, request, pk, format=None):
        ct = self.get_object(pk)
        serializer = CounselingmanualcommentSerializer(ct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  삭제하기
    def delete(self, request, pk, format=None):
        ct = self.get_object(pk)
        ct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 5 SoftwareProductFamily 목록을 보여주는 역할
class SoftwareProductFamilyList(APIView):
    # list를 보여줄 때
    def get(self, request):
        spf = SoftwareProductFamily.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = SoftwareproductfamilySerializer(spf, many=True)
        return Response(serializer.data)

    # 새로운 Counselingtype 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = SoftwareproductfamilySerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# SoftwareProductFamily detail을 보여주는 역할
class SoftwareProductFamilyDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return SoftwareProductFamily.objects.get(pk=pk)
        except SoftwareProductFamily.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        spf = self.get_object(pk)
        serializer = SoftwareproductfamilySerializer(spf)
        return SoftwareproductfamilySerializer(serializer.data)

    #  수정하기
    def put(self, request, pk, format=None):
        spf = self.get_object(pk)
        serializer = CounselingmanualcommentSerializer(spf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  삭제하기
    def delete(self, request, pk, format=None):
        spf = self.get_object(pk)
        spf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



