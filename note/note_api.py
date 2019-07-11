from rest_framework import serializers, viewsets
from .models import Note

# Serializers define the API representation.


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'description', 'create_at',
                  'create_by', 'proiority')

# ViewSets define the view behavior.


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
