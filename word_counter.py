from pprint import pprint

# Single
# 1e6  -> 0.47s
# 1e9  -> 456.67s
# 1e12 -> nope...

def main():
  chunk_size = 18
  main_word_map = {}

  buffer = ""
  is_eod = False
  with open('./fruits_1e9.txt', 'r') as file:
    while not is_eod:
      next_chunk =  file.read(chunk_size)
      chunk = buffer + next_chunk
      clean_chunk, _, to_buffer = chunk.rpartition(",")
      if not next_chunk: # end of string
        clean_chunk = buffer
        buffer = ""
        is_eod = True
      else:
        buffer = to_buffer

      # print(f"{chunk} -> {clean_chunk}")
      chunk_word_map = create_map(clean_chunk)
      main_word_map = merge_maps(main_word_map, chunk_word_map)

  return main_word_map

def create_map(s: str) -> dict:
  word_map = {}
  for word in s.split(","):
    if word in word_map:
      word_map[word] += 1
      continue
    word_map[word] = 1
  return word_map

def merge_maps(*maps) -> dict:
  main_word_map = {}
  for map in maps:
    for word, count in map.items():
      if word in main_word_map:
        main_word_map[word] += count
        continue
      main_word_map[word] = count
  return main_word_map

if __name__ == "__main__":
  result = main()
  pprint(result)