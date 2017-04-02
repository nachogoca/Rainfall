import csv


def handle_upload_file(file):
    # Write file
    print("writing file")
    with open('tmp/upload.csv', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    print("Processing csv")
    with open(file.name) as f:
        reader = csv.reader(f)
        for row in reader:
            _, print("hi")
    return True