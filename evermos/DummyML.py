def getModel(path):
    images = []
    for i in range(1525, 1600) :
        images.append('img/products/' + str(i) + '.jpg')
    return {'images':images}
