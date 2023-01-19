from rest_framework import pagination

class ProductionLargePagination(pagination.PageNumberPagination):
    page_size = 10