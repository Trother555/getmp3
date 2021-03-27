import argparse
import os
import tempfile

import pytube
import ffmpeg


parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--path', 
                    default=os.path.join(os.path.expanduser('~'),
                                         'Downloads'))


def main():
    args = parser.parse_args()
    yt = pytube.YouTube(args.url)
    print('Getting the video')
    temp_path = yt.streams.get_highest_resolution().download(
        output_path=tempfile.gettempdir()
    )
    out_name = ''
    if not args.path.endswith('mp3'):
        out_name = (os.path.splitext(os.path.basename(temp_path))[0] +
                    '.mp3')
    out_path = os.path.join(args.path, out_name)
    print(f'Saving mp3 into {out_path}')
    ffmpeg.input(temp_path).output(out_path, loglevel='error').run()
    print(f'Removing temp file {temp_path}')
    os.remove(temp_path)


if __name__ == '__main__':
    main()
