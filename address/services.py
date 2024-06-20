import hashlib
import os

from dadata import Dadata

from django.core.cache import cache
from rest_framework.exceptions import APIException


class AddressesService:
    dadata = Dadata(os.environ.get('DADATA_KEY'), os.environ.get('DADATA_SECRET'))

    def validate_address(self, raw_query):
        try:
            cache_key = hashlib.md5(raw_query.encode('utf-8')).hexdigest()
            request_cache = cache.get(cache_key)
            if request_cache:
                result = request_cache
            else:
                result = self.dadata.clean('address', raw_query)
                qc = result.get('qc')
                if qc == 2:
                    raise APIException('Wrong data')
                elif qc in (1, 3):
                    raise APIException('Address needs verification and clarification')
                cache.set(cache_key, result)
            return result
        except APIException as e:
            raise e
        except Exception:
            raise APIException('Error from external service', 500)
