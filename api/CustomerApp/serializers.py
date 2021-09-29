from rest_framework import serializers
from CustomerApp.models import StatusCatalogs, Customers, Groups


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('GroupsId',
                  'GroupName')


class StatusCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCatalogs
        fields = ('CatalogId',
                  'DescriptionName')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerId',
                  'CustomerName',
                  'CustomerName2',
                  'CustomerName3',
                  'Surname',
                  'LastName',
                  'DateOfJoining',
                  'Street',
                  'Number',
                  'Suburb',
                  'ZipCode',
                  'PhotoFileName',
                  'Status',
                  'StatusBC',
                  'StatusWL',
                  'StatusPLD',
                  'Group')
