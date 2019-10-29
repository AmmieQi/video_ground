# Program To Read video
# and Extract Frames
import glob
import os
import cv2
import timeit

def video_file2id(video_file):
    basename = os.path.basename(video_file).split(".mp4")[0]
    return basename[2:]

def video2jpg(video_path, jpg_path):
    existing_vfs = glob.glob(video_path + "*.mp4")
    num_videos = len(existing_vfs)
    for idx, file in enumerate(existing_vfs):
        id = video_file2id(file)

        # create jpg folder if not exist, if exists skip the video
        jpg_folder = jpg_path + "jpg_" + id + "/"
        if not os.path.exists(jpg_folder):
            os.makedirs(jpg_folder)
        start = timeit.default_timer()
        fps, count = convert_one_video(file, jpg_folder)
        time_elapse = timeit.default_timer() - start
        print(idx + 1, "/", str(num_videos), ": ", id, " (fps:", str(fps), ", count:", str(count), ") time:",
              "%.2f" % round(time_elapse,2), "s", sep="")

# Function to extract frames
def convert_one_video(video_file, jpg_folder):
    # Path to video file
    vid_object = cv2.VideoCapture(video_file)
    fps = vid_object.get(cv2.CAP_PROP_FPS)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1
    sampled_fps = 5
    while success:
        vid_object.set(cv2.CAP_PROP_POS_MSEC, (count * 1000 / sampled_fps))
        # vidObj object calls read
        # function extract frames
        success, image = vid_object.read()

        # Saves the frames with frame-count
        cv2.imwrite(jpg_folder + "frame%d.jpg" % count, image)
        count += 1
    return fps, count




# Driver Code
if __name__ == '__main__':
    # Calling the function
    data_root = "../data/activitynet/"
    video_path = data_root + "videos/"
    jpg_path = data_root + "jpg/"

    # sample_video = video_path + "v__7GQcJezzo4.mp4"
    # FrameCapture(sample_video)

    video2jpg(video_path, jpg_path)