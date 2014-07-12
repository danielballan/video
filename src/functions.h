#include <math.h>

#include <libavutil/opt.h>
#include <libavcodec/avcodec.h>
#include <libavutil/channel_layout.h>
#include <libavutil/common.h>
#include <libavutil/imgutils.h>
#include <libavutil/mathematics.h>
#include <libavutil/samplefmt.h>

static int   check_sample_fmt       (AVCodec *codec, enum AVSampleFormat sample_fmt);
static int   select_sample_rate     (AVCodec *codec);
static int   select_channel_layout  (AVCodec *codec);
static void  audio_encode_example   (const char *filename);
static void  audio_decode_example   (const char *outfilename, const char *filename);
static void  video_encode_example   (const char *filename, int codec_id);
static void  video_decode_example   (const char *outfilename, const char *filename);

