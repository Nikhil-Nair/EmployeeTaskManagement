from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or created.Login required!
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        """
        This view should return a list of all the tasks
        for the currently authenticated user.
        """
        if self.request.user.is_authenticated:

            current_user = self.request.user
            return Task.objects.filter(user=current_user)
        else:
            return None
