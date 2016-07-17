from django.shortcuts import render
from django.http import HttpResponse
from cluster.models import Student, Discipline, Scores
from cluster.tools import Cluster, k_means
#from cluster.tools import cluster1, cluster2, cluster3


def index(request):
    data = {int(str(id)): [int(str(s)) for s in Scores.objects.filter(student_id=id)] for id in Student.objects.all()}
    cluster1 = Cluster()
    cluster2 = Cluster()
    cluster3 = Cluster()
    clusters = [cluster1, cluster2, cluster3]
    k_means(data, clusters)

    return HttpResponse(cluster2.objects.values())
# Create your views here.
