from rest_framework.serializers import ModelSerializer

from rating.models import Rating


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'score', 'created_at']
