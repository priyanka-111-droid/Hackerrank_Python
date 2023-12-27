def print_from_stream(n, stream=EvenStream()):
    
    for _ in range(n):
        print(stream.get_next())
    stream.current=0

# here default value of stream is EvenStream
# in EvenStream class, stream.current has to be 0.
# So we set to 0.
# for oddstream,stream.current is set to 1.