from rest_framework import serializers
from .models import Mission, Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_complete', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', None)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        instance.save()

        if targets_data:
            for target_data in targets_data:
                target_id = target_data.get('id')
                if target_id:
                    target = Target.objects.get(id=target_id, mission=instance)
                    target.name = target_data.get('name', target.name)
                    target.country = target_data.get('country', target.country)
                    if not target.is_complete:
                        target.notes = target_data.get('notes', target.notes)
                    target.save()
        return instance
