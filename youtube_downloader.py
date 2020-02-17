from pytube import YouTube

url = input('Please Enter The Youtube URL:\n')
audio_streams = YouTube(url).streams.filter(only_audio=True).all()
highest_abr = 0
# stream_itag = ''
strm = None
for stream in audio_streams:
    if stream.abr and int(stream.abr.split('k')[0]) > highest_abr:
        highest_abr = int(stream.abr.split('k')[0])
        # stream_itag = stream.itag
        strm = stream
print('\nDownload Quality: ' + str(highest_abr) + 'kbps' + '\n')
if stream.itag != '':
    print(strm.download())
