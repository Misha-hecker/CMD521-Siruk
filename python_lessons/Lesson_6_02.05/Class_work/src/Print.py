def print_people(data):
    if isinstance(data, dict) and 'results' in data:
        data = data['results']

    headers = ["name", "height", "mass", "hair_color", "gender"]
    rows = [[str(item.get(h, "")) for h in headers] for item in data]

    col_widths = [max(len(headers[i]), max((len(row[i])
                      for row in rows), default=0)) for i in range(len(headers))]
    header_row = " | ".join(headers[i].ljust(col_widths[i])
                            for i in range(len(headers)))
    separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    print(header_row)
    print(separator)
    for row in rows:
        print(" | ".join(row[i].ljust(col_widths[i])
              for i in range(len(headers))))