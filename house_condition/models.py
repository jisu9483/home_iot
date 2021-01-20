from django.db import models

# 판매상품 
class ConditionRecord(models.Model):
    temperature = models.FloatField(default=0, blank=True, verbose_name='온도')
    humidity = models.FloatField(default=0, blank=True, verbose_name='습도')
    on_air_conditioner = models.BooleanField(default=False,  verbose_name='에어컨 켜짐여부')
    record_time = models.DateTimeField(auto_now_add=True, verbose_name='기록시간') 

    class Meta:
        ordering=['id']
        verbose_name = 'conditionrecord'
        verbose_name_plural = 'conditionrecords'

    # 이름으로 표시
    def __str__(self):
        return '시간 : %s - 온도 : %.1f 습도: %.1f' %(self.record_time, self.temperature, self.humidity)  