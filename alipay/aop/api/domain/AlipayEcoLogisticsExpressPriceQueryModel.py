#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLogisticsExpressPriceQueryModel(object):

    def __init__(self):
        self._area_type = None
        self._from_code = None
        self._logis_merch_code = None
        self._product_type_code = None
        self._to_code = None

    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def from_code(self):
        return self._from_code

    @from_code.setter
    def from_code(self, value):
        self._from_code = value
    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value
    @property
    def product_type_code(self):
        return self._product_type_code

    @product_type_code.setter
    def product_type_code(self, value):
        self._product_type_code = value
    @property
    def to_code(self):
        return self._to_code

    @to_code.setter
    def to_code(self, value):
        self._to_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.from_code:
            if hasattr(self.from_code, 'to_alipay_dict'):
                params['from_code'] = self.from_code.to_alipay_dict()
            else:
                params['from_code'] = self.from_code
        if self.logis_merch_code:
            if hasattr(self.logis_merch_code, 'to_alipay_dict'):
                params['logis_merch_code'] = self.logis_merch_code.to_alipay_dict()
            else:
                params['logis_merch_code'] = self.logis_merch_code
        if self.product_type_code:
            if hasattr(self.product_type_code, 'to_alipay_dict'):
                params['product_type_code'] = self.product_type_code.to_alipay_dict()
            else:
                params['product_type_code'] = self.product_type_code
        if self.to_code:
            if hasattr(self.to_code, 'to_alipay_dict'):
                params['to_code'] = self.to_code.to_alipay_dict()
            else:
                params['to_code'] = self.to_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLogisticsExpressPriceQueryModel()
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'from_code' in d:
            o.from_code = d['from_code']
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        if 'product_type_code' in d:
            o.product_type_code = d['product_type_code']
        if 'to_code' in d:
            o.to_code = d['to_code']
        return o


