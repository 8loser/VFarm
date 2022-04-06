import argparse
from reddit_db import RedditDB
import subprocess


class ExportVideo:

    def __init__(self):
        # 預設總長度10分鐘
        self.total_length = 600
        # 每個影片預設長度1分鐘內
        self.part_length = 60
        self.flair = []

    def command_parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-t',
                            '--total_length',
                            nargs='?',
                            type=int,
                            help='影片總時間長度(秒)')
        parser.add_argument('-p',
                            '--part_length',
                            nargs='?',
                            type=int,
                            help='片段最大時間長度')
        parser.add_argument('-f', '--flair', nargs='*', help='flair')
        args = parser.parse_args()
        if args.total_length:
            self.total_length = args.total_length
        if args.flair:
            self.flair = args.flair
        if args.part_length:
            self.part_length = args.part_length

    def export(self):
        reddit_db = RedditDB()
        reddit_db.set_flair(self.flair)
        reddit_db.set_duration(self.part_length)
        rows = reddit_db.query()
        url_list = []
        id_list = []
        duration = 0

        for row in rows:
            id_list.append(row[0])
            duration += row[1]
            # 每個影片 fps 要固定，不然合併後會有影音不同不情況
            subprocess.call([
                'ffmpeg', '-i', row[2], '-filter:v', 'fps=30', '-n',
                './video/' + row[0] + '.mp4'
            ])
            url_list.append('file ./video/' + row[0] + '.mp4\n')
            if duration > self.total_length:
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
