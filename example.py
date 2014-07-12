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

    static int   check_sample_fmt(      AVCodec *codec, enum AVSampleFormat sample_fmt);
    static int   select_sample_rate     (AVCodec *codec);
    static int   select_channel_layout  (AVCodec *codec);
    static void  audio_encode_example   (const char *filename);
    static void  audio_decode_example   (const char *outfilename, const char *filename);
    static void  video_encode_example   (const char *filename, int codec_id);
    static void  video_decode_example   (const char *outfilename, const char *filename);
""")

libexample = ffi.verify("""
#include <math.h>

#include <libavutil/opt.h>
#include <libavcodec/avcodec.h>
#include <libavutil/channel_layout.h>
#include <libavutil/common.h>
#include <libavutil/imgutils.h>
#include <libavutil/mathematics.h>
#include <libavutil/samplefmt.h>
""", sources=["src/functions.c"],
    include_dirs=["src"],  # I think this is not necessary or correct.
    define_macros=[("INBUF_SIZE", "4096"),
                   ("AUDIO_INBUF_SIZE", "20480"),
                   ("AUDIO_REFILL_THRESH", "4096")],
    libraries=['avformat', 'avutil', 'avcodec'])
