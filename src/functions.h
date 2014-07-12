#include <math.h>

#include <libavutil/opt.h>
#include <libavcodec/avcodec.h>
#include <libavutil/channel_layout.h>
#include <libavutil/common.h>
#include <libavutil/imgutils.h>
#include <libavutil/mathematics.h>
#include <libavutil/samplefmt.h>
#include <libavformat/avformat.h>

/* from second example */
#include <libavutil/imgutils.h>
#include <libavutil/samplefmt.h>
#include <libavutil/timestamp.h>
#include <libavformat/avformat.h>

static AVFormatContext *fmt_ctx = NULL;

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
