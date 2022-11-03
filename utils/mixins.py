class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)

class OverwritePerformCreateUserAnimeMixin:
    def perform_create(self, serializer):
        anime = self.get_object_or_404()
        serializer.save(anime=anime, user=self.request.user)