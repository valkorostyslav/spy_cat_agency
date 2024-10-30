from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Mission, Target
from .serializers import MissionSerializer
from cats.models import Cat

class MissionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            if Mission.objects.filter(cat=serializer.validated_data['cat']).exists():
                return Response({"error": "Cat already has a mission."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        missions = Mission.objects.all()
        serializer = MissionSerializer(missions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            mission = Mission.objects.get(pk=pk)
            serializer = MissionSerializer(mission)
            return Response(serializer.data)
        except Mission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            mission = Mission.objects.get(pk=pk)
            serializer = MissionSerializer(mission, data=request.data)
            if serializer.is_valid():
                if serializer.validated_data.get('is_complete', mission.is_complete):
                    return Response({"error": "Cannot update notes because the mission is completed."}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                targets_data = serializer.validated_data.get('targets', [])
                for target_data in targets_data:
                    target_id = target_data.get('id')
                    if target_id:
                        target = Target.objects.get(id=target_id, mission=mission)
                        if target.is_complete:
                            return Response({"error": "Cannot update notes for completed targets."}, 
                                            status=status.HTTP_400_BAD_REQUEST)
                        target.notes = target_data.get('notes', target.notes)
                        target.save()
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            mission = Mission.objects.get(pk=pk)
            if mission.cat is not None:
                return Response({"error": "Mission cannot be deleted because it is assigned to a cat."}, 
                                status=status.HTTP_400_BAD_REQUEST)
            mission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Mission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
