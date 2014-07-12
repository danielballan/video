from __future__ import print_function
from cffi import FFI


ffi = FFI()

C = ffi.dlopen(None)

# These raise if the library is not found. They are working properly.
libavformat = ffi.dlopen('avformat')
libavutil = ffi.dlopen('libavutil')
libavcodec = ffi.dlopen('libavcodec')

print('Loaded lib {0}'.format(libavformat))
print('Loaded lib {0}'.format(libavutil))
print('Loaded lib {0}'.format(libavcodec))

ffi.cdef("""
    typedef ... AVCodec;
    typedef ... AVSampleFormat;

    int    check_sample_fmt       (AVCodec *codec, enum AVSampleFormat sample_fmt);
    int    select_sample_rate     (AVCodec *codec);
    int    select_channel_layout  (AVCodec *codec);
    void   audio_encode_example   (const char *filename);
    void   audio_decode_example   (const char *outfilename, const char *filename);
    void   video_encode_example   (const char *filename, int codec_id);
    void   video_decode_example   (const char *outfilename, const char *filename);
""")

libexample = ffi.verify("""
#include "functions.h"
""", sources=["src/functions.c"],
    include_dirs=["src"],  # I think this is not necessary or correct.
    define_macros=[("INBUF_SIZE", "4096"),
                   ("AUDIO_INBUF_SIZE", "20480"),
                   ("AUDIO_REFILL_THRESH", "4096")],
    libraries=['avformat', 'avutil', 'avcodec'])
