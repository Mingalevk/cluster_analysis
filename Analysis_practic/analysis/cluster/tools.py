import math


def euclidian_distance(score1, score2):
    sum_sqr = 0
    for i, j in zip(score1, score2):
        sum_sqr += (int(i)-int(j))**2
    distance = math.sqrt(sum_sqr)

    return distance

def new_centroid(scores):
    new_centroid_coordinates = []
    devisor = len(scores)
    average_score = 0
    for j in range(len(scores[0]) - 1):
        for i in scores:
            average_score =+ scores[i][j]/devisor
        new_centroid_coordinates.append(average_score)
        average_score = 0
    return new_centroid_coordinates