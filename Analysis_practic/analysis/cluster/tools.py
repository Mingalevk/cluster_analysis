#coding: utf8
import math
from cluster.models import Student, Discipline, Scores


class Cluster:
    __i = 0

    def __init__(self):
        Cluster.__i += 1
        self.name = 'Кластер'+str(Cluster.__i)
        self.centroid = None
        self.prev_centroid = None
        self.graphic = []
        self.objects = {}
        self.students = []

    def __del__(self):
        Cluster.__i = 0

    def set_centroid(self, new_centroid):
        self.prev_centroid = list(new_centroid) if self.prev_centroid == None else self.centroid
        self.centroid = list(new_centroid)

    def add_object(self, key, value):
        self.objects.update({key: value})
        self.__get_student()

    def recalculate_centroid(self):
        coordinate_lists = zip(*(self.objects.values()))  # лист листов 1х, 2х и т.д. координат
        new_centroid_coordinates = map(lambda x: sum(x)/len(x), coordinate_lists)
        #self.prev_centroid = self.centroid
        self.__calculate_cluster_graphic()  # координаты кластера для вывода на график
        self.set_centroid(new_centroid_coordinates)  # для вывода нужно преобразовать в list

    def clear_cluster(self):
        self.objects.clear()

    def __calculate_cluster_graphic(self):
        scores_lists = zip(*(self.objects.values()))  # лист листов 1х, 2х и т.д. оценок
        vcoordinates = list(map(lambda x: sum(x)/len(x)*100, scores_lists))
        for h, v in enumerate(vcoordinates, 1):
            self.graphic.append(Point((h * 100.0), abs(600 - v)))

    def __get_student(self):
        self.students = [Student.objects.get(pk=id) for id in list(self.objects.keys())]


class Point:
    def __init__(self, h_coordinate, v_coordinate):
        self.h_coordinate = h_coordinate
        self.v_coordinate = v_coordinate


def euclidian_distance(score1, score2):
    distance = math.sqrt(sum([(x-y)**2 for x, y in zip(score1, score2)]))
    return float("%.15f" % distance)


def clustering(scores, __clusters):
    for score in scores:
        distances = [euclidian_distance(scores[score], cluster.centroid) for cluster in __clusters]  # лист с расстояниями до каждого центроида
        clnum = distances.index(min(distances))  # определение наименьшего расстояния и соответственно кластера, в который будет помещен объект
        __clusters[clnum].add_object(score, scores[score])  # запись в кластер


def k_means(__data, __clusters):
    for num, cluster in enumerate(__clusters, 0):
        cluster.set_centroid(__data[list(__data.keys())[num]])
    clustering(__data, __clusters)
    #for cluster in clusters:
    #    cluster.recalculate_centroid()
    [cluster.recalculate_centroid() for cluster in __clusters]  # То же самое, что и две предыдущих строки
    while any(abs(euclidian_distance(cluster.centroid, cluster.prev_centroid)) > 10**-3 for cluster in __clusters):  # С точностью надо будет определиться еще
        #for cluster in clusters:
        #    cluster.clear_cluster()
        [cluster.clear_cluster() for cluster in __clusters]
        clustering(__data, __clusters)
        #for cluster in __clusters:
        #    cluster.recalculate_centroid()
        [cluster.recalculate_centroid() for cluster in __clusters]



#data = {int(str(id)): [int(str(s)) for s in Scores.objects.filter(student_id=id)] for id in Student.objects.all()}
data = {1: [5, 4], 2: [5, 3], 4: [4, 4], 5: [3, 4]}

cluster1 = Cluster()
cluster2 = Cluster()
cluster3 = Cluster()
clusters = [cluster1, cluster2, cluster3]

k_means(data, clusters)
