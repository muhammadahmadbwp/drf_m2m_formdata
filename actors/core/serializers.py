from rest_framework import serializers
from core.models import ActorsDetail, Children, Pictures, Movies


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = "__all__"


class PicturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pictures
        fields = "__all__"


class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Children
        fields = "__all__"


class ActorsSerializer(serializers.ModelSerializer):
    children = ChildrenSerializer(write_only=True, many=True)
    pictures = PicturesSerializer(write_only=True, many=True)
    movies = MoviesSerializer(write_only=True, many=True)
    
    class Meta:
        model = ActorsDetail
        fields = ["name", "dob", "spouse", "children", "pictures", "movies"]

    def create(self, validated_data):
        # print(validated_data)
        children_data = validated_data.pop('children', None)
        pictures_data = validated_data.pop('pictures', None)
        movies_data = validated_data.pop('movies', None)
        item = ActorsDetail.objects.create(**validated_data)
        children = []
        if children_data is not None:
            for child in children_data:
                child_id = child.pop('id', None)
                child_data, _ = Children.objects.get_or_create(id=child_id, defaults=child)
                children.append(child_data)
                item.children.add(*children)
        pictures = []
        if pictures_data is not None:
            for pic in pictures_data:
                pic_id = pic.pop('id', None)
                pic_data, _ = Pictures.objects.get_or_create(id=pic_id, defaults=pic)
                pictures.append(pic_data)
                item.pictures.add(*pictures)
        movies = []
        if movies_data is not None:
            for movie in movies_data:
                movie_id = movie.pop('id', None)
                movie_data, _ = Movies.objects.get_or_create(id=movie_id, defaults=movie)
                movies.append(movie_data)
                item.movies.add(*movies)
        item.save()
        return item


class GetActorsSerializer(serializers.ModelSerializer):
    # children = ChildrenSerializer(many=True)
    # pictures = PicturesSerializer(many=True)
    # movies = MoviesSerializer(many=True)


    class Meta:
        model = ActorsDetail
        fields = ["name", "dob", "spouse", "children", "pictures", "movies"]
        depth = 1