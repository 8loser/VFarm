import argparse


class ExportVideo:

    def __init__(self):
        self.length = 600
        self.flair = []

    def command_parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--length', nargs='+', help='時間長度(秒)')
        parser.add_argument('-f', '--flair', nargs='+', help='flair')
        args = parser.parse_args()
        if args.length:
            self.length = args.length
        if args.flair:
            self.flair = args.flair

    def export(self):
        print(self.length, self.flair)


if __name__ == "__main__":
    ev = ExportVideo()
    ev.command_parse()
    ev.export()
