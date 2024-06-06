from django.db import models

class Archive(models.Model):
    shelf = models.IntegerField()
    rack = models.IntegerField()
    cell = models.IntegerField()
    cell_code = models.CharField(max_length=100)
    fill_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Shelf: {self.shelf}, Rack: {self.rack}, Cell: {self.cell}"

class Subscriber(models.Model):
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Document(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=50)
    cell_code = models.ForeignKey(Archive, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    arrival_date = models.DateField()
    issue_dates = models.JSONField(default=list)

    def __str__(self):
        return self.title
