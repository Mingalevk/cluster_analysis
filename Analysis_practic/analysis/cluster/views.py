# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template, Context
from cluster.models import Student, Discipline, Scores
from django.http import Http404
from cluster.tools import Cluster, k_means, Point


def index(request):
    template = loader.get_template('index2.html')
    data = {int(str(id)): [int(str(s)) for s in Scores.objects.filter(student_id=id)] for id in Student.objects.all()}
    cluster1 = Cluster()
    cluster2 = Cluster()
    cluster3 = Cluster()
    clusters = [cluster1, cluster2, cluster3]
    k_means(data, clusters)

    verticals = [s * 100 for s in range(7)]
    horizontals = [s * 100 for s in range(5)]
    lines = [l*100 + i for l in range(1, 3, 1) for i in range(10, 100, 10)]

    context = RequestContext(request, {
        'clusters': clusters,
        'verticals': verticals,
        'horizontals': horizontals,
        'lines': lines
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
