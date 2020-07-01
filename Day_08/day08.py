#Day 08
with open('data.txt', 'r') as f:
    data = f.readline()


def image_by_layers(image):
    layers = []
    for i in range(0, len(image), 150):
        layers.append(list(image[i:i + 150]))
    return layers


def corrupted_check(layers):
    count = float('inf')
    layer_index = None

    for index, layer in enumerate(layers):
        if layer.count('0') < count:
            count = layer.count('0')
            layer_index = index

    return layers[layer_index].count('1') * layers[layer_index].count('2')


image_layers = image_by_layers(data)
print(corrupted_check(image_layers))


def decode_image(layers):
    decoded = []
    for i, pixel in enumerate(layers[0]):
        if pixel == '0':
            decoded.append(' ')
        elif pixel == '1':
            decoded.append('#')
        elif pixel == '2':
            for j in range(1, len(layers)):
                if layers[j][i] == '0':
                    decoded.append(' ')
                    break
                elif layers[j][i] == '1':
                    decoded.append('#')
                    break
    return decoded


def print_image(layers):
    decoded = decode_image(layers)
    for k in range(0, len(decoded), 25):
        for m in range(25):
            print(decoded[k+m], end='')
        print('')


print_image(image_layers)
