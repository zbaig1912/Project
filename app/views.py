from rest_framework import viewsets
from app.models import User, Firm, Product, Transaction
from app.serializers import FirmSerializer, UserSerializer, ProductSerializer, TransactionSerializer
class FirmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Firm to be viewed.
    """
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer