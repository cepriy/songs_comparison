import numpy as np
import math
import pydub
from sklearn.metrics.pairwise import cosine_similarity
from os import listdir
from os.path import isfile, join
from scipy.spatial.distance import cdist

reduced_array_size = 2500   #increment this number for a more detailed sampling;

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def compare_two_songs(songfile1, songfile2, method): #

    sr, x = read('songs/' + songfile1)
    step = x.size / reduced_array_size
    song1 = x[::math.floor(step)]
    song1_slice = song1[0:reduced_array_size]
    median1 = np.median(song1_slice)
    song1_slice[song1_slice == 0] = median1

    sr, x = read('songs/' + songfile2)
    step = x.size / reduced_array_size
    song2 = x[::math.floor(step)]
    song2_slice = song2[0:reduced_array_size]
    median2 = np.median(song2_slice)
    song2_slice[song2_slice == 0] = median2

    similarity = cdist(song1_slice, song2_slice, method)
    if (method == 'cosine'):                          # Hardcode for now! for the given arrays shape the 'pairwise' cosine algorythm provides clearer results, which is why the latter
                                                       #is now implemented and hardcoded. The discrepancies in the cosine similarity results are to be explored, if necessary.
        similarity  = cosine_similarity(song1_slice, song2_slice)

    print("Song 1 wiht itself")
    print(np.average(cdist(song1_slice, song1_slice, method )))
    print("Song 2 wiht itself")
    print(np.average(cdist(song2_slice, song2_slice, method)))

    if (method == 'cosine' and similarity[0][0] > 0):                 #Only valid for cosine similarity
        print("The songs: " + str(songfile1) + " " + str(songfile2) + " " + " are similar")
    else:
        print("The songs: " + str(songfile1) + " " + str(songfile2) + " " + " are not similar")
    return np.average(similarity)

def compare_songs_each_to_each(method):

    print ("Type the name of the song for comparison:")
    song = input()
    for songfile in listdir("songs"):
        if isfile(join("songs", songfile)):
            similarity = compare_two_songs(song, songfile, method)
            print("Comparison results for " + songfile + " and " + song + "; rate: " + str(similarity) )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    compare_songs_each_to_each('cosine')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

