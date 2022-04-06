# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pydub
import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity
from os import listdir
from os.path import isfile, join
from scipy.spatial.distance import cdist

reduced_array_size = 2000

"""MP3 to numpy array"""

# mp3_file = open("thunderstorm.mp3", "rb")
# a = pydub.AudioSegment.from_mp3(mp3_file)
# y = np.array(a.get_array_of_samples())
# print(y)
def cos_sim_2d(x, y):
    norm_x = x / np.linalg.norm(x, axis=1, keepdims=True)
    norm_y = y / np.linalg.norm(y, axis=1, keepdims=True)
    return np.matmul(norm_x, norm_y.T)

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
# sr, x = read('songs/thunderstorm.mp3')
# step = x.size / reduced_array_size
# print("full size of thunderstorm")
# print(x.size)
# arr_thunderstorm = x[::math.floor(step)].flatten()
# arr_thunderstorm_slice = arr_thunderstorm[0:reduced_array_size]
#
# sr, x = read('songs/deepside.mp3')
# step = x.size / reduced_array_size
# deepside = x[::math.floor(step)].flatten()
# deepside_slice = deepside[0:reduced_array_size]
#
# sr, x = read('songs/italdialog1.mp3')
# step = x.size / reduced_array_size
# italdialog1 = x[::math.floor(step)].flatten()
# italdialog1_slice = italdialog1[0:reduced_array_size]
#
# sr, x = read('songs/italdialog2.mp3')
# step = x.size / reduced_array_size
# italdialog2 = x[::math.floor(step)].flatten()
# italdialog2_slice = italdialog2[0:reduced_array_size]
#
# sr, x = read('songs/zhinka_dr.mp3')
# step = x.size / reduced_array_size
# zhinka_dr = x[::math.floor(step)].flatten()
# zhinka_dr_slice = zhinka_dr[0:reduced_array_size]
#
# sr, x = read('songs/ennio1.mp3')
# step = x.size / reduced_array_size
# print("printing step")
# print(step)
# arr_ennio_1 = x[::math.floor(step)]
# arr_ennio_1_slice = np.array(arr_ennio_1.flatten()[0:reduced_array_size])
# print("slice size")
# print(arr_ennio_1_slice.size)
# #arr_ennio_1 = x[10000:100000]
# median1 = np.median(arr_ennio_1)
# # Assign the median to the zero elements
# arr_ennio_1_slice[arr_ennio_1_slice == 0] = median1
#
#
# sr, x = read('songs/ennio2.mp3')
# print("printing step")
# print(step)
# step = x.size / reduced_array_size
# arr_ennio_2 = x[::math.floor(step)]
# arr_ennio_2_slice = arr_ennio_2.flatten()[0:reduced_array_size]
#
# #arr_ennio_2 = x[10000:100000]
# median2 = np.median(arr_ennio_2)
# # Assign the median to the zero elements
# arr_ennio_2_slice[arr_ennio_2_slice == 0] = median2

# print("Arrays size")
# print(arr_ennio_2.size)
#
#
# print("Printing array1")
# print(arr_ennio_1)
# print("Printing array2")
# print(arr_ennio_2)

# print("cos_sim_2d similarity")
# print(cos_sim_2d(arr_ennio_1, arr_ennio_2))
# print("Average cosine similarity")
# print(np.average(cos_sim_2d(arr_ennio_1, arr_ennio_2)))

# print("Printing distance")
# print(spatial.distance.cosine(arr_ennio_1.flatten(), arr_ennio_2.flatten()))
# print("Printing similarity")
# print(1 - spatial.distance.cosine(arr_ennio_1.flatten(), arr_ennio_2.flatten()))

# print("sklearn similarity ennio1 and ennio2")
# print(cosine_similarity([arr_ennio_1_slice], [arr_ennio_2_slice]))
#
# print("sklearn similarity ennio2 and ennio1")
# print(cosine_similarity([arr_ennio_2_slice], [arr_ennio_1_slice]))
#
# print("sklearn similarity thundertorm and ennio2")
# print(cosine_similarity([arr_thunderstorm_slice], [arr_ennio_2_slice]))
#
# print("sklearn similarity thundertorm and zhinka_dr")
# print(cosine_similarity([arr_thunderstorm_slice], [zhinka_dr_slice]))
#
# print("sklearn similarity italdialog1 and italdialog2")
# print(cosine_similarity([italdialog1_slice], [italdialog2_slice]))
#
# print("sklearn similarity deepside and italdialog2")
# print(cosine_similarity([deepside_slice], [italdialog1_slice]))
#
# print("sklearn similarity italdialog1 and zhinka_dr")
# print(cosine_similarity([italdialog1_slice], [zhinka_dr_slice]))
#
# print("sklearn similarity italdialog2 and ennio2")
# print(cosine_similarity([italdialog2_slice], [arr_ennio_2_slice]))


#similarity = sklearn.metrics.pairwise.cosine_similarity()
#print(similarity)
def compare_two_songs(songfile1, songfile2):

    # print("Enter the first song to compare (full name with dot and extension):")
    # song1 = input()
    # print("Enter the second song to compare (full name with dot and extension):")
    # song2 = input()

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

    similarity  = cosine_similarity(song1_slice, song2_slice)
    mahalanobis = cdist(song1_slice, song2_slice, 'mahalanobis')

    print("Song 1 wiht itself")
    print(np.average(cdist(song1_slice, song1_slice, 'mahalanobis')))
    print("Song 2 wiht itself")
    print(np.average(cdist(song2_slice, song2_slice, 'mahalanobis')))


    euclidian = np.linalg.norm(song1_slice - song2_slice)
    print ("shape")
    # print(song1_slice.shape)
    #
    # i, j, k = song1_slice.shape
    #
    # song1_slice = song1_slice.reshape(i, j * k).T
    # i, j, k = song1_slice.shape
    #
    # song2_slice = song2_slice.reshape(i, j * k).T
    # similarity = cdist([song1_slice],  [song2_slice], 'mahalanobis')
    #
    # print("Cosine similarity:")
    # print(cosine_similartiy_2_songs)
    if (similarity[0][0] > 0):
        print("The songs: " + str(songfile1) + " " + str(songfile2) + " " + " are similar")
    else:
        print("The songs: " + str(songfile1) + " " + str(songfile2) + " " + " are not similar")
    return np.average(mahalanobis)




#similarity = sklearn.metrics.pairwise.cosine_similarity()
#print(similarity)

def find_most_simlar_song():

    print ("Type the name of the song for comparison:")

    song = input()

    for songfile in listdir("songs"):
        if isfile(join("songs", songfile)):
            similarity = compare_two_songs(song, songfile)
            print("Comparison results for " + songfile + " and " + song + "; rate: " + str(similarity) )



# import audio2numpy as a2n
# x,sr=a2n.audio_from_file("thunderstorm.mp3")
# print(x[222])

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    find_most_simlar_song()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

