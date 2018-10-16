# -*- coding:utf-8 -*-
import base64

from oscar.apps.catalogue.models import Product, ProductImage
from oscar.apps.partner.models import StockRecord, Partner
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ProductInfo.models import ProductOwner


class ImageSerializer(ModelSerializer):
    # image_url = serializers.SerializerMethodField(required=False)

    class Meta:
        model = ProductImage
        fields = '__all__'

    # def get_image_url(self, image):
    #     request = self.context.get('request')
    #     #TODO need check
    #     # image = image.original.url
    #     image = image.url
    #     return image

class ProductImageReadSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('original','caption')

class ProductImageCreateSerializer(ModelSerializer):
    display_order =serializers.IntegerField(allow_null=True,required=False)
    product = serializers.StringRelatedField(allow_null=True,required=False)
    class Meta:
        model = ProductImage
        fields = '__all__'

class SubProdcutsSerializer(ModelSerializer):
    fullPrice = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =(
                 'id',
                 'structure',
                 'upc',
                 'title',
                 'slug',
                 'description',
                 'rating',
                 'date_created',
                 'date_updated',
                 'is_discountable',
                 'product_class',
                 'attributes',
                 'fullPrice',
                 'categories',
                 'has_stockrecords',
                 'num_stockrecords',
                 'unit_description'
        )

    def get_fullPrice(self,product):
        Product.objects.get(pk=product.id)
        try:
            fullPrice=StockRecord.objects.get(product_id=product.id).price_excl_tax
            return fullPrice
        except:
            pass


class ProdcutsSerializer(ModelSerializer):
    fullPrice = serializers.SerializerMethodField()
    children = SubProdcutsSerializer(many=True)
    has_stockrecords = serializers.SerializerMethodField()
    num_stockrecords = serializers.SerializerMethodField()
    primary_image = ProductImageReadSerializer()
    class Meta:
        model = Product
        fields =('children',
                 'id',
                 'structure',
                 'upc',
                 'title',
                 'slug',
                 'description',
                 'rating',
                 'date_created',
                 'date_updated',
                 'is_discountable',
                 'product_class',
                 'attributes',
                 'fullPrice',
                 'categories',
                 'has_stockrecords',
                 'num_stockrecords',
                 'primary_image',
                 'unit_description'
                )

    def get_fullPrice(self,product):
        if product.structure == 'child':
            try:
                fullPrice=StockRecord.objects.get(product_id=product.id).price_excl_tax
                return fullPrice
            except:
                pass


    def get_has_stockrecords(self,product):
        if product.structure == 'standalone':
            try:
                return product.has_stockrecords
            except:
                return False

    def get_num_stockrecords(self,product):
        if product.structure == 'standalone':
            try:
                return product.num_stockrecords
            except:
                return 0




class SimpleProductInfoSerializer(ModelSerializer):
    fullPrice = serializers.SerializerMethodField()
    attributes = serializers.StringRelatedField(many=True)
    primary_image = ProductImageReadSerializer()

    class Meta:
        model = Product
        fields = ( 'id',
                  'structure',
                  'upc',
                  'title',
                  'slug',
                  'description',
                  'rating',
                  'date_created',
                  'date_updated',
                  'is_discountable',
                  'attributes',
                  'fullPrice',
                  'has_stockrecords',
                  'num_stockrecords',
                  'primary_image',
                  'unit_description'
                  )

    def get_fullPrice(self, product):
        fullPrice = StockRecord.objects.get(product_id=product.id).price_excl_tax
        return str(fullPrice)

class ProductCreateSerializer(ModelSerializer):
    images = ProductImageCreateSerializer(read_only=True,many=True,required=False)
    children = serializers.StringRelatedField(read_only=True,many=True,required=False)

    # attributes = serializers.ManyRelatedField(required=False)
    class Meta:
        model = Product
        fields = '__all__'



    # def validate(self, attrs):
    #     pass



    def create(self, validated_data):
        images_data = self._kwargs['data'].pop('images')
        subProducts = None
        price = self._kwargs['data'].pop('price')
        stockNumber = self._kwargs['data'].pop('stockNumber')
        productOwner = self._kwargs['data'].pop('productOwner')


        try:
            partner = Partner.objects.get(user=productOwner)

        except:
            provider = self._kwargs['data'].pop('provider')
            providerName = '%s_%s' % (provider, productOwner)
            partner = Partner.objects.create(name=providerName, user=productOwner)

        if validated_data['structure'] == 'parent':
            subProducts =  self._kwargs['data'].pop('children')

        product = Product.objects.create(**validated_data)
        partner_sku = '%s%s%s' % (productOwner, product.title,product.id)
        StockRecord.objects.create(product=product, partner=partner, partner_sku=partner_sku,price_retail=price,
                                   num_in_stock=stockNumber)
        ProductOwner.create(product=product,owner=productOwner)

        for image_data in images_data:
            image_data['product'] = product
            imageUrl = image_data.pop('image_url')
            ProductImage.objects.create(**image_data)
            # ProductImagesUrl.objects.create(image_url=imageUrl)

        if subProducts is not None:
            for child in subProducts:
                stockNumber = child.pop('stocknumber')
                price = child.pop('max_price')
                if stockNumber is not None:
                    subproduct = Product.objects.create(parent=product, **child)
                    partner_sku = '%s%s%s' % (productOwner, product.title,product.id)
                    StockRecord.objects.create(product=subproduct, partner=partner, partner_sku=partner_sku,
                                               price_retail=price,
                                               num_in_stock=stockNumber)
                    ProductOwner.create(product=product, owner=productOwner)

        return product


