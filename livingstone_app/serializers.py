# serializers.py

from rest_framework import serializers
from .models import Product, ProductVariant, Color, Size

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'hex_code']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']




class ProductVariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer(allow_null=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'color', 'size', 'price', 'quantity']

    def create(self, validated_data):
        color_data = validated_data.pop('color')
        size_data = validated_data.pop('size', None)

        color, _ = Color.objects.get_or_create(**color_data)
        size = None
        if size_data:
            size, _ = Size.objects.get_or_create(**size_data)

        return ProductVariant.objects.create(color=color, size=size, **validated_data)

    def update(self, instance, validated_data):
        color_data = validated_data.pop('color', None)
        size_data = validated_data.pop('size', None)

        if color_data:
            color, _ = Color.objects.get_or_create(**color_data)
            instance.color = color

        if size_data:
            size, _ = Size.objects.get_or_create(**size_data)
            instance.size = size

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance







class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'price', 'category', 'subcategory',
            'description', 'delivery_info', 'payment_info',
            'image1', 'image2', 'image3', 'image4',
            'is_new', 'length', 'width', 'height', 'weight',
            'variants',
        ]

    def create(self, validated_data):
        variants_data = validated_data.pop('variants', [])
        product = Product.objects.create(**validated_data)

        for variant_data in variants_data:
            self.fields['variants'].create(validated_data={**variant_data, 'product': product})
        return product

    def update(self, instance, validated_data):
        variants_data = validated_data.pop('variants', [])

        # Update product fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Optionally: replace all variants
        instance.variants.all().delete()
        for variant_data in variants_data:
            self.fields['variants'].create(validated_data={**variant_data, 'product': instance})

        return instance
