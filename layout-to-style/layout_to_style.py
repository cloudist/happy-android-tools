import sys


def clean_style_key(line):
    return line.strip()


def clean_style_value(line):
    start_index = line.index('"') + 1
    end_index = line.rindex('"')
    return line[start_index:end_index]


def main():
    style_template = '<item name="%s">%s</item>'

    for line in sys.stdin.readlines():
        cleaned_line = line.strip()
        cuts = cleaned_line.split('=')

        if len(cuts) != 2:
            continue

        style_key = clean_style_key(cuts[0])
        style_value = clean_style_value(cuts[1])

        print style_template % (style_key, style_value)


if __name__ == '__main__':
    main()
