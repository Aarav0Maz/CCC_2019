def run_length_encoding(s):
  encoded_message = []
  i = 0

  while i < len(s):
      count = 1
      current_char = s[i]
      # Count consecutive occurrences of the current character
      while i + 1 < len(s) and s[i] == s[i + 1]:
          count += 1
          i += 1
      # Append the count and character to the encoded message
      encoded_message.extend([str(count), current_char])
      i += 1
  return ' '.join(encoded_message)

def main():
  # Input
  n = int(input().strip())
  lines = [input().strip() for _ in range(n)]

  # Output
  for line in lines:
      result = run_length_encoding(line)
      print(result)

if __name__ == "__main__":
  main()