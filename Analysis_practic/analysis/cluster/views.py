# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template, Context
from cluster.models import Student, Discipline, Scores
from django.http import Http404
from cluster.tools import Cluster_graphic
#from cluster.tools import new_centroid

def index(request):
    template = loader.get_template('index2.html')
    data1 = [Student.objects.get(pk=1002), Student.objects.get(pk=1003)]
    data2 = list(Student.objects.filter(pk=1003))
    data3 = list(Student.objects.filter(pk=1004))
    clusters = [data1, data2, data3]
    verticals = [s * 100 for s in range(7)]
    horizontals = [s * 100 for s in range(5)]
    cluster1_centroid = [500, 400, 300, 200, 300, 400]
    i = 100
    cluster1_graphic = []

    for score in cluster1_centroid:
        cluster1_graphic.append(Cluster_graphic(abs(600 - score), i))
        i = i + 100

    cluster2_centroid = [300, 400, 500, 400, 200, 300]
    i = 100
    cluster2_graphic = []

    for score in cluster2_centroid:
        cluster2_graphic.append(Cluster_graphic(abs(600 - score), i))
        i = i + 100

    cluster3_centroid = [200, 400, 400, 500, 400, 300]
    i = 100
    cluster3_graphic = []

    for score in cluster3_centroid:
        cluster3_graphic.append(Cluster_graphic(abs(600 - score), i))
        i = i + 100

    context = RequestContext(request, {
        'clusters': clusters,
        'verticals': verticals,
        'horizontals': horizontals,
        'cluster1_graphic': cluster1_graphic,
        'cluster2_graphic': cluster2_graphic,
        'cluster3_graphic': cluster3_graphic,
    })
    return HttpResponse(template.render(context))


def detail(request, object_id):
    try:
        object = Student.objects.get(pk=object_id)
        object_scores = Scores.objects.filter(student=object_id).order_by('-discipline')
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'detail.html', {'object': object,
                                           'object_scores': object_scores})
# Create your views here.
