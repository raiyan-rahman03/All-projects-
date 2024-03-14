from rest_framework import serializers
from django.contrib import admin
from django.contrib.auth.models import Group, User 
from rest_framework.authtoken.models import Token 


from.models import Category ,MenuItem,Order,Card,OrderItem
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='Category', queryset=Category.objects.all())

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category_id']



class UserSerializer(serializers.ModelSerializer):
    a = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "a"]

    def get_a(self, obj):
        # Get the token for the user
        token_obj = Token.objects.get(user=obj)
        
        # Return the token key
        return token_obj.key
    
class cart_get(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
class cart_add(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('quantity','menu_item',)


class orderitem_s(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class Order_post(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ''
class Order_s(serializers.ModelSerializer):
    order_items = orderitem_s(many=True, read_only=True)

    
    class Meta:
        model = Order
        fields = '__all__'
class orderitem_post(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
##
        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
class delivery(serializers.ModelSerializer):
    class  Meta:
        model =Order
        fields=['status']