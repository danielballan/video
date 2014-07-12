#include <math.h>

#include <libavutil/opt.h>
#include <libavcodec/avcodec.h>
#include <libavutil/channel_layout.h>
#include <libavutil/common.h>
#include <libavutil/imgutils.h>
#include <libavutil/mathematics.h>
#include <libavutil/samplefmt.h>
#include <libavformat/avformat.h>

int    check_sample_fmt       (AVCodec *codec, enum AVSampleFormat sample_fmt);
int    select_sample_rate     (AVCodec *codec);
int    select_channel_layout  (AVCodec *codec);
void   audio_encode_example   (const char *filename);
void   audio_decode_example   (const char *outfilename, const char *filename);
void   video_encode_example   (const char *filename, int codec_id);
void   video_decode_example   (const char *outfilename, const char *filename);
void   initialize             ();
