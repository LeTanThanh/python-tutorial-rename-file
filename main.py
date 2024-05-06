if __name__ == "__main__":
  # Python Rename File

  import os

  try:
    os.rename("readme.txt", "notes.txt")
  except FileNotFoundError as error:
    print(error)
  except FileExistsError as error:
    print(error)
