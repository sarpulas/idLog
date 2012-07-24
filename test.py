def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
if __name__ == "__main__":
    import sys
    for char in reverse('golf'):
      print char