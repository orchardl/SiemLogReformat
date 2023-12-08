import sys

def reformat_log_line(line):
    # Split the line at each '[' and join them back with '\n['
    return line.replace('[', '\n[').strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python reformat_log.py '<log_entry>'")
        sys.exit(1)

    log_entry = ' '.join(sys.argv[1:])

    formatted_line = reformat_log_line(log_entry)
    print(formatted_line)

if __name__ == "__main__":
    main()
