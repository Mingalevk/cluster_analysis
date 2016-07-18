# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template, Context
from cluster.models import Student, Discipline, Scores
from django.http import Http404
from cluster.tools import Cluster, k_means, Point


def index(request):
    template = loader.get_template('index2.html')
    data = {int(str(id)): [float(str(s)) for s in Scores.objects.filter(student_id=id).order_by('discipline')] for id in Student.objects.all()}

    cluster1 = Cluster()
    cluster2 = Cluster()
    cluster3 = Cluster()
    clusters = [cluster1, cluster2, cluster3]
    k_means(data, clusters)

    context = RequestContext(request, {
        'clusters': clusters
    })
    return HttpResponse(template.render(context))


def detail(request, object_id):
    try:
        object = Student.objects.get(pk=object_id)
        object_scores = Scores.objects.filter(student=object_id).order_by('discipline')
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'detail.html', {'object': object,
                                           'object_scores': object_scores})
# Create your views here.
