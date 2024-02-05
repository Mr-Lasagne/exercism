def accumulate(collection, operation):
    response = []
    for element in collection:
        response.append(operation(element))
    return response
