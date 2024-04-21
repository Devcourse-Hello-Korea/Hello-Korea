from django.db import models

class LanguageInfo(models.Model):
    lang = models.CharField(max_length=10, primary_key=True)
    selected = models.BooleanField(default=False)
    def __str__(self):
        return self.lang
    
    @classmethod
    def GetCurrentLanguage(cls):
        return cls.objects.get(selected=True)

class TypeInfo(models.Model):
    type = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.type
    
class TraditionExperienceInfo(models.Model):
    lang = models.ForeignKey(LanguageInfo, on_delete=models.CASCADE, to_field='lang')
    type = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)
    info = models.CharField(max_length=300, default='')
    call = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    homepage = models.URLField(max_length=100, default='')

    # Lang, Type으로 정보를 얻을 수 있는 함수
    @classmethod
    def GetInfoByLangType(cls, type_name, language):
        try:
            # 해당 타입에 해당하는 TraditionExperienceInfo 객체들 필터링
            experience_info_list = cls.objects.filter(type__type=type_name, lang__lang=language)
            
            # 필터링된 객체들의 정보를 담을 리스트 초기화
            result = []

            # 필터링된 객체들의 정보를 result 리스트에 저장
            for experience_info in experience_info_list:
                result.append({
                    'name': experience_info.name,
                    'info': experience_info.info,
                    'call': experience_info.call,
                    'address': experience_info.address,
                    'homepage': experience_info.homepage,
                })
            
            return result
        except cls.DoesNotExist:
            # 해당 타입에 해당하는 정보가 없을 경우 빈 리스트 반환
            return []
        
    # Type으로 정보를 얻는 함수.
    @classmethod
    def GetInfoByLang(cls, language):
        try:
            # 해당 타입에 해당하는 TraditionExperienceInfo 객체들 필터링
            experience_info_list = cls.objects.filter(lang__lang=language)
            
            # 필터링된 객체들의 정보를 담을 리스트 초기화
            result = []

            # 필터링된 객체들의 정보를 result 리스트에 저장
            for experience_info in experience_info_list:
                result.append({
                    'name': experience_info.name,
                    'info': experience_info.info,
                    'call': experience_info.call,
                    'address': experience_info.address,
                    'homepage': experience_info.homepage,
                })
            
            return result
        except cls.DoesNotExist:
            # 해당 타입에 해당하는 정보가 없을 경우 빈 리스트 반환
            return []
