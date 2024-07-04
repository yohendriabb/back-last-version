class DateViewSet(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Date.objects.all()
    serializer_class = DateSerializer
