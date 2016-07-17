# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template, Context
from cluster.models import Student, Discipline, Scores
from django.http import Http404
#from cluster.tools import new_centroid

def index(request):
    template = loader.get_template('index2.html')
    data1 = list(Student.objects.filter(pk=1002))
    data2 = list(Student.objects.filter(pk=1003))
    data3 = list(Student.objects.filter(pk=1004))
    clusters = [data1, data2, data3]
    # {int(str(id)): [int(str(s)) for s in Scores.objects.filter(student_id=id)] for id in Student.objects.all()}
    #data_key = data.keys()
    #data_values = data.values()
    #centroids = [data_values[0], data_values[1], data_values[2]]
    #new_centroids = []
    #clusters = []
    #for i in clusters:
    #    new_centroids.append = new_centroid(clusters[i])
    #centroids = new_centroids
    #new_centroids = []
    context = RequestContext(request, {
        'clusters': clusters,
    })
    return HttpResponse(template.render(context))


def detail(request, object_id):
    try:
        object = Student.objects.get(pk=object_id)
        object_scores = Scores.objects.filter(student=object_id).order_by('-discipline')
    except Student.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'object': object,
                                           'object_scores': object_scores})
# Create your views here.
