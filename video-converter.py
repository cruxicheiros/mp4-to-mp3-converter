import ffmpeg, os

indir = "./input/"
outdir = "./output/"

if not os.path.exists(indir):
    print("Please add an input directory at: " + indir + " and put your mp4 files in it.")
    quit()

if not os.path.exists(outdir):
    os.makedirs(outdir)

for filename in os.listdir(indir):
	file_prefix = filename.split('.')[0]

	sound = ffmpeg.input(indir + filename).audio  # Import the video and get the audio from it
	normalised = ffmpeg.filter(sound, "dynaudnorm")  # Apply dynamic audio compression (fixing any volume issues)
	out_sound = ffmpeg.output(normalised, outdir + file_prefix + '.mp3', audio_bitrate='96k') # Output at a low bitrate as a mp3


	ffmpeg.run(out_sound) # Process the prior instructions (time intensive step)
	


