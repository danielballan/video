"""Usage:

from example import libexample, arg
libexample.video_decode_example(arg('outfile'), arg('infile'))
"""

from __future__ import print_function
from cffi import FFI


ffi = FFI()

C = ffi.dlopen(None)

# These raise if the library is not found. They are working properly.
libavformat = ffi.dlopen('avformat')
libavutil = ffi.dlopen('avutil')
libavcodec = ffi.dlopen('avcodec')

print('Loaded lib {0}'.format(libavformat))
print('Loaded lib {0}'.format(libavutil))
print('Loaded lib {0}'.format(libavcodec))

ffi.cdef("""
    typedef ... AVCodec;
    typedef ... AVSampleFormat;
    typedef ... AVFormatContext;
    typedef ... AVStream;
    typedef ... AVMediaType;
    
    int    check_sample_fmt            (AVCodec *codec, enum AVSampleFormat sample_fmt);
    int    select_sample_rate          (AVCodec *codec);
    int    select_channel_layout       (AVCodec *codec);
    void   audio_encode_example        (const char *filename);
    void   audio_decode_example        (const char *outfilename, const char *filename);
    void   video_encode_example        (const char *filename, int codec_id);
    void   video_decode_example        (const char *outfilename, const char *filename);
    void   initialize                  ();
    int    demux                       (int argc, char **argv);
    int    decode_packet               (int *got_frame, int cached);
    int    open_codec_context          (int *stream_idx, AVFormatContext *fmt_ctx, enum AVMediaType type);
    int    get_format_from_sample_fmt  (const char **fmt, enum AVSampleFormat sample_fmt);
""")

libexample = ffi.verify("""
#include "functions.h"
""", sources=["src/functions.c"],
    include_dirs=["src"],  # I think this is not necessary or correct.
    define_macros=[("INBUF_SIZE", "4096"),
                   ("AUDIO_INBUF_SIZE", "20480"),
                   ("AUDIO_REFILL_THRESH", "4096")],
    libraries=['avformat', 'avutil', 'avcodec'])

libexample.initialize()

def arg(filename):
    "Utility for unboxing string args."
    return ffi.new("char[]", filename)


