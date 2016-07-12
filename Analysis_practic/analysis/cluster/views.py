from django.shortcuts import render
from django.http import HttpResponse
from cluster.models import Student, Discipline, Scores
from cluster.tools import new_centroid

def index(request):

    data = {int(str(id)): [int(str(s)) for s in Scores.objects.filter(student_id=id)] for id in Student.objects.all()}
    data_key = data.keys()
    data_values = data.values()
    centroids = [data_values[0], data_values[1], data_values[2]]
    new_centroids = []
    clusters = []
    for i in clusters:
        new_centroids.append = new_centroid(clusters[i])
    centroids = new_centroids
    new_centroids = []


    return HttpResponse(data)
# Create your views here.
