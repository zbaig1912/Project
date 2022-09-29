from rest_framework import viewsets
from app.models import User, Firm, Product, Transaction
from app.serializers import FirmSerializer, UserSerializer, ProductSerializer, TransactionSerializer
class FirmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Firm to be viewed.
    """
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    def get_object(self):
        user = User.objects.get(id=self.kwargs["pk"])
        firm = user.firm
        return firm

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        user = User.objects.get(id=self.kwargs["pk"])
        return user

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_object(self):
        user = Transaction.objects.get(id=self.kwargs["pk"])
        product = user.product
        return product


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def get_object(self):
        tran = Transaction.objects.get(id=self.kwargs["pk"])
        return tran
