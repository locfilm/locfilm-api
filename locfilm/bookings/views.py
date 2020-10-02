
# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# App data
from locfilm.bookings.serializers import BookingSerializer
from locfilm.bookings.models import Booking
from locfilm.locations.models import Location
from locfilm.bookings.permissions import IsOwner, IsAllowed



# create a viewset
class BookingViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Booking.objects.all()
    # specify serializer to be used
    serializer_class = BookingSerializer
    permission_classes = [ IsOwner]

    # def get_object(self, queryset=queryset):
    #     print(self.request.data)
    #     print(self.request.query_params)
    #     print(self.request.query_params)
    #     obj = self.request.user
    #     return obj


    # def get_permissions(self):
    #     permissions= [IsAuthenticated,]
    #     return permissions
    #authentication_classes = [IsOwner]



class BookingLocationsViewSet(viewsets.ViewSet):
    """ViewSet for manage the bookings of locations
    """

    @action(detail=True, methods=['get','post'], )
    def bookings(self, request, pk=None):
        try:
            location = Location.objects.get(pk=pk)
        except:
            return Response( {'error':'Location with ID provided does not exist'} )

        data = request.data
        data['location_id'] = location.pk
        data['user_id'] = request.user.id
        print(data)
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response( serializer.errors )

        if request.method == 'GET':
            print('Hiiiii')
            return Response({"hi":'holaa'})

        if request.method == 'POST':
            print('Hiiiii')

            return Response({"HELP":'holaa'})

        #serializer =
