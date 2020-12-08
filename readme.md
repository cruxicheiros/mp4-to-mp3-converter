# MP4 to MP3 converter

I made this script to help me convert my lecture videos into audio files I can put on my phone to revise from. It:
 * Converts mp4s to mp3s
 * Specifies bitrate as 96kb
 * Applies dynamic range compression to fix any audio volume issues that sometimes happen if the person recording the video moves away from the mic

It could in the future:
 * Help you apply metadata to mp3s to make them easier to find in audio players
 * Allow you to set your own input and output directories
 * Retain tree structure in input and output directories 

## Dependencies

I made it using [ffmpeg-python](https://github.com/kkroening/ffmpeg-python/) because I wanted to try it out, but this should be simple enough to convert to a bash script if that is what you prefer. The ffmpeg-python library was made by Karl Kroening and is licensed under the Apache License 2.0. You will also have to install ffmpeg to use this, which is licensed under LGPL but may contain GPL components.

## How to use

In the same directory as `video-converter.py`, create a `input/` folder. Put your MP4 video files in that. Then, execute the script with `python video-converter.py`. If any file names clash with files in the directory, you will be prompted by ffmpeg as to whether you want to overwrite them - so if you do not want to interact with this script at all then make sure your `output/` directory is clear.

## License

MIT license. More detail in LICENSE.txt.

## Final notes

I have only tested this on Linux. It probably works on other platforms but I can't guarantee that.
