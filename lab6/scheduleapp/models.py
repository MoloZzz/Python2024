from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=100)
    credits = models.IntegerField()

    class Meta:
        unique_together = ('name', 'professor')

    def __str__(self):
        return self.name


class DictionaryScheduleDay(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Schedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    day = models.ForeignKey(DictionaryScheduleDay, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)

    class Meta:
        unique_together = ('discipline', 'day', 'time')

    def __str__(self):
        return f"{self.discipline} - {self.day} at {self.time}"
