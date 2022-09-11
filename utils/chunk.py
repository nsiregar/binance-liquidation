def make_chunks(data, chunk_size):
    while data:
        chunk, data = data[:chunk_size], data[chunk_size:]
        yield chunk
