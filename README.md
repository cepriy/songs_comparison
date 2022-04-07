This is a straightforward algorythm for analyzing cosine, euclidean, mahalanobis and othe similarity types between pairs of audio mp3 files once converted into numpy arrays. The arrays are subject to sampling, and the cosine similarity algorithm used on 100000-sized or greater arrays yields some rough, still questionable, results.
The mahalonobis comparisons results seem quite weird and should be explored in a deeper way. However, 
a specific feature extraction approach looks much more promising, which will be implemented in another project. 
The implemented library is
scipy.spatial.distance.cdist
The possible metric methods can be  ‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘cityblock’, ‘correlation’, ‘cosine’, ‘dice’, ‘euclidean’, ‘hamming’, ‘jaccard’, ‘jensenshannon’, ‘kulsinski’, ‘kulczynski1’, ‘mahalanobis’, ‘matching’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’.
Nevertheless, for the given arrays shape the 'pairwise' cosine algorythm provides clearer results, which is why the latter
is now implemented and hardcoded. The discrepancies in the cosine similarity results are to be explored, if necessary.