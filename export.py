import argparse
from reddit_db import RedditDB
import subprocess


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
            self.length = int(args.length[0])
        if args.flair:
            self.flair = args.flair

    def export(self):
        reddit_db = RedditDB()
        rows = reddit_db.get_url_by_flair(self.flair)
        url_list = []
        id_list = []
        duration = 0

        for row in rows:
            id_list.append(row[0])
            duration += row[1]
            subprocess.call([
                'ffmpeg', '-i', row[2], '-filter:v', 'fps=30', '-n',
                './video/' + row[0] + '.mp4'
            ])
            url_list.append('file ./video/' + row[0] + '.mp4\n')
            if duration > self.length:
                break

        f = open('video.list', 'w')
        f.writelines(url_list)
        f.close()
        subprocess.call(['sh', './make.sh', 'video.list', 'out.mp4'])
        reddit_db.update(id_list)


if __name__ == "__main__":
    ev = ExportVideo()
    ev.command_parse()
    ev.export()
